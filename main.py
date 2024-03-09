import pytest
import os
from time import *
from settings import *


if __name__ == '__main__':
    # Get the current time
    now = strftime("%Y-%m-%d-%H_%M_%S", localtime(time()))
    pytest.main(['-v', '-n', str(WORKERS_CNT)])
    #os.system('allure generate report-{0}/ -o report-{0}/html'.format(now))

