import os
import time

from dotenv import load_dotenv
import pytest
from selene import browser
from faker import Faker
from clients.spends_clients import SpendsHttpClient
from databases.spend_db import SpendDb
from models.config import Envs


@pytest.fixture(scope="session")
def envs() -> Envs:
    load_dotenv()
    return Envs(
        frontend_url=os.getenv("FRONTEND_URL"),
        gateway_url=os.getenv("GATEWAY_URL"),
        spend_db_url=os.getenv("SPEND_DB_URL"),
        profile_url=os.getenv("PROFILE_URL"),
        test_username=os.getenv("USER_NAME"),
        test_password=os.getenv("PASSWORD")
    )


@pytest.fixture(scope="session")
def auth(envs):
    browser.open(envs.frontend_url)
    browser.element('a:nth-child(1)').click()
    browser.element('input[name=username]').set_value(envs.test_username)
    browser.element('input[name=password]').set_value(envs.test_password)
    browser.element('button[type=submit]').click()
    time.sleep(3)

    return browser.driver.execute_script('return window.sessionStorage.getItem("id_token")')


@pytest.fixture(scope="session")
def spends_client(envs, auth) -> SpendsHttpClient:
    return SpendsHttpClient(envs.gateway_url, auth)


@pytest.fixture(scope="session")
def spend_db(envs) -> SpendDb:
    return SpendDb(envs.spend_db_url)


@pytest.fixture(params=[])
def category(request, spends_client, spend_db):
    category_name = request.param
    categories = spends_client.get_categories()
    existing_category = next((cat for cat in categories if cat.category == category_name), None)

    if existing_category:
        category = existing_category
        created = False
    else:
        category = spends_client.add_category(category_name)
        created = True
    yield category
    if created:
        spend_db.delete_category(category.id)

@pytest.fixture(params=[])
def category_db(request, spends_client, spend_db):
    category = spends_client.add_category(request.param)
    yield category
    spend_db.delete_category(category.id)


@pytest.fixture(params=[])
def spends(request, spends_client):
    test_spend = spends_client.add_spends(request.param)
    yield test_spend
    all_spends = spends_client.get_spends()
    if test_spend.id in [spend.id for spend in all_spends]:
        spends_client.remove_spends([test_spend.id])


@pytest.fixture()
def main_page(auth, envs):
    browser.open(envs.frontend_url)


@pytest.fixture()
def profile_page(auth, envs):
    browser.open(envs.profile_url)


@pytest.fixture
def generate_test_user():
    fake = Faker()
    name = fake.user_name()
    password = fake.password()
    return name, password

@pytest.fixture
def generate_category_name():
    fake = Faker()
    return fake.word()