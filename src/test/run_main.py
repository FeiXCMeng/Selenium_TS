# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../')
from utils.unittest.HTMLTestRunner_PY3 import HTMLTestRunner
from test_main import TestMain



# if __name__ == '__main__':
# 	report = '../utils/unittest/report/report.html'
# 	# unittest.main()
# 	suite = unittest.TestSuite()
# 	tests = [TestMain('test_create_net'), 
# 			TestMain('test_message'), 
# 			TestMain('test_judge_message'), 
# 			TestMain('test_judge_message2'),
# 			TestMain('test_inherit_column'),
# 			TestMain('test_manage_user'),
# 			TestMain('upload_photo')
# 			]
# 	suite.addTests(tests)

# 	with open(report, 'wb') as f:
# 		runner = HTMLTestRunner(stream=f,
# 								title=u'JCMS-UI自动化测试',
# 								description='FeiXCMeng',
# 								verbosity=2
# 								)
# 		runner.run(suite)