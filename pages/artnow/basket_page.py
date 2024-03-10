from models.base import WebPage
from models.elements import ManyWebElements, WebElement
from pages.artnow.urls import *


class BasketPage(WebPage):
    def __init__(self, web_driver, without_get=False):
        super().__init__(web_driver, BASKET_URL, without_get)

    products_titles = ManyWebElements(
        xpath='//div[contains(@id, "cart")]/div[contains(@class, "c_cell")]/div[contains(@class, "c_name")]/a')

    products_prices = ManyWebElements(
        xpath='//div[contains(@id, "cart")]/div[contains(@class, "c_cell")]/div[contains(@class, "shop")]/div[contains(@class, "price")]')

    product_items = ManyWebElements(xpath='//div[contains(@id, "cart")]')

