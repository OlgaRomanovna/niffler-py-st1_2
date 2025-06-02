import os
import pytest
from dotenv import load_dotenv
from pages.login_page import login_page
from pages.spending_page import spending_page
from marks import Pages

class TestLogin:

    @Pages.main_page
    def test_successful_login(self):
        spending_page.check_spending_page_titles()

    load_dotenv()
    test_data = [
        {'username': os.getenv("USER_NAME"), 'password': 12345},
        {'username': 'Helga', 'password': '56789'}]

    @pytest.mark.parametrize('user', test_data)
    def test_wrong_data(self, user):
        login_page.sign_in(user['username'], user['password'])
        login_page.check_category_error_message()
