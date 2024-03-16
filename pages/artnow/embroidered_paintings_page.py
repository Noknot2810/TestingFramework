from models.base import WebPage
from models.elements import ManyWebElements, WebElement
from tdata.data_artnow import DATA, Url


# Page object: Art embroidered paintings page
class EmbroideredPaintingsPage(WebPage):
    def __init__(self, web_driver, without_get=False):
        assert DATA.urls.get(Url.EmbroideredPaintings) is not None
        super().__init__(
            web_driver,
            DATA.urls[Url.EmbroideredPaintings],
            without_get)

    @staticmethod
    def is_current_page(cur_url: str):
        assert DATA.urls.get(Url.EmbroideredPaintings) is not None
        return cur_url.startswith(DATA.urls[Url.EmbroideredPaintings])

    # Button to show/hide all genres
    show_genres_button = WebElement(
        xpath=('//div[contains(@class, "onefilter")]'
               '/span[@data-show="genrebox"]'))

    # Button to expand hidden genres
    genres_expand_button = WebElement(
        xpath=('//div[@id="genrebox"]'
               '/span[@data-show="genrebox"]'))

    # Genre references
    genres_refs = ManyWebElements(xpath='//div[@id="genrebox"]/div/label')

    # Titles of products on the page
    products_titles = ManyWebElements(
        xpath=('//div[@itemtype="http://schema.org/Product"]'
               '/a[1]'
               '/div[@itemprop="name"]'))
