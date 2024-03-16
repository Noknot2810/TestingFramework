from models.base import WebPage
from models.elements import ManyWebElements
from tdata.data_artnow import DATA, Url


# Page object: Shopping cart page
class ShoppingCartPage(WebPage):
    def __init__(self, web_driver, without_get=False):
        assert DATA.urls.get(Url.ShoppingCart) is not None
        super().__init__(web_driver, DATA.urls[Url.ShoppingCart], without_get)

    @staticmethod
    def is_current_page(cur_url: str):
        assert DATA.urls.get(Url.ShoppingCart) is not None
        return cur_url.startswith(DATA.urls[Url.ShoppingCart])

    # Titles of products on the page
    products_titles = ManyWebElements(
        xpath=('//div[contains(@id, "cart")]'
               '/div[contains(@class, "c_cell")]'
               '/div[contains(@class, "c_name")]'
               '/a'))

    # Prices of products on the page
    products_prices = ManyWebElements(
        xpath=('//div[contains(@id, "cart")]'
               '/div[contains(@class, "c_cell")]'
               '/div[contains(@class, "shop")]'
               '/div[contains(@class, "price")]'))

    # Div containers of products on the page
    product_items = ManyWebElements(xpath='//div[contains(@id, "cart")]')

