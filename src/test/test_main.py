import sys
sys.path.append('../')
from utils import *
from utils.unittest.HTMLTestRunner_PY3 import HTMLTestRunner
from utils.mylogger import *
from createNet import *
from public import *
from setAuditUser import *
from auditArticle import *
from columnInherit import *
from manage_organization import *
from set_photoAndAttachmengt import *
from changeWebsite import *
import unittest

# root = mylogger.log_to_RotatingFile(os.path.join('.\\runlog.txt'))

class TestMain(unittest.TestCase):
	def __init__(self, website_mail=websiteName()):
		self.website_mail= website_mail
		# self.logger = root

	def setUp(self):
		# self.logger.info("************************setup***************************")
		get_url()

	def tearDown(self):
		dr.quit()
		# self.logger.info("************************quit*****************************")

	def test_create_net(self, website_mail):
		# setUp()
		login('wy', 'hanweb1')
		# website_mail = self.websiteName()

#新建网站、模板、信息
		createWebsite(website_mail)
		create_audit_column()
		createMessage()
		importIndexTemplate()
		importColumnTemplate()
		importArticleTemplate()
		createIndexTempate()
		createArticleTemplate()
		createColumnTemplate()
		setColumnTemplate()
		setArticleTemplate()
		setTitleTemplate()
		release()
		logout()

	def test_message(website_mail):
		login('wy', 'hanweb1')
		change_website(website_mail)
		set_audit_user()
		sleep(1)
		create_audit_message()

#信息审核通过
	def test_judge_message(website_mail):
		login('test', 'hanweb1')
		change_website(website_mail)
		auditArticle()
		login('gy', 'hanweb1')
		change_website(website_mail)
		auditArticle()
		sleep(1)
		login('test', 'hanweb1')
		first_judge()

#信息审核不通过
	def test_judge_message2(website_mail):
		login('wy', 'hanweb1')
		change_website(website_mail)
		create_audit_message()
		login('test', 'hanweb1')
		auditArticle(1)
		login('test', 'hanweb1')
		first_judge()

#栏目继承
	def test_inherit_column():
		create_columnA('wy', 'hanweb1')
		set_attributes()
		create_columnB()
		logout()


#机构用户管理
	def test_manage_user(website_mail):
		login('wy', 'hanweb1')
		change_website(website_mail)
		create_role(website_mail)
		create_organization_user(website_mail)
		logout()

#图片附件上传
	def upload_photo():
		login('wy', 'hanweb1')
		createCategory()
		upload_photo_attachment()
		create_message()
		tearDown()

if __name__ == '__main__':
	# report = '../utils/unittest/report/report.html'
	# # unittest.main()
	# suite = unittest.TestSuite()
	# tests = [TestMain('test_create_net'), 
	# 		TestMain('test_message'), 
	# 		TestMain('test_judge_message'), 
	# 		TestMain('test_judge_message2'),
	# 		TestMain('test_inherit_column'),
	# 		TestMain('test_manage_user'),
	# 		TestMain('upload_photo')
	# 		]
	# suite.addTests(tests)

	# with open(report, 'wb') as f:
	# 	runner = HTMLTestRunner(stream=f,
	# 							title=u'JCMS-UI自动化测试',
	# 							description='FeiXCMeng',
	# 							verbosity=2
	# 							)
	# 	runner.run(suite)
	case1 = TestMain()
	case1.setUp()
	case1.test_create_net(case1.website_mail)
