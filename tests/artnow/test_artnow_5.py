from pages.artnow.main_page import MainPage
from pages.artnow.juvelirnye_izdelija_page import JuvelirnyeIzdelijaPage
from pages.artnow.basket_page import BasketPage
from pages.artnow.urls import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytest


SECTION = "Ювелирное искусство"

#@pytest.mark.skip()
def test_artnow_5(driver):
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
    assert page.get_current_url() == JUVELIRNYE_IZDELIJA_URL

    page = JuvelirnyeIzdelijaPage(driver, True)

    assert page.products_titles.count() > 0

    chosen_prod_label = page.products_titles.get_text()[0]
    chosen_prod_label = chosen_prod_label[chosen_prod_label.find('.') + 2:]

    assert page.products_prices.count() > 0

    chosen_prod_price = page.products_prices.get_text()[0]
    assert len(chosen_prod_price) != 0

    assert page.products_basket_buttons.count() > 0

    chosen_prod_id = (page.products_basket_buttons[0]
                      .get_attribute("id")
                      .replace("CartButton", ""))
    page.products_basket_buttons[0].click()
    page.wait_page_loaded()

    assert page.go_basket_button.is_presented() is True
    assert page.go_basket_button.is_visible() is True

    page.go_basket_button.click()
    page.wait_page_loaded()
    assert page.get_current_url().startswith(BASKET_URL) is True

    page = BasketPage(driver, True)

    assert page.product_items.count() > 0
    product_items_ids = list(map(
        lambda sid: sid.replace("cart", ""),
        page.product_items.get_attribute("id")
    ))

    assert page.products_titles.count() > 0
    assert page.products_prices.count() > 0
    product_item_found = False
    for i in range(len(product_items_ids)):
        if product_items_ids[i] == chosen_prod_id:
            assert page.products_titles.get_text()[i] == chosen_prod_label
            assert page.products_prices.get_text()[i] == chosen_prod_price
            product_item_found = True

    assert product_item_found is True
