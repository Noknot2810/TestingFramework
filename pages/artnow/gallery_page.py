from models.base import WebPage
from models.elements import ManyWebElements, WebElement
from pages.artnow.urls import *


class GalleryPage(WebPage):
    def __init__(self, web_driver, without_get=False):
        super().__init__(web_driver, GALLERY_URL, without_get)

    products_titles = ManyWebElements(
        xpath='//div[@itemtype="http://schema.org/Product"]/a[1]/div[@itemprop="name"]')

    next_products_button = WebElement(xpath='//div[contains(@class, "pagelmt")]/*[contains(text(), "»")]')

    product_style = WebElement(xpath='//div[contains(@class, "infocontainer")]/div/*[contains(text(), "Стиль")]/following-sibling::*')
