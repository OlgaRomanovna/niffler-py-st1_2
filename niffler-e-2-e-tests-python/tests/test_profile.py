import pytest
from faker import Faker

from marks import Pages
from pages.profile_page import profiles_page

pytestmark = [pytest.mark.allure_label("Profile", label_type="epic")]


class TestProfile:

    @Pages.profile
    def test_successful_filling_form(self, envs):
        fake = Faker()

        profiles_page.check_filling_form(envs.test_username, fake.last_name())