import pytest
from models.config import Envs
from pages.spending_page import spending_page
from clients.spends_client import SpendsHttpClient
from clients.category_client import CategoryHttpClient
from databases.spend_db import SpendDb
from models.category import CategoryAdd
from _pytest.fixtures import FixtureRequest


@pytest.fixture(params=[])
def category(request: FixtureRequest, category_client: CategoryHttpClient, spend_db: SpendDb):
    category_name = request.param
    category = category_client.add_category((CategoryAdd(name=category_name)))
    yield category.name
    spend_db.delete_category(category.id)


@pytest.fixture(params=[])
def category_db(request: FixtureRequest, category_client: CategoryHttpClient, spend_db: SpendDb):
    category = category_client.add_category(request.param)
    yield category
    spend_db.delete_category(category.id)


@pytest.fixture(params=[])
def spends(request: FixtureRequest, spends_client: SpendsHttpClient):
    t_spend = spends_client.add_spends(request.param)
    yield t_spend
    all_spends = spends_client.get_spends()
    if t_spend.id in [spend.id for spend in all_spends]:
        spends_client.remove_spends([t_spend.id])


@pytest.fixture()
def delete_spend(request: FixtureRequest, auth: str, envs: Envs):
    name_category = request.param
    yield name_category
    spending_page.delete_spend(name_category)