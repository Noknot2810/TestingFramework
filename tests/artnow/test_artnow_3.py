import pytest
import allure
from pages.artnow.main_page import MainPage
from pages.artnow.favorites_page import FavoritesPage
from pages.artnow.utils import get_section_page_class
from tdata.data_artnow import DATA


@allure.epic("Web interface")
@allure.feature("Favorites")
@allure.story("First product from specified section")
@pytest.mark.skipif(not DATA.use_tests[3]
                    if DATA.use_tests.get(3) is not None
                    else True,
                    reason="Test was disabled during setup")
def test_artnow_3(driver):
    """
    Test #3 [Artnow.ru]
    Steps:
    1) Goes to the main page
    2) Goes to "section" page
    3) Adds to favorites first product on the page
    4) Goes to favorites
    5) Checks there is the product that was added earlier
    """
    with allure.step("Get all test variables"):
        var = DATA.vars[3] if DATA.vars.get(3) is not None else {}
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

    with allure.step("Add the product to favorites"):
        assert page.add_to_favorites_buttons.count() > 0, \
            "There is no 'add to favorite' buttons on the page"
        page.add_to_favorites_buttons[0].click()
        page.wait_page_loaded()

    with allure.step("Go to favorites"):
        page.show_favorites_button.click()
        page.wait_page_loaded()

    with allure.step("Check if there is the favorites page on the screen"):
        assert FavoritesPage.is_current_page(page.get_current_url()), \
            "There isn't a favorites page"
        page = FavoritesPage(driver, True)

    with allure.step("Try to find here the product that was added earlier"):
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

        assert product_found is True, \
            f"The product that was added to favorites wasn't found on the page"
