import pytest


class Pages:
    main_page = pytest.mark.usefixtures("main_page")
    profile = pytest.mark.usefixtures("profile_page")
    delete_spend = lambda name_category: pytest.mark.parametrize("delete_spend", [name_category], indirect=True)


class TestData:
    category = lambda x: pytest.mark.parametrize("category", [x], indirect=True)
    spends = lambda x: pytest.mark.parametrize("spends", [x], indirect=True, ids=lambda param: param.description)
    category_db = lambda x: pytest.mark.parametrize("category_db", [x], indirect=True, ids=lambda param: param.name)

