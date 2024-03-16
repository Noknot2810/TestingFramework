import pytest
from pages.artnow.main_page import MainPage
from pages.artnow.embroidered_paintings_page import EmbroideredPaintingsPage
from pages.artnow.gallery_page import GalleryPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from tdata.data_artnow import DATA, Url


@pytest.mark.skipif(not DATA.use_tests[2]
                    if DATA.use_tests.get(2) is not None
                    else True,
                    reason="Test was disabled during setup")
def test_artnow_2(driver):
    """
    Test #2 [Artnow.ru]
    Steps:
    1) Goes to the main page
    2) Goes to "section" page
    3) Chooses "genre"
    4) Finds a product named "product_name"
    5) Goes to the product page
    6) Checks that the product style is "style"
    """
    var = DATA.vars[2] if DATA.vars.get(2) is not None else {}
    assert var.get("section") is not None
    assert var.get("genre") is not None
    assert var.get("product_name") is not None
    assert var.get("style") is not None

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

    products_labels = []
    product_found = False
    while True:
        products_labels = page.products_titles.get_text()
        product_found = (
                "|{0}|".format(
                    "|".join(list(map(
                        lambda label: label[label.find('.') + 2:],
                        products_labels
                    )))
                ).find("|{0}|".format(var["product_name"])) != -1
        )
        if product_found is True:
            break
        else:
            if page.next_products_button.is_presented() is True:
                page.next_products_button.click()
                page.wait_page_loaded()
            else:
                break

    assert product_found is True
    product_chosen = False
    for i in range(len(products_labels)):
        if (products_labels[i][products_labels[i].find('.') + 2:] ==
                var["product_name"]):
            page.products_titles[i].click()
            page.wait_page_loaded()
            product_chosen = True
            break

    assert product_chosen is True
    assert page.product_style.is_presented() is True
    assert page.product_style.get_text() == var["style"]
