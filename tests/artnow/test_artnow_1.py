import pytest
from pages.artnow.main_page import MainPage
from pages.artnow.embroidered_paintings_page import EmbroideredPaintingsPage
from pages.artnow.gallery_page import GalleryPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from tdata.data_artnow import DATA, Url


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
    var = DATA.vars[1] if DATA.vars.get(1) is not None else {}
    assert var.get("section") is not None
    assert var.get("genre") is not None
    assert var.get("product_name") is not None
    
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
    assert EmbroideredPaintingsPage.is_current_page(page.get_current_url())
    page = EmbroideredPaintingsPage(driver, True)

    if page.genres_expand_button.is_visible() is False:
        page.show_genres_button.click()
        page.wait_page_loaded()

    genres_labels = page.genres_refs.get_text()
    if "|{0}|".format("|".join(genres_labels)).find(
            "|{0}|".format(var["genre"])
    ) == -1:
        page.genres_expand_button.click()
        page.wait_page_loaded()
        genres_labels = page.genres_refs.get_text()

    genre_checked = False
    for i in range(len(genres_labels)):
        if genres_labels[i] == var["genre"]:
            page.genres_refs[i].click()
            genre_checked = True
            break

    assert genre_checked is True
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    page.wait_page_loaded()

    assert GalleryPage.is_current_page(page.get_current_url())
    page = GalleryPage(driver, True)

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

    assert product_found is True
