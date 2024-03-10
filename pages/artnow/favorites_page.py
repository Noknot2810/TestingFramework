from models.base import WebPage
from models.elements import ManyWebElements, WebElement
from pages.artnow.urls import *


class FavoritesPage(WebPage):
    def __init__(self, web_driver, without_get=False):
        super().__init__(web_driver, FAVORITES_URL, without_get)

    products_titles = ManyWebElements(
        xpath='//div[@id="sa_container"]/div[contains(@class, "post")]/a[1]/div')

    next_products_button = WebElement(xpath='//div[contains(@class, "pagelmt")]/*[contains(text(), "»")]')
