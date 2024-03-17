from models.base import WebPage
from models.elements import ManyWebElements, WebElement
from tdata.data_artnow import DATA, Url


# Page object: Batic page
class BaticPage(WebPage):
    def __init__(self, web_driver, without_get=False):
        assert DATA.urls.get(Url.Batic) is not None, \
            "Url for batic page wasn't specified"
        super().__init__(web_driver, DATA.urls[Url.Batic], without_get)

    @staticmethod
    def is_current_page(cur_url: str):
        assert DATA.urls.get(Url.Batic) is not None, \
            "Url for batic page wasn't specified"
        return cur_url.startswith(DATA.urls[Url.Batic])

    # Button to go to favorites page
    show_favorites_button = WebElement(
        xpath='//span[contains(@class, "fvtico")]')

    # Titles of products on the page
    products_titles = ManyWebElements(
        xpath=('//div[@itemtype="http://schema.org/Product"]'
               '/a[1]'
               '/div[@itemprop="name"]'))

    # Buttons "Add to favorites" of products on the page
    add_to_favorites_buttons = ManyWebElements(
        xpath=('//div[@itemtype="http://schema.org/Product"]'
               '/div[contains(@class, "heart")]'))
