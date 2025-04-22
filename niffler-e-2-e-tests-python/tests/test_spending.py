from pages.spending_page import spending_page
from marks import Pages, TestData

TEST_CATEGORY = "school"


class TestSpending:

    @Pages.main_page
    def test_spending_title_exists(self):
        spending_page.check_spending_page_titles()


    @Pages.main_page
    @TestData.category(TEST_CATEGORY)
    @TestData.spends({
        "amount": "108.51",
        "description": "QA.GURU Python Advanced 1",
        "category": TEST_CATEGORY,
        "spendDate": "2024-08-08T18:39:27.955Z",
        "currency": "RUB"
    })
    def test_create_spending(self, category, spends):
        spending_page.check_spending_exists(TEST_CATEGORY, 100)

    @Pages.main_page
    def test_empty_category(self):
        spending_page.create_spending(100, 'RUB', '', 'breakfast')
        spending_page.check_error_message()
