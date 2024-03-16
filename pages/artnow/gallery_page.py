from models.base import WebPage
from models.elements import ManyWebElements, WebElement
from tdata.data_artnow import DATA, Url


# Page object: Gallery page
class GalleryPage(WebPage):
    def __init__(self, web_driver, without_get=False):
        assert DATA.urls.get(Url.Gallery) is not None
        super().__init__(web_driver, DATA.urls[Url.Gallery], without_get)

    @staticmethod
    def is_current_page(cur_url: str):
        assert DATA.urls.get(Url.Gallery) is not None
        return cur_url.startswith(DATA.urls[Url.Gallery])

    # Titles of products on the page
    products_titles = ManyWebElements(
        xpath=('//div[@itemtype="http://schema.org/Product"]'
               '/a[1]'
               '/div[@itemprop="name"]'))

    # Button to get a next set of products
    next_products_button = WebElement(
        xpath=('//div[contains(@class, "pagelmt")]'
               '/*[contains(text(), "»")]'))

    # Style of a specific product on the page
    product_style = WebElement(
        xpath=('//div[contains(@class, "infocontainer")]'
               '/div'
               '/*[contains(text(), "Стиль")]'
               '/following-sibling::*'))
