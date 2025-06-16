import pytest
from models.config import Envs
from clients.spends_client import SpendsHttpClient
from clients.category_client import CategoryHttpClient
from databases.spend_db import SpendDb
from databases.auth_db import UserDb
from databases.user_db import UserdataDb


@pytest.fixture(scope='session')
def spends_client(envs: Envs, auth_api_token: str) -> SpendsHttpClient:
    return SpendsHttpClient(envs, auth_api_token)


@pytest.fixture(scope="session")
def spend_db(envs: Envs) -> SpendDb:
    return SpendDb(envs)


@pytest.fixture(scope="session")
def auth_db(envs: Envs) -> UserDb:
    return UserDb(envs)


@pytest.fixture()
def user_db(envs: Envs) -> UserdataDb:
    return UserdataDb(envs)


@pytest.fixture(scope='session')
def category_client(envs: Envs, auth_api_token: str) -> CategoryHttpClient:
    return CategoryHttpClient(envs, auth_api_token)