# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../')
from HTMLTestRunner_PY3 import HTMLTestRunner
from test_unittest import TestMathFunc

if __name__ == '__main__':
	report = './report/report.html'
	suite = unittest.TestSuite()

	tests = [TestMathFunc('test_minus'), TestMathFunc('test_add')]
	suite.addTests(tests)

	# runner = unittest.TextTestRunner(verbosity=3)
	with open(report, 'wb')as f:
		runner = HTMLTestRunner(stream=f,
								title='数学计算方法的测试',
								description='执行人：FeiXCMeng',
								verbosity=2
								)

		runner.run(suite)
