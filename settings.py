from enum import Enum


class Browser(Enum):
    Chrome = 1
    Firefox = 2


BROWSER_VAR = Browser.Chrome
URL_VAR = "https://google.com"
# TODO: replace with 2,3 or 4
WORKERS_CNT = 1
