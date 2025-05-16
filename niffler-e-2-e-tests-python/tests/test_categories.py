import pytest

from marks import Pages
from pages.profile_page import profiles_page

pytestmark = [pytest.mark.allure_label("Category", label_type="epic")]

class TestCategories:

    @Pages.profile
    def test_add_categories(self, generate_category_name):
        profiles_page.check_adding_category(generate_category_name)
        profiles_page.successful_adding()

    @Pages.profile
    def test_add_same_categories(self):
        category_name = 'school'
        profiles_page.check_adding_category(category_name)
        profiles_page.check_category_error_message()

    @Pages.profile
    def test_empty_name_category(self):
        profiles_page.check_adding_empty_name_category()
