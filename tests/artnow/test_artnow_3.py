import pytest
import allure
from pages.artnow.main_page import MainPage
from pages.artnow.batic_page import BaticPage
from pages.artnow.favorites_page import FavoritesPage
from tdata.data_artnow import DATA


@allure.step("Test 3")
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
    var = DATA.vars[3] if DATA.vars.get(3) is not None else {}
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
    assert BaticPage.is_current_page(page.get_current_url())
    page = BaticPage(driver, True)

    assert page.products_titles.count() > 0
    chosen_prod_label = page.products_titles.get_text()[0]
    chosen_prod_label = chosen_prod_label[chosen_prod_label.find('.') + 2:]

    assert page.add_to_favorites_buttons.count() > 0
    page.add_to_favorites_buttons[0].click()
    page.wait_page_loaded()

    assert page.show_favorites_button.is_presented() is True
    page.show_favorites_button.click()
    page.wait_page_loaded()

    assert FavoritesPage.is_current_page(page.get_current_url())
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
