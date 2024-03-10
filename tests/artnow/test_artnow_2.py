from pages.artnow.main_page import MainPage
from pages.artnow.vyshitye_kartiny_page import VyshityeKartinyPage
from pages.artnow.gallery_page import GalleryPage
from pages.artnow.urls import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pytest


SECTION = "Вышитые картины"
GENRE = "Городской пейзаж"
PRODUCT_NAME = "Трамвайный путь"
STYLE = "Реализм"

#@pytest.mark.skip()
def test_artnow_2(driver):
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
    assert page.get_current_url() == VYSHITYE_KARTINY_URL

    page = VyshityeKartinyPage(driver, True)

    if page.genres_expand_button.is_visible() is False:
        page.show_genres_button.click()
        page.wait_page_loaded()

    genres_labels = page.genres_refs.get_text()
    if "|{0}|".format("|".join(genres_labels)).find(
            "|{0}|".format(GENRE)
    ) == -1:
        page.genres_expand_button.click()
        page.wait_page_loaded()
        genres_labels = page.genres_refs.get_text()

    genre_checked = False
    for i in range(len(genres_labels)):
        if genres_labels[i] == GENRE:
            page.genres_refs[i].click()
            genre_checked = True
            break

    assert genre_checked is True

    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    page.wait_page_loaded()
    assert page.get_current_url().startswith(GALLERY_URL) is True

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
                ).find("|{0}|".format(PRODUCT_NAME)) != -1
        )
        if product_found is True:
            break
        else:
            if page.next_products_button.is_presented() is True:
                page.next_products_button.click()
            else:
                break

    assert product_found is True

    product_chosen = False
    for i in range(len(products_labels)):
        if products_labels[i][products_labels[i].find('.') + 2:] == PRODUCT_NAME:
            page.products_titles[i].click()
            product_chosen = True
            break

    assert product_chosen is True

    page.wait_page_loaded()
    assert page.product_style.is_presented() is True
    assert page.product_style.get_text() == STYLE
