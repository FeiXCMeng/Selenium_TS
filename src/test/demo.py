# import os
# BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
# print(BASE_PATH)
# REPORT_PATH = os.path.join(BASE_PATH, 'utils', 'unittest')
# print(REPORT_PATH)
# import HTMLTestRunner_PY3

import sys
sys.path.append('../')
from utils import name_and_password
from utils.unittest import HTMLTestRunner_PY3