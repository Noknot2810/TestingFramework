from models.base import WebPage
from models.elements import ManyWebElements, WebElement
from tdata.data_artnow import DATA, Url


# Page object: Jeweller art page
class JewellerArtPage(WebPage):
    def __init__(self, web_driver, without_get=False):
        assert DATA.urls.get(Url.JewellerArt) is not None
        super().__init__(web_driver, DATA.urls[Url.JewellerArt], without_get)

    @staticmethod
    def is_current_page(cur_url: str):
        assert DATA.urls.get(Url.JewellerArt) is not None
        return cur_url.startswith(DATA.urls[Url.JewellerArt])

    # Button to go to shopping cart page
    go_shopping_cart_page_button = WebElement(
        xpath='//button[contains(@class, "ok-button")]')

    # Titles of products on the page
    products_titles = ManyWebElements(
        xpath=('//div[@itemtype="http://schema.org/Product"]'
               '/a[1]'
               '/div[@itemprop="name"]'))

    # Prices of products on the page
    products_prices = ManyWebElements(
        xpath=('//div[@itemtype="http://schema.org/Product"]'
               '/div[contains(@class, "price")]'))

    # Buttons "Add to cart" of products on the page
    add_to_cart_buttons = ManyWebElements(
        xpath=('//div[@itemtype="http://schema.org/Product"]'
               '/a'
               '/div[contains(@id, "CartButton")]'))
