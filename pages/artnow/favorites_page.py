from models.base import WebPage
from models.elements import ManyWebElements, WebElement
from tdata.data_artnow import DATA, Url


# Page object: Favorites page
class FavoritesPage(WebPage):
    def __init__(self, web_driver, without_get=False):
        assert DATA.urls.get(Url.Favorites) is not None, \
            "Url for favorites page wasn't specified"
        super().__init__(web_driver, DATA.urls[Url.Favorites], without_get)

    @staticmethod
    def is_current_page(cur_url: str):
        assert DATA.urls.get(Url.Favorites) is not None, \
            "Url for favorites page wasn't specified"
        return cur_url.startswith(DATA.urls[Url.Favorites])

    # Titles of products on the page
    products_titles = ManyWebElements(
        xpath=('//div[@id="sa_container"]'
               '/div[contains(@class, "post")]'
               '/a[1]'
               '/div'))

    # Button to get a next set of products
    next_products_button = WebElement(
        xpath=('//div[contains(@class, "pagelmt")]'
               '/*[contains(text(), "»")]'))
