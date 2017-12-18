# -*- coding:utf-8 -*-
from selenium import webdriver
# from log_in_out import login
from time import sleep
from public import *

def create_audit_column():
    #新建多信息栏目（设置信息审核步骤）
    dr.find_element_by_xpath('//*[@id="nav"]/ul/li[3]').click()
    dr.switch_to_frame("menu")
    dr.find_element_by_id("tree_1_a").click()
    dr.switch_to.parent_frame()
    dr.switch_to_frame("page")
    dr.find_element_by_xpath('//*[@id="grid_toolbar"]/div[1]/a[1]').click()
    sleep(0.5)
    dr.switch_to.parent_frame()
    dr.switch_to_frame("page")
    dr.find_element_by_id("vc_cataname").send_keys("shenhelanmu_2")
    dr.find_element_by_xpath('//*[@id="tabs"]/div[1]/div[3]/ul/li[3]').click()
    dr.find_element_by_xpath('//*[@id="b_audit"]').click()
    dr.find_element_by_xpath('//*[@id="page-toolbar"]/div/table/tbody/tr/td[1]').click()
    sleep(1)
    dr.switch_to_default_content()

def set_audit_user():
    dr.find_element_by_xpath('//*[@id="nav"]/ul/li[3]').click()
    #设置审核流程和人员
    dr.switch_to.parent_frame()
    dr.switch_to_frame("page")
    dr.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[10]').click()
    dr.switch_to.parent_frame()
    dr.switch_to_frame("dialog_frame")
    sleep(0.5)
    dr.find_element_by_xpath('//*[@id="self"]').click()
    dr.find_element_by_xpath('//*[@id="chooseFlow"]').click()
    sleep(1)
    #两个iframe的名称一样，用一个list存储
    dr.switch_to_default_content()
    iframe_list = dr.find_elements_by_name('dialog_frame')
    dr.switch_to_frame(iframe_list[1])
    dr.find_element_by_xpath('//*[@id="datagrid-row-r1-2-1"]/td[1]/div/input').click()
    dr.find_element_by_xpath('//*[@id="grid_toolbar"]/div[1]').click()

    dr.switch_to.parent_frame()
    dr.switch_to_frame('dialog_frame')
    sleep(1)
    #选择审核用户1
    dr.find_element_by_xpath('//*[@id="modelNodeList"]/div[1]/div[2]/input[3]').click()
    sleep(2)
    dr.switch_to.parent_frame()
    iframe_list2 = dr.find_elements_by_name('dialog_frame')
    dr.switch_to_frame(iframe_list2[1])
    dr.switch_to_frame("userframe")
    dr.find_element_by_xpath('//*[@id="dialog-content"]/div/div[1]/div[4]/div[2]/div[2]').click()
    dr.switch_to.parent_frame()
    dr.find_element_by_xpath('//*[@id="saveChoose"]').click()
    #选择审核用户2
    dr.switch_to.parent_frame()
    dr.switch_to_frame('dialog_frame')
    dr.find_element_by_xpath('//*[@id="modelNodeList"]/div[2]/div[2]/input[3]').click()
    sleep(1)
    dr.switch_to.parent_frame()
    iframe_list3 = dr.find_elements_by_name('dialog_frame')
    dr.switch_to_frame(iframe_list3[1])
    dr.switch_to_frame('userframe')
    dr.find_element_by_xpath('//*[@id="dialog-content"]/div/div[1]/div[4]/div[3]/div[2]').click()
    dr.switch_to.parent_frame()
    dr.find_element_by_xpath('//*[@id="saveChoose"]').click()

    dr.switch_to.parent_frame()
    dr.switch_to_frame('dialog_frame')
    dr.find_element_by_xpath('//*[@id="saveChoose"]').click()

if __name__ == '__main__':
    get_url()
    login('wy', 'hanweb1')
    create_audit_column()
    set_audit_user()

