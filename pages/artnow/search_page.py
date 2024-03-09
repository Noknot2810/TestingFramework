from models.base import WebPage
from models.elements import ManyWebElements
from pages.artnow.urls import *


class SearchPage(WebPage):
    def __init__(self, web_driver, without_get=False):
        super().__init__(web_driver, SEARCH_PAGE_URL, without_get)

    products_titles = ManyWebElements(
        xpath='//div[@itemtype="http://schema.org/Product"]/a[1]/div[@itemprop="name"]')
