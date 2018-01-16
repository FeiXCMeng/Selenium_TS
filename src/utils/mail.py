#-*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Email(object):
    def __init__(self, server, user, password, sender, receiver):
        self.server = server
        self.user = user
        self.password = password
        self.sender = sender
        self.receiver = receiver

    def send(self):
        subject = 'Email Test!'
        self.message = MIMEText('<html><h1>你好,世界</h1></html>', 'html', 'utf-8')
        self.message['Subject'] = Header(subject, 'utf-8')
        #发件人和收件人的参数需要定义
        self.message['From'] = self.sender
        self.message['To'] = self.receiver
        smtp_server = smtplib.SMTP()
        smtp_server.connect(self.server)
        smtp_server.login(self.user, self.password)
        smtp_server.sendmail(self.sender, self.receiver, self.message.as_string())
        smtp_server.quit()
        print('sendmail success !')

if __name__ == '__main__':
    e = Email('smtp.163.com',
            'mingzulingzhen@163.com',
            'yj0211',
            'mingzulingzhen@163.com',
            '2473015134@qq.com'
            )
    e.send()
# #邮箱服务器
# smtpserver = 'smtp.163.com'
# user = 'mingzulingzhen@163.com'
# #授权码取代密码
# # password = 'yangjie~~wy0211'
# password = 'yj0211'
# #发送邮箱
# sender = 'mingzulingzhen@163.com'
# #接收邮箱
# receiver = '2473015134@qq.com'
#
# subject = 'email test'
#
# msg = MIMEText('<html><h1>你好</h1></html>', 'html', 'utf-8')
# msg['Subject'] = Header(subject, 'utf-8')
# #发件人和收件人的参数需要定义
# msg['From'] = 'mingzulingzhen@163.com'
# msg['To'] = '2473015134@qq.com'
#
# smtp = smtplib.SMTP()
# smtp.connect(smtpserver)
# smtp.login(user, password)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()
# print('sendmail success!')
