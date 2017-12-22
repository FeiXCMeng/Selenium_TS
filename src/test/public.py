# -*- coding:utf-8 -*-
from time import sleep
from selenium import webdriver

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
