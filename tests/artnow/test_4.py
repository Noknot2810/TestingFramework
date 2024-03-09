from pages.artnow.main_page import MainPage
from pages.artnow.search_page import SearchPage
from pages.artnow.urls import *


SEARCH_REQUEST = "Жираф"

def test_check_main_search(driver):
    """ Make sure main search works fine. """

    page = MainPage(driver)

    page.search = SEARCH_REQUEST
    page.search_run_button.click()

    cur_url = page.get_current_url()
    assert cur_url[:cur_url.find('?')] == SEARCH_PAGE_URL

    page = SearchPage(driver, True)

    all_titles = page.products_titles.get_text()
    assert all_titles[0].find(SEARCH_REQUEST) != -1