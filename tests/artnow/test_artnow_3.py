from pages.artnow.main_page import MainPage
from pages.artnow.batik_page import BatikPage
from pages.artnow.favorites_page import FavoritesPage
from pages.artnow.urls import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytest


SECTION = "Батик"

#@pytest.mark.skip()
def test_artnow_3(driver):
    """ TEST DESCRIPTION """
    page = MainPage(driver)

    section_labels = page.sections_refs.get_text()
    if "|{0}|".format("|".join(section_labels)).find(
            "|{0}|".format(SECTION)
    ) == -1:
        page.sections_expand_button.click()
        page.wait_page_loaded()
        section_labels = page.sections_refs.get_text()

    section_ref_used = False
    for i in range(len(section_labels)):
        if section_labels[i] == SECTION:
            page.sections_refs[i].click()
            section_ref_used = True
            break

    assert section_ref_used is True

    page.wait_page_loaded()
    assert page.get_current_url() == BATIK_KARTINY_URL

    page = BatikPage(driver, True)

    assert page.products_titles.count() > 0

    chosen_prod_label = page.products_titles.get_text()[0]
    chosen_prod_label = chosen_prod_label[chosen_prod_label.find('.') + 2:]

    assert page.products_heart_buttons.count() > 0

    page.products_heart_buttons[0].click()
    page.wait_page_loaded()

    assert page.show_favorites_button.is_presented() is True

    page.show_favorites_button.click()
    page.wait_page_loaded()
    assert page.get_current_url() == FAVORITES_URL

    page = FavoritesPage(driver, True)

    product_found = False
    while True:
        product_found = (
                "|{0}|".format(
                    "|".join(list(map(
                        lambda title: title[title.find('.') + 2:],
                        page.products_titles.get_text()
                    )))
                ).find("|{0}|".format(chosen_prod_label)) != -1
        )
        if product_found is True:
            break
        else:
            if page.next_products_button.is_presented() is True:
                page.next_products_button.click()
            else:
                break

    assert product_found is True
