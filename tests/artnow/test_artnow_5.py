import pytest
import allure
from pages.artnow.main_page import MainPage
from pages.artnow.shopping_cart_page import ShoppingCartPage
from pages.artnow.utils import get_section_page_class
from tdata.data_artnow import DATA


@allure.epic("Web interface")
@allure.feature("Shopping cart")
@allure.story("First product from specified section")
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
    with allure.step("Get all test variables"):
        var = DATA.vars[5] if DATA.vars.get(5) is not None else {}
        with allure.step("Get variable 'section'"):
            assert var.get("section") is not None, \
                "Variable 'section' wasn't specified"
            allure.dynamic.parameter(
                "section",
                var.get("section"))

    with allure.step("Go to the main page"):
        page = MainPage(driver)

    with allure.step("Get section labels"):
        section_labels = page.sections_refs.get_text()

    with allure.step("Check if there is a need to expand hidden sections"):
        if "|{0}|".format("|".join(section_labels)).find(
                "|{0}|".format(var["section"])
        ) == -1:
            with allure.step("Expand hidden sections"):
                page.sections_expand_button.click()
                page.wait_page_loaded()
                section_labels = page.sections_refs.get_text()

    with allure.step("Try to find and open 'section'"):
        section_ref_used = False
        for i in range(len(section_labels)):
            if section_labels[i] == var["section"]:
                page.sections_refs[i].click()
                page.wait_page_loaded()
                section_ref_used = True
                break

        assert section_ref_used is True, \
            f"Section with name {var["section"]} wasn't found"

    with allure.step("Check if there is the 'section' page on the screen"):
        page_class = get_section_page_class(var["section"])
        assert page_class.is_current_page(page.get_current_url()), \
            f"There isn't the {var["section"]} page"
        page = page_class(driver, True)

    with allure.step("Get the first product"):
        assert page.products_titles.count() > 0, \
            "There is no products on the page"
        chosen_prod_label = page.products_titles.get_text()[0]
        chosen_prod_label = chosen_prod_label[chosen_prod_label.find('.') + 2:]

        assert page.products_prices.count() > 0, \
            "There is no products prices on the page"
        chosen_prod_price = page.products_prices.get_text()[0]

        assert len(chosen_prod_price) != 0, \
            "The first product hasn't any price"

    with allure.step("Add the product to shopping cart"):
        assert page.add_to_cart_buttons.count() > 0, \
            "There is no 'add to cart' buttons on the page"
        chosen_prod_id = (page.add_to_cart_buttons[0]
                          .get_attribute("id")
                          .replace("CartButton", ""))
        page.add_to_cart_buttons[0].click()
        page.wait_page_loaded()

    with allure.step("Go to shopping cart"):
        page.go_shopping_cart_page_button.click()
        page.wait_page_loaded()

    with allure.step("Check if there is the shopping cart page on the screen"):
        assert ShoppingCartPage.is_current_page(page.get_current_url()), \
            "There isn't a shopping cart page"
        page = ShoppingCartPage(driver, True)

    with allure.step("Try to find here the product that was added earlier"):
        assert page.product_items.count() > 0, \
            "There is no products on the page"
        product_items_ids = list(map(
            lambda sid: sid.replace("cart", ""),
            page.product_items.get_attribute("id")
        ))

        assert page.products_titles.count() > 0, \
            "There is no products titles on the page"
        assert page.products_prices.count() > 0, \
            "There is no products prices on the page"
        product_item_found = False
        for i in range(len(product_items_ids)):
            if product_items_ids[i] == chosen_prod_id:
                assert page.products_titles.get_text()[i] == chosen_prod_label, \
                    "The product title was changed"
                assert page.products_prices.get_text()[i] == chosen_prod_price, \
                    "The product price was changed"
                product_item_found = True

        assert product_item_found is True, \
            ("The product that was added to shopping cart "
             "wasn't found on the page")
