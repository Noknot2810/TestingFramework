import pytest
from pages.artnow.main_page import MainPage
from pages.artnow.search_page import SearchPage
from tdata.data_artnow import DATA, Url


@pytest.mark.skipif(not DATA.use_tests[4]
                    if DATA.use_tests.get(4) is not None
                    else True,
                    reason="Test was disabled during setup")
def test_artnow_4(driver):
    """
    Test #4 [Artnow.ru]
    Steps:
    1) Goes to the main page
    2) Writes "search_request" in the search field
    3) Clicks the search button
    4) Checks the first product has "search_request" in its name
    """
    var = DATA.vars[4] if DATA.vars.get(4) is not None else {}
    assert var.get("search_request") is not None

    page = MainPage(driver)

    page.search = var["search_request"]
    page.search_run_button.click()
    page.wait_page_loaded()

    assert SearchPage.is_current_page(page.get_current_url())
    page = SearchPage(driver, True)

    first_title = page.products_titles.get_text()[0]
    first_title = first_title[first_title.find('.') + 2:].lower()

    assert first_title.find(var["search_request"].lower()) != -1
