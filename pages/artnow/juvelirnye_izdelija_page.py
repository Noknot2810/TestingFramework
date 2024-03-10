from models.base import WebPage
from models.elements import ManyWebElements, WebElement
from pages.artnow.urls import *


class JuvelirnyeIzdelijaPage(WebPage):
    def __init__(self, web_driver, without_get=False):
        super().__init__(web_driver, JUVELIRNYE_IZDELIJA_URL, without_get)

    go_basket_button = WebElement(xpath='//button[contains(@class, "ok-button")]')

    products_titles = ManyWebElements(
        xpath='//div[@itemtype="http://schema.org/Product"]/a[1]/div[@itemprop="name"]')

    products_prices = ManyWebElements(
        xpath='//div[@itemtype="http://schema.org/Product"]/div[contains(@class, "price")]')

    products_basket_buttons = ManyWebElements(
        xpath='//div[@itemtype="http://schema.org/Product"]/a/div[contains(@id, "CartButton")]')
