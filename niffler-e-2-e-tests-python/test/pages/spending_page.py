from selene import browser, be, have, query


class SpendingPage:
    def __init__(self):
        self.history = browser.element('.main-content__section-history h2')
        self.statistics = browser.element('//*[@id="stat"]/h2')
        self.new_spending = browser.element("#react-select-3-placeholder")
        self.spending_container = browser.element('.table.spendings-table td')
        self.amount = browser.element('input[name=amount]')
        self.currency = browser.element('input[name=currency]')
        self.category = browser.element('#react-select-3-input')
        self.description = browser.element('input[name=description]')
        self.add_button = browser.element('button[type=submit]')

    def check_spending_page_titles(self):
        browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.history.should(have.text('History of spendings'))

    def create_spending(self, amount: int, currency: str, category: str, description: str = None):
        self.amount.clear().should(be.blank).type(amount)

        if currency and currency != "RUB":
            browser.element('div[id="currency"]').click()
            browser.element(f'.MuiButtonBase-root[data-value="{currency}"]').click()

        self.category.type(category).press_enter()

        if description:
            self.description.should(be.blank).type(description)

        self.add_button.click()

    def check_spending_exists(self, category, amount):
        filtered_cells = browser.all('.table.spendings-table td').filtered_by(have.text(f'{category} {amount}'))

        for cell in filtered_cells:
            print(f"Найдена ячейка с текстом: {cell.get(query.text)}")


spending_page = SpendingPage()