import os
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
print(BASE_PATH)
REPORT_PATH = os.path.join(BASE_PATH, 'utils', 'unittest', 'report')
print(REPORT_PATH)