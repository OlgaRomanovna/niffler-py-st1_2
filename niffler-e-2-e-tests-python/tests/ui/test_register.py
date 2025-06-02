import os
from pages.login_page import login_page
from pages.register_page import registration_page

class TestRegistration:

    def test_successful_registration(self, generate_test_user):
        username, password = generate_test_user
        login_page.create_new_user_button.click()
        registration_page.sign_up(username, password, password)
        registration_page.check_registration_message()

    def test_mismatch_password(self, generate_test_user):
        username, password = generate_test_user
        login_page.create_new_user_button.click()
        registration_page.sign_up(username, password, 'password')
        registration_page.check_category_error_message()

    def test_double_registration(self, generate_test_user):
        username = os.getenv('USER_NAME')
        password = 12345
        login_page.create_new_user_button.click()
        registration_page.sign_up(username, password, password)
        registration_page.check_already_exist_user(username)

