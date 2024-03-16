import pytest
import os
from time import *
from settings import *


if __name__ == '__main__':
    # Get the current time
    now = strftime("%Y-%m-%d-%H_%M_%S", localtime(time()))
    # Launch pytest
    pytest.main([
        '-v',
        '-n', str(WORKERS_CNT),
        '--alluredir', 'reports/report-{0}'.format(now)
    ])
    # Generate allure report
    os.system('npx allure-commandline generate reports/report-{0}/ -o reports/report-{0}/html'.format(now))
    # Open generated allure report
    if OPEN_REPORT_IMMEDIATELY:
        os.system('npx allure-commandline open reports/report-{0}/html'.format(now))
