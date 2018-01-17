#-*- coding:utf-8 -*-
import sys
sys.path.append('../')
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

class Email(object):
    def __init__(self, server, user, password, sender, receiver, title, content):
        self.server = server
        self.user = user
        self.password = password
        self.sender = sender
        self.receiver = receiver
        self.title = title
        self.content = content
        self.message = MIMEMultipart('related')

    def send(self):
        # self.message = MIMEText('<html><h1>你好,世界</h1></html>', 'html', 'utf-8')
        # sendfile = open('E:\\log.txt', 'rb').read()
        sendfile = open('./unittest/report/report.html', 'rb').read()
        att = MIMEText(sendfile, 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment; filename="report.html"'

        
        self.message['Subject'] = self.title
        self.message.attach(att)
        self.message.attach(MIMEText(self.content))
        # self.message['Subject'] = Header(subject, 'utf-8')
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
              '2473015134@qq.com',
              'FeiXCMeng测试报告',
              '这是今天的测试报告，在附件中，请查看'
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
