import os

import pytest

from marks import Pages, TestData
from models.category import CategoryAdd
from models.enum import Information, Categories
from pages.spending_page import spending_page
from utils.assertion import check_category_in_db, check_category_name_in_db, check_spend_in_db
from faker import Faker
from pages.profile_page import profiles_page

pytestmark = [pytest.mark.allure_label("Category DB", label_type="epic")]

fake = Faker()
name = fake.name()

TEST_CATEGORY = "school"

class TestCategoryDb:

    @Pages.profile
    @TestData.category_db(CategoryAdd(
        name=f"Test category name {name}"
    ))
    def test_edit_name_category(self, category_db, spend_db) -> None:
        check_category_in_db(
            spend_db,
            category_db.id,
            category_db.name,
            category_db.username,
            category_db.archived)

        old_name = category_db.name
        new_name = f"{category_db.name} junior"

        profiles_page.edit_category_name(old_name, new_name)
        profiles_page.should_be_category_name(new_name)


    @Pages.profile
    @TestData.category_db(CategoryAdd(
        name=f"Test category name {name}"
    ))
    def test_archived_category(self, category_db, spend_db) -> None:
        check_category_in_db(
            spend_db,
            category_db.id,
            category_db.name,
            category_db.username,
            category_db.archived)

        profiles_page.archive_category(category_db.name)
        profiles_page.check_archived_category(category_db.name)

    @Pages.main_page
    def test_created_spend_exist_in_database(self, spend_db):
        user_name = os.getenv("USER_NAME")
        spending_page.create_spending(Information.AMOUNT, 'RUB', TEST_CATEGORY, Information.DESCRIPTION)
        check_spend_in_db(spend_db, Information.AMOUNT, TEST_CATEGORY, Information.DESCRIPTION, user_name)
        profiles_page.delete_spend(TEST_CATEGORY)


    @Pages.profile
    def test_check_category_name_changes_in_database(self, spend_db):
        user_name = os.getenv("USER_NAME")
        profiles_page.check_adding_category(Categories.TEST_CATEGORY2)
        profiles_page.refresh_page()
        check_category_name_in_db(spend_db, user_name, Categories.TEST_CATEGORY2)