import sys
sys.path.append('..')
from utils import *
from createNet import *
from public import *
from setAuditUser import *
from auditArticle import *
from columnInherit import *
from manage_organization import *
from set_photoAndAttachmengt import *
from changeWebsite import *


try:
    get_url()
except:
    pass
login('wy', 'hanweb1')
website_mail = websiteName()

print(website_mail)

createWebsite(website_mail)
create_audit_column()
# #################################### createColumn()
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


login('wy', 'hanweb1')
change_website(website_mail)
set_audit_user()
sleep(1)
create_audit_message()

#信息审核通过
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
login('wy', 'hanweb1')
change_website(website_mail)
create_audit_message()
login('test', 'hanweb1')
auditArticle(1)
login('test', 'hanweb1')
first_judge()

#栏目继承
create_columnA('wy', 'hanweb1')
set_attributes()
create_columnB()
logout()


#机构用户管理
login('wy', 'hanweb1')
change_website(website_mail)
create_role(website_mail)
create_organization_user(website_mail)
logout()

#图片附件上传
login('wy', 'hanweb1')
createCategory()
upload_photo_attachment()
create_message()
dr.quit()

