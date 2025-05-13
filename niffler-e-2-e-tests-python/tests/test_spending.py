import pytest
from selene import browser

from models.spend import SpendAdd
from pages.spending_page import spending_page
from marks import Pages, TestData

pytestmark = [pytest.mark.allure_label("Spendings", label_type="epic")]

TEST_CATEGORY = "school"
TEST_CATEGORY_2 = "investments"


class TestSpending:

    @Pages.main_page
    def test_spending_title_exists(self):
        spending_page.check_spending_page_titles()

    @pytest.fixture()
    def main_page_late(self, category, spends, envs):
        browser.open(envs.frontend_url)

    @pytest.mark.usefixtures("main_page_late")
    @TestData.category(TEST_CATEGORY)
    @TestData.spends(
        SpendAdd(
            amount=108.51,
            description="QA.GURU Python Advanced 1",
            category=TEST_CATEGORY,
            spendDate="2024-08-08T18:39:27.955Z",
            currency="RUB"
        )
    )
    def test_create_spending(self, category, spends):
        spending_page.check_spending_exists(TEST_CATEGORY, 100)

    @Pages.main_page
    def test_empty_category(self):
        spending_page.create_spending(100, 'RUB', '', 'breakfast')
        spending_page.check_category_error_message()

    @Pages.main_page
    @TestData.category(TEST_CATEGORY)
    def test_amount_is_0(self, category):
        spending_page.create_spending(0, 'RUB', f'{TEST_CATEGORY}', 'breakfast')
        spending_page.check_amount_error_message()

    @Pages.main_page
    @TestData.category(TEST_CATEGORY)
    def test_date_in_future(self, category):
        spending_page.create_spending(100, 'RUB', f'{TEST_CATEGORY}', 'breakfast', '2025/12/31')
        spending_page.check_date_error_message()

    @pytest.mark.usefixtures("main_page_late")
    @TestData.category(TEST_CATEGORY)
    @TestData.spends(
        SpendAdd(
            amount=108.51,
            description="QA.GURU Python Advanced 1",
            category=TEST_CATEGORY,
            spendDate="2024-08-08T18:39:27.955Z",
            currency="RUB"
        )
    )
    def test_delete_all_spending(self, category, spends):
        spending_page.check_delete_spending()
