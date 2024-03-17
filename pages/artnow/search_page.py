from models.base import WebPage
from models.elements import ManyWebElements
from tdata.data_artnow import DATA, Url


# Page object: Search results page
class SearchPage(WebPage):
    def __init__(self, web_driver, without_get=False):
        assert DATA.urls.get(Url.SearchPage) is not None, \
            "Url for search page wasn't specified"
        super().__init__(web_driver, DATA.urls.get(Url.SearchPage), without_get)

    @staticmethod
    def is_current_page(cur_url: str):
        assert DATA.urls.get(Url.SearchPage) is not None, \
            "Url for search page wasn't specified"
        return cur_url.startswith(DATA.urls.get(Url.SearchPage))

    # Titles of products on the page
    products_titles = ManyWebElements(
        xpath=('//div[@itemtype="http://schema.org/Product"]'
               '/a[1]'
               '/div[@itemprop="name"]'))
