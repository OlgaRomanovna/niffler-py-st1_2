import os
import time

from dotenv import load_dotenv
import pytest
from selene import browser
from faker import Faker
from clients.spends_clients import SpendsHttpClient


@pytest.fixture(scope="session", autouse=True)
def envs():
    load_dotenv()

@pytest.fixture(scope="session")
def frontend_url(envs):
    return os.getenv("FRONTEND_URL")


@pytest.fixture(scope="session")
def gateway_url(envs):
    return os.getenv("GATEWAY_URL")

@pytest.fixture(scope="session")
def profile_url(envs):
    return os.getenv("PROFILE_URL")


@pytest.fixture(scope="session")
def app_user(envs):
    return os.getenv("USER_NAME"), os.getenv("PASSWORD")


@pytest.fixture(scope="session")
def auth(frontend_url, app_user):
    username, password = app_user
    browser.open(frontend_url)
    browser.element('a:nth-child(1)').click()
    browser.element('input[name=username]').type(username)
    browser.element('input[name=password]').type(password)
    browser.element('button[type=submit]').click()
    time.sleep(5)
    return browser.driver.execute_script('return window.sessionStorage.getItem("id_token");')


@pytest.fixture(scope="session")
def spends_client(gateway_url, auth) -> SpendsHttpClient:
    return SpendsHttpClient(gateway_url, auth)


@pytest.fixture(params=[])
def category(request, spends_client):
    category_name = request.param
    current_categories = spends_client.get_categories()
    category_names = [category["category"] for category in current_categories]
    if category_name not in category_names:
        spends_client.add_category(category_name)
    return category_name


@pytest.fixture(params=[])
def spends(request, spends_client: SpendsHttpClient):
    test_spend = spends_client.add_spends(request.param)
    yield test_spend
    all_spends = spends_client.get_spends()
    if test_spend["id"] in [spend["id"] for spend in all_spends]:
        spends_client.remove_spends([test_spend["id"]])


@pytest.fixture()
def main_page(auth, frontend_url):
    browser.open(frontend_url)

@pytest.fixture()
def profile_page(auth, profile_url):
    browser.open(profile_url)


@pytest.fixture(scope='function', autouse=True)
def setup_browser(frontend_url):
    browser.config.base_url = frontend_url
    browser.config.window_width = 1200
    browser.config.window_height = 800

    browser.open('/')
    yield
    browser.quit()

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