import pytest
import allure
from pages.artnow.main_page import MainPage
from pages.artnow.embroidered_paintings_page import EmbroideredPaintingsPage
from pages.artnow.gallery_page import GalleryPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from tdata.data_artnow import DATA


@allure.epic("Web interface")
@allure.feature("Product placement")
@allure.story("Product with specified section, genre and name")
@pytest.mark.skipif(not DATA.use_tests[1]  
                    if DATA.use_tests.get(1) is not None 
                    else True,
                    reason="Test was disabled during setup")
def test_artnow_1(driver):
    """
    Test #1 [Artnow.ru]
    Steps:
    1) Goes to the main page
    2) Goes to "section" page
    3) Chooses "genre"
    4) Checks there is the product named "product_name"
    """
    with allure.step("Get all test variables"):
        var = DATA.vars[1] if DATA.vars.get(1) is not None else {}
        with allure.step("Get variable 'section'"):
            assert var.get("section") is not None, \
                "Variable 'section' wasn't specified"
            allure.dynamic.parameter(
                "section",
                var.get("section"))
        with allure.step("Get variable 'genre'"):
            assert var.get("genre") is not None, \
                "Variable 'genre' wasn't specified"
            allure.dynamic.parameter(
                "genre",
                var.get("genre"))
        with allure.step("Get variable 'product_name'"):
            assert var.get("product_name") is not None, \
                "Variable 'product_name' wasn't specified"
            allure.dynamic.parameter(
                "product_name",
                var.get("product_name"))

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
        assert EmbroideredPaintingsPage.is_current_page(page.get_current_url()), \
            f"There isn't the {var["section"]} page"
        page = EmbroideredPaintingsPage(driver, True)

    with allure.step("Check if there is a need to expand all genres"):
        if page.genres_expand_button.is_visible() is False:
            with allure.step("Expand all genres"):
                page.show_genres_button.click()
                page.wait_page_loaded()

    with allure.step("Check if there is a need to expand hidden genres"):
        genres_labels = page.genres_refs.get_text()
        if "|{0}|".format("|".join(genres_labels)).find(
                "|{0}|".format(var["genre"])
        ) == -1:
            with allure.step("Expand hidden genres"):
                page.genres_expand_button.click()
                page.wait_page_loaded()
                genres_labels = page.genres_refs.get_text()

    with allure.step("Try to find and choose 'genre'"):
        genre_checked = False
        for i in range(len(genres_labels)):
            if genres_labels[i] == var["genre"]:
                page.genres_refs[i].click()
                genre_checked = True
                break

        assert genre_checked is True, \
            f"Genre with name {var["genre"]} wasn't found"
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        page.wait_page_loaded()

    with allure.step("Check if there is the gallery page on the screen"):
        assert GalleryPage.is_current_page(page.get_current_url()), \
            "There isn't a gallery page"
        page = GalleryPage(driver, True)

    with allure.step("Try to find product with name 'product_name'"):
        product_found = False
        while True:
            product_found = (
                "|{0}|".format(
                    "|".join(list(map(
                        lambda title: title[title.find('.') + 2:],
                        page.products_titles.get_text()
                    )))
                ).find("|{0}|".format(var["product_name"])) != -1
            )
            if product_found is True:
                break
            else:
                if page.next_products_button.is_presented() is True:
                    page.next_products_button.click()
                else:
                    break

        assert product_found is True, \
            f"Product with name {var["product_name"]} wasn't found"
