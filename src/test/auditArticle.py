# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from public import *
import random

#新建一条信息，并提交审核
def create_audit_message():
    # login(name, password)
    dr.switch_to_default_content()
    dr.find_element_by_xpath('//*[@id="nav"]/ul/li/div').click()
    sleep(2)
    dr.switch_to_frame('menu')
    dr.find_element_by_id('tree1_2_span').click()
    dr.switch_to.parent_frame()
    dr.switch_to_frame('page')
    dr.find_element_by_xpath('//*[@id="grid_toolbar"]/div[1]/a[1]').click()
    dr.switch_to_default_content()
    sleep(5)
    dr.switch_to_frame('dialog_frame')
    dr.find_element_by_id('vc_Title1').send_keys('2018年来了，怎样才能达成新年目标？'+str(random.randrange(1, 100)))
    dr.find_element_by_xpath('//*[@id="moresave"]/i').click()
    sleep(0.5)
    dr.find_element_by_xpath('//*[@id="moresave-menu"]/a[2]').click()
    sleep(8)
    logout()

def auditArticle(status=0):
    sleep(1.5)
    dr.find_element_by_xpath('//*[@id="nav"]/ul/li[1]').click()
    dr.switch_to_frame("menu")
    dr.find_element_by_xpath('/html/body/div/div[2]/div[1]').click()
    sleep(0.5)
    dr.find_element_by_xpath('//*[@id="tree2_4"]').click()
    dr.switch_to.parent_frame()
    dr.switch_to_frame('page')
    dr.find_element_by_xpath(
        '//*[@id="page-content"]/div[2]/div/div[2]/div[2]/div[1]/div/table/tbody/tr/td[1]/div/input').send_keys(
        Keys.SPACE)
    if status == 0:
        dr.find_element_by_xpath('//*[@id="grid_toolbar"]/div[1]/a[1]').click()
    else:
        dr.find_element_by_xpath('//*[@id="grid_toolbar"]/div[1]/a[2]').click()
    dr.switch_to.parent_frame()
    #弹框确认
    dr.find_element_by_xpath('/html/body/div[8]/div[2]/div[4]/a[1]').click()
    sleep(0.5)
    dr.switch_to_default_content()
    logout()

#判断第一个审核员是否审核通过
def first_judge():
    sleep(1.5)
    dr.find_element_by_xpath('//*[@id="nav"]/ul/li[1]').click()
    dr.switch_to_frame("menu")
    dr.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[1]').click()
    sleep(0.5)
    dr.find_element_by_xpath('//*[@id="tree1_2"]').click()
    sleep(0.5)
    dr.switch_to.parent_frame()
    dr.switch_to_frame("page")
    # first_value = dr.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[6]/div/div/span').text
    first_value = dr.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[6]/div/div').text
    sleep(1.5)
    if first_value == "通过":
        print("信息审核通过")
    else:
        print("信息审核未通过")
    logout()

if __name__ == '__main__':
    auditArticle('wy', 'hanweb1')
    auditArticle('test', 'hanweb1')
    first_judge('wy', 'hanweb1')


