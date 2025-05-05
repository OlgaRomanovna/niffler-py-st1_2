from selene import browser, have


class ProfilePage:

    def __init__(self):
        self.input_category = browser.element('.add-category__input-container .form__input')
        self.button_add_category = browser.element('.add-category__input-container button')
        self.successful_alert =  browser.element('div[role="alert"] div:nth-child(2)')
        self.error_alert = browser.element('.add-category__input-container button')
        self.firstname = browser.element('[name="firstname"]')
        self.surname = browser.element('[name="surname"]')
        self.button_submit = browser.element('[type="submit"]')

    def successful_adding(self):
        self.successful_alert.should(have.text('New category added'))

    def check_adding_category(self, category):
        self.input_category.type(category)
        self.button_add_category.click()


    def check_error_message(self):
        self.successful_alert.should(have.text('Can not add new category'))

    def check_adding_empty_name_category(self):
        self.input_category.type('')
        self.button_add_category.click()
        self.check_error_message()

    def check_filling_form(self, name, surname):
        self.firstname.set_value(name)
        self.surname.set_value(surname)
        self.button_submit.click()

        self.successful_alert.should(have.text('Profile successfully updated'))


profiles_page = ProfilePage()
