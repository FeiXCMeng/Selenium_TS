#-*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#邮箱服务器
smtpserver = 'smtp.163.com'
user = 'mingzulingzhen@163.com'
#授权码取代密码
# password = 'yangjie~~wy0211'
password = 'yj0211'
#发送邮箱
sender = 'mingzulingzhen@163.com'
#接收邮箱
receiver = '2473015134@qq.com'

subject = 'email test'

msg = MIMEText('<html><h1>你好</h1></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
#发件人和收件人的参数需要定义
msg['From'] = 'mingzulingzhen@163.com'
msg['To'] = '2473015134@qq.com'

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
print('sendmail success!')
