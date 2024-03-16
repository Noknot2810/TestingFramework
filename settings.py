from enum import Enum


# Browsers that the framework supports
class Browser(Enum):
    Chrome = 1
    Firefox = 2


# Browser that must be used in tests
BROWSER_VAR = Browser.Chrome
# TODO: replace with 2,3 or 4
# Count of threads that must be used in tests
WORKERS_CNT = 1
