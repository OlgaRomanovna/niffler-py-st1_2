import os
import pytest
from .pages.login_page import login_page
from .pages.spending_page import spending_page


@pytest.fixture(scope="function", autouse=True)
def login():
    user = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")
    login_page.sign_in(user, password)

class TestSpending:

    def test_spending_title_exists(self):
        spending_page.check_spending_page_titles()


    def test_create_spending(self):
        spending_page.create_spending(100, 'RUB', 'school', 'breakfast')
        spending_page.check_spending_exists('school', 100)