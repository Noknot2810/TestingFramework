from models.base import WebPage
from models.elements import ManyWebElements, WebElement
from pages.artnow.urls import *


class VyshityeKartinyPage(WebPage):
    def __init__(self, web_driver, without_get=False):
        super().__init__(web_driver, VYSHITYE_KARTINY_URL, without_get)

    show_genres_button = WebElement(xpath='//div[contains(@class, "onefilter")]/span[@data-show="genrebox"]')

    genres_expand_button = WebElement(xpath='//div[@id="genrebox"]/span[@data-show="genrebox"]')

    #
    genres_refs = ManyWebElements(xpath='//div[@id="genrebox"]/div/label')

    products_titles = ManyWebElements(
        xpath='//div[@itemtype="http://schema.org/Product"]/a[1]/div[@itemprop="name"]')
