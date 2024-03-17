import pytest
import allure
from pages.artnow.main_page import MainPage
from pages.artnow.search_page import SearchPage
from tdata.data_artnow import DATA


@allure.epic("Web interface")
@allure.feature("Search field")
@allure.story("Correct first product name in search response")
@pytest.mark.skipif(not DATA.use_tests[4]
                    if DATA.use_tests.get(4) is not None
                    else True,
                    reason="Test was disabled during setup")
def test_artnow_4(driver):
    """
    Test #4 [Artnow.ru]
    Steps:
    1) Goes to the main page
    2) Writes 'search_request' in the search field
    3) Clicks the search button
    4) Checks the first product has 'search_request' in its name
    """
    with allure.step("Get all test variables"):
        var = DATA.vars[4] if DATA.vars.get(4) is not None else {}
        with allure.step("Get variable 'search_request'"):
            assert var.get("search_request") is not None, \
                "Variable 'search_request' wasn't specified"
            allure.dynamic.parameter(
                "search_request",
                var.get("search_request"))

    with allure.step("Go to the main page"):
        page = MainPage(driver)

    with allure.step("Search product by 'search_request'"):
        page.search = var["search_request"]
        page.search_run_button.click()
        page.wait_page_loaded()

    with allure.step("Check if there is the search page on the screen"):
        assert SearchPage.is_current_page(page.get_current_url()), \
            "There isn't a search page"
        page = SearchPage(driver, True)

    with allure.step("Get the first product title"):
        first_title = page.products_titles.get_text()[0]
        first_title = first_title[first_title.find('.') + 2:].lower()

    with allure.step(("Check the first product title has "
                      "'search_request' in its name")):
        assert first_title.find(var["search_request"].lower()) != -1, \
            "The first product title doesn't has 'search_request' in its name"
