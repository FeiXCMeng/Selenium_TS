import sys
sys.path.append('../')
from utils.name_and_password import excel_table_byname
from utils.unittest.HTMLTestRunner_PY3 import HTMLTestRunner
# from utils.mylogger import *
from createNet import *
from public import *
from setAuditUser import *
from auditArticle import *
from columnInherit import *
from manage_organization import *
from set_photoAndAttachmengt import *
from changeWebsite import *
import unittest

global website_mail
website_mail = websiteName()
global name_passwd 
name_passwd = excel_table_byname()

# root = mylogger.log_to_RotatingFile(os.path.join('.\\runlog.txt'))
class TestMain(unittest.TestCase):
	# def __init__(self, website_mail=websiteName()):
	# 	super(TestMain, self).__init__(website_mail)
	# 	self.website_mail= website_mail

	# def setUp(self):
	# 	print('5--------------------')
	# 	get_url()

	# def tearDown(self):
	# 	dr.quit()

#新建网站、模板、信息
	def test_create_net(self):
		get_url()
		# login('wy', 'hanweb1')
		login(name_passwd[0]['name'], name_passwd[0]['password'])
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

	def test_message(self):
		# login('wy', 'hanweb1')
		login(name_passwd[0]['name'], name_passwd[0]['password'])
		change_website(website_mail)
		set_audit_user()
		sleep(1)
		create_audit_message()

#信息审核通过
	def test_judge_message(self):
		# login('test', 'hanweb1')
		login(name_passwd[1]['name'], name_passwd[1]['password'])
		change_website(website_mail)
		auditArticle()
		# login('gy', 'hanweb1')
		login(name_passwd[2]['name'], name_passwd[2]['password'])
		change_website(website_mail)
		auditArticle()
		sleep(1)
		# login('test', 'hanweb1')
		login(name_passwd[1]['name'], name_passwd[1]['password'])
		first_judge()

#信息审核不通过
	def test_judge_message2(self):
		# login('wy', 'hanweb1')
		login(name_passwd[0]['name'], name_passwd[0]['password'])
		change_website(website_mail)
		create_audit_message()
		# login('test', 'hanweb1')
		login(name_passwd[1]['name'], name_passwd[1]['password'])
		auditArticle(1)
		# login('test', 'hanweb1')
		login(name_passwd[1]['name'], name_passwd[1]['password'])
		first_judge()

#栏目继承
	def test_inherit_column(self):
		# create_columnA('wy', 'hanweb1')
		create_columnA(name_passwd[0]['name'], name_passwd[0]['password']) 
		set_attributes()
		create_columnB()
		logout()


#机构用户管理
	def test_manage_user(self):
		# login('wy', 'hanweb1')
		login(name_passwd[0]['name'], name_passwd[0]['password'])
		change_website(website_mail)
		create_role(website_mail)
		create_organization_user(website_mail)
		logout()

#图片附件上传
	def test_upload_photo(self):
		# login('wy', 'hanweb1')
		login(name_passwd[0]['name'], name_passwd[0]['password'])
		createCategory()
		upload_photo_attachment()
		create_message()

if __name__ == '__main__':
	report = '../utils/unittest/report/report.html'
	test_suite = unittest.TestSuite()
	tests = [
			TestMain('test_create_net'), 
			TestMain('test_message'), 
			TestMain('test_judge_message'),
			TestMain('test_judge_message2'),
			TestMain('test_inherit_column'),
			TestMain('test_manage_user'),
			TestMain('test_upload_photo')
			]
	test_suite.addTests(tests)
	print('3--------------------')
	with open(report, 'wb') as f:
		runner = HTMLTestRunner(stream=f,
								title=u'JCMS-UI自动化测试',
								description='FeiXCMeng',
								verbosity=2
								)
		runner.run(test_suite)
