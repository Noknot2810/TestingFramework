import pytest
import allure
from pages.artnow.main_page import MainPage
from pages.artnow.jeweller_art_page import JewellerArtPage
from pages.artnow.shopping_cart_page import ShoppingCartPage
from tdata.data_artnow import DATA


@allure.step("Test 5")
@pytest.mark.skipif(not DATA.use_tests[5]
                    if DATA.use_tests.get(5) is not None
                    else True,
                    reason="Test was disabled during setup")
def test_artnow_5(driver):
    """
    Test #5 [Artnow.ru]
    Steps:
    1) Goes to the main page
    2) Goes to "section" page
    3) Adds to the shopping cart first product on the page
    4) Goes to the shopping cart
    5) Checks there is the product that was added earlier,
       and it has the same price
    """
    var = DATA.vars[5] if DATA.vars.get(5) is not None else {}
    assert var.get("section") is not None

    page = MainPage(driver)

    section_labels = page.sections_refs.get_text()
    if "|{0}|".format("|".join(section_labels)).find(
            "|{0}|".format(var["section"])
    ) == -1:
        page.sections_expand_button.click()
        page.wait_page_loaded()
        section_labels = page.sections_refs.get_text()

    section_ref_used = False
    for i in range(len(section_labels)):
        if section_labels[i] == var["section"]:
            page.sections_refs[i].click()
            page.wait_page_loaded()
            section_ref_used = True
            break

    assert section_ref_used is True
    assert JewellerArtPage.is_current_page(page.get_current_url())
    page = JewellerArtPage(driver, True)

    assert page.products_titles.count() > 0
    chosen_prod_label = page.products_titles.get_text()[0]
    chosen_prod_label = chosen_prod_label[chosen_prod_label.find('.') + 2:]

    assert page.products_prices.count() > 0
    chosen_prod_price = page.products_prices.get_text()[0]

    assert len(chosen_prod_price) != 0
    assert page.add_to_cart_buttons.count() > 0
    chosen_prod_id = (page.add_to_cart_buttons[0]
                      .get_attribute("id")
                      .replace("CartButton", ""))
    page.add_to_cart_buttons[0].click()
    page.wait_page_loaded()

    assert page.go_shopping_cart_page_button.is_presented() is True
    assert page.go_shopping_cart_page_button.is_visible() is True
    page.go_shopping_cart_page_button.click()
    page.wait_page_loaded()

    assert ShoppingCartPage.is_current_page(page.get_current_url())
    page = ShoppingCartPage(driver, True)

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
