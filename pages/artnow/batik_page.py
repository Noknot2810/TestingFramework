from models.base import WebPage
from models.elements import ManyWebElements, WebElement
from pages.artnow.urls import *


class BatikPage(WebPage):
    def __init__(self, web_driver, without_get=False):
        super().__init__(web_driver, BATIK_KARTINY_URL, without_get)

    show_favorites_button = WebElement(xpath='//span[contains(@class, "fvtico")]')

    products_titles = ManyWebElements(
        xpath='//div[@itemtype="http://schema.org/Product"]/a[1]/div[@itemprop="name"]')

    products_heart_buttons = ManyWebElements(
        xpath='//div[@itemtype="http://schema.org/Product"]/div[contains(@class, "heart")]')
