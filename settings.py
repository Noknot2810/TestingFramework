from enum import Enum


# Browsers that the framework supports
class Browser(Enum):
    Chrome = 1
    Firefox = 2


# Browser that must be used in tests
BROWSER_VAR = Browser.Chrome
# Count of threads that must be used in tests
WORKERS_CNT = 2
# Flag indicating that the generated allure report must be opened immediately
# after its generation
OPEN_REPORT_IMMEDIATELY = True
# Flag indicating that error screenshots must be additionally
# saved into "error_screenshots" directory
# (not only into allure report)
SAVE_ERROR_SCREENSHOTS = False
