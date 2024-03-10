from models.base import WebPage
from models.elements import ManyWebElements, WebElement
from pages.artnow.urls import *


class MainPage(WebPage):

    def __init__(self, web_driver, without_get=False):
        super().__init__(web_driver, MAIN_PAGE_URL, without_get)

    # Main search field
    search = WebElement(xpath='//input[@name="qs"]')

    # Search button
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    #main_menu = WebElement(xpath='//div[contains(@class, "main_menu")]/ul[2]/li[@data-show="gids"]')
    #
    sections_expand_button = WebElement(xpath='//div[contains(@class, "main_menu")]/ul[2]/li[@data-show="gids"]')

    #
    sections_refs = ManyWebElements(xpath='//div[contains(@class, "main_menu")]/ul[2]/li')

    # Titles of the products in search results
    #products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Button to sort products by price
    #sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Prices of the products in search results
    #products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')