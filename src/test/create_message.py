# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def createAuditMessage():
    sleep(1.5)
    self.dr.find_element_by_xpath('//*[@id="nav"]/ul/li[1]').click()
    self.dr.switch_to_frame("menu")
    self.dr.find_element_by_xpath('//*[@id="tree1_2"]').click()
    self.dr.switch_to.parent_frame()
    self.dr.switch_to_frame('page')
    self.dr.find_element_by_xpath('//*[@id="grid_toolbar"]/div[1]/a[1]').click()
    sleep(0.5)
    self.dr.switch_to.parent_frame()
    self.dr.switch_to_frame('dialog_frame')
    self.dr.find_element_by_id('vc_Title1').send_keys('shenheshenheshenheshenhe')
    self.dr.find_element_by_id('editbutton').click()

def application():
    self.dr.switch_to.parent_frame()
    self.dr.switch_to_frame('page')
    sleep(1)
    self.dr.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[1]/div/input').send_keys(Keys.SPACE)
    sleep(0.5)
    self.dr.find_element_by_xpath('//*[@id="grid_toolbar"]/div[1]/a[3]').click()
    self.dr.switch_to.parent_frame()
    self.dr.find_element_by_xpath('/html/body/div[8]/div[2]/div[4]/a[1]').click()
    sleep(1)
    self.dr.find_element_by_xpath('//*[@id="nav"]/ul/li[10]').click()
    sleep(0.5)
    self.dr.find_element_by_xpath('//*[@id="nav"]/ul/li[10]/ul/li[4]').click()