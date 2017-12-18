## -*- coding:utf-8 -*-
# from time import sleep

#
# def login(dr, name, password):
#     self.dr.find_element_by_id("name").clear()
#     self.dr.find_element_by_id('name').send_keys(name)
#     self.dr.find_element_by_id('password').clear()
#     self.dr.find_element_by_id('password').send_keys(password)
#     self.dr.find_element_by_id('login-btn').click()
#     sleep(1.5)
#
# def logout(dr):
#     self.dr.switch_to_default_window()
#     self.dr.find_element_by_xpath('//*[@id="nav"]/ul/li[10]').click()
#     self.dr.find_element_by_xpath('//*[@id="nav"]/ul/li[10]/ul/li[4]').click()

# -*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver

# class Public():
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password
#         self.dr = webdriver.Chrome()
#         self.dr.get('http://192.168.89.110:8139/jcms2732/login.do')
#         self.dr.maximize_window()
#
#     def login(self):
#         self.dr.find_element_by_id("name").clear()
#         self.dr.find_element_by_id('name').send_keys(self.name)
#         self.dr.find_element_by_id('password').clear()
#         self.dr.find_element_by_id('password').send_keys(self.password)
#         self.dr.find_element_by_id('login-btn').click()
#         sleep(1.5)
#
#     def logout(self):
#         self.dr.switch_to_default_content()
#         self.dr.find_element_by_xpath('//*[@id="nav"]/ul/li[10]').click()
#         self.dr.find_element_by_xpath('//*[@id="nav"]/ul/li[10]/ul/li[4]').click()
dr = webdriver.Chrome()
def get_url():
    dr.get('http://192.168.89.110:8082/jcms2732/login.do')
    # dr.get('http://192.168.5.35:8080/jcms/login.do')
    dr.maximize_window()

def login(name, password):
    dr.find_element_by_id("name").clear()
    dr.find_element_by_id('name').send_keys(name)
    dr.find_element_by_id('password').clear()
    dr.find_element_by_id('password').send_keys(password)
    dr.find_element_by_id('login-btn').click()
    sleep(1.5)

def logout():
    dr.switch_to_default_content()
    sleep(1)
    dr.find_element_by_xpath('//*[@id="nav"]/ul/li[10]').click()
    sleep(0.5)
    dr.find_element_by_xpath('//*[@id="nav"]/ul/li[10]/ul/li[4]').click()

if __name__ == '__main__':
    pass
