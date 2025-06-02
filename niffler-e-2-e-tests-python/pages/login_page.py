import allure
from selene import browser, be, have

from utils.helper import step


class LoginPage:
    def __init__(self):
        self.username = browser.element('input[name=username]')
        self.password = browser.element('input[name=password]')
        self.submit_button = browser.element('button[type=submit]')
        self.login_button = browser.element('a:nth-child(1)')
        self.create_new_user_button = browser.element('a:nth-child(2)')
        self.error_message = browser.element("//p[@class='form__error']")

    @step
    @allure.step('UI: sign in user')
    def sign_in(self, user: str, password: str):
        self.login_button.click()
        self.username.should(be.blank).type(user)
        self.password.should(be.blank).type(password)
        self.submit_button.click()

    @step
    @allure.step('UI: check text about error')
    def check_error_message(self):
        self.error_message.should(have.text('Неверные учетные данные пользователя'))


login_page = LoginPage()