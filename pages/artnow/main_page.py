from models.base import WebPage
from models.elements import ManyWebElements, WebElement
from tdata.data_artnow import DATA, Url


# Page object: Main page
class MainPage(WebPage):

    def __init__(self, web_driver, without_get=False):
        assert DATA.urls.get(Url.MainPage) is not None, \
            "Url for main page wasn't specified"
        super().__init__(web_driver, DATA.urls[Url.MainPage], without_get)

    @staticmethod
    def is_current_page(cur_url: str):
        assert DATA.urls.get(Url.MainPage) is not None, \
            "Url for main page wasn't specified"
        return cur_url.startswith(DATA.urls[Url.MainPage])

    # Search field
    search = WebElement(xpath='//input[@name="qs"]')

    # Search button
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # Button to expand hidden sections
    sections_expand_button = WebElement(
        xpath=('//div[contains(@class, "main_menu")]'
               '/ul[2]'
               '/li[@data-show="gids"]'))

    # Sections references
    sections_refs = ManyWebElements(
        xpath=('//div[contains(@class, "main_menu")]'
               '/ul[2]'
               '/li'))
