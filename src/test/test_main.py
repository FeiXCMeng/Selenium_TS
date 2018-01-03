import sys
BASE_PATH = sys.path.append('../')
print(BASE_PATH)
from utils import *
from createNet import *
from public import *
from setAuditUser import *
from auditArticle import *
from columnInherit import *
from manage_organization import *
from set_photoAndAttachmengt import *
from changeWebsite import *
# from HTMLTestRunner_PY3 import HTMLTestRunner
import unittest		

class TestMain(unittest.TestCase):
	def __init__(self, website_mail=websiteName()):
		self.website_mail= website_mail

	def setUp(self):
		self.get_url()
		
	def tearDown(self):
		self.dr.quit()

	def test_create_net(self):		
		self.login('wy', 'hanweb1')
		website_mail = self.websiteName()

#新建网站、模板、信息
		self.createWebsite(website_mail)
		self.create_audit_column()
		self.createMessage()
		self.importIndexTemplate()
		self.importColumnTemplate()
		self.importArticleTemplate()
		self.createIndexTempate()
		self.createArticleTemplate()
		self.createColumnTemplate()
		self.setColumnTemplate()
		self.setArticleTemplate()
		self.setTitleTemplate()
		self.release()
		self.logout()

	def test_message():
		self.login('wy', 'hanweb1')
		self.change_website(website_mail)
		self.set_audit_user()
		self.sleep(1)
		self.create_audit_message()

#信息审核通过
	def test_judge_message():
		self.login('test', 'hanweb1')
		self.change_website(website_mail)
		self.auditArticle()
		self.login('gy', 'hanweb1')
		self.change_website(website_mail)
		self.auditArticle()
		self.sleep(1)
		self.login('test', 'hanweb1')
		self.first_judge()

#信息审核不通过
	def test_judge_message2():
		self.login('wy', 'hanweb1')
		self.change_website(website_mail)
		self.create_audit_message()
		self.login('test', 'hanweb1')
		self.auditArticle(1)
		self.login('test', 'hanweb1')
		self.first_judge()

#栏目继承
	def test_inherit_column():
		self.create_columnA('wy', 'hanweb1')
		self.set_attributes()
		self.create_columnB()
		self.logout()


#机构用户管理
	def test_manage_user():
		self.login('wy', 'hanweb1')
		self.change_website(website_mail)
		self.create_role(website_mail)
		self.create_organization_user(website_mail)
		self.logout()

#图片附件上传
	def upload_photo():
		self.login('wy', 'hanweb1')
		self.createCategory()
		self.upload_photo_attachment()
		self.create_message()

if __name__ == '__main__':
	report = './report.html'
	suite = unittest.TestSuite()
	suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMain))

	with open(report, 'wb') as f:
		runner = HTMLTestRunner(stream=f,
								title=u'JCMS-UI自动化测试',
								description='FeiXCMeng',
								verbosity=2
								)