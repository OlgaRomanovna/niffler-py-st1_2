import os
import pytest
from .pages.login_page import login_page
from .pages.spending_page import spending_page


class TestLogin:

    def test_successful_login(self):
        username = os.getenv('USER_NAME')
        password = os.getenv('PASSWORD')

        login_page.sign_in(username, password)
        spending_page.check_spending_page_titles()


    test_data = [
        {'username': os.getenv('USER_NAME'), 'password': 12345},
        {'username': 'Helga', 'password': '56789'}]

    @pytest.mark.parametrize('user', test_data)
    def test_wrong_data(self, user):
        login_page.sign_in(user['username'], user['password'])
        login_page.check_error_message()
