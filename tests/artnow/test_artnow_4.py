from pages.artnow.main_page import MainPage
from pages.artnow.search_page import SearchPage
from pages.artnow.urls import *
import pytest


SEARCH_REQUEST = "Жираф"

#@pytest.mark.skip()
def test_artnow_4(driver):
    """ TEST DESCRIPTION """
    page = MainPage(driver)

    page.search = SEARCH_REQUEST
    page.search_run_button.click()
    page.wait_page_loaded()
    cur_url = page.get_current_url()
    assert cur_url[:cur_url.find('?')] == SEARCH_PAGE_URL

    page = SearchPage(driver, True)

    first_title = page.products_titles.get_text()[0]
    first_title = first_title[first_title.find('.') + 2:].lower()
    assert first_title.find(SEARCH_REQUEST.lower()) != -1
