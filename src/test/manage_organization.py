# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from public import *

def create_role(website_mail):
    # login(name, password)
    sleep(1.5)
    dr.find_element_by_xpath('//*[@id="nav"]/ul/li[8]').click()
    dr.switch_to_frame('menu')
    #新增角色、设置角色权限
    dr.find_element_by_xpath('//*[@id="tree_5"]').click()
    dr.switch_to.parent_frame()
    dr.switch_to_frame('page')

    #获取相对网站名称的位置
    list_span =  dr.find_elements_by_tag_name('span')

    web_name = [list_span.index(i)+1 for i in list_span if i.text == website_mail][0]
    print(web_name)
    dr.find_element_by_xpath('/html/body/div[1]/p[%d]' % (web_name)).click()


    # dr.find_element_by_xpath('/html/body/div[1]/p[1]').click()

    sleep(0.5)
    dr.switch_to_frame('rolelistframe')
    dr.find_element_by_xpath('//*[@id="grid_toolbar"]/div[1]/a[1]').click()

    sleep(0.5)
    dr.switch_to_default_content()
    dr.switch_to_frame('dialog_frame')
    dr.find_element_by_xpath('//*[@id="vc_rolename"]').send_keys('维护信息栏目')
    dr.find_element_by_xpath('//*[@id="dialog-toolbar-panel"]/input[1]').click()
    sleep(1)
    dr.switch_to_default_content()
    dr.switch_to_frame('page')


    dr.find_element_by_xpath('/html/body/div[1]/p[%d]' % (web_name)).click()

    sleep(0.5)
    dr.switch_to_frame('rolelistframe')
    #获取新建的角色那一行，然后再定位具体的td
    list_col = dr.find_elements_by_class_name('datagrid-cell-c1-vc_rolename')
    row_num = [list_col.index(i) for i in list_col if i.text == '维护信息栏目'][0]
    # print(row_num)
    dr.find_element_by_xpath('//*[@id="page-content"]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[%d]/td[5]' % (row_num)).click()
    sleep(0.5)
    dr.switch_to_default_content()
    dr.switch_to_frame('dialog_frame')
    dr.switch_to_frame('menu_tree')
    dr.find_element_by_xpath('//*[@id="tree_3_check"]').click()
    dr.find_element_by_xpath('//*[@id="dialog-toolbar-panel"]/input[1]').click()
    sleep(1)
    dr.switch_to_default_content()
    dr.find_element_by_xpath('/html/body/div[10]/div[2]/div[3]/a').click()

    dr.switch_to_frame('dialog_frame')
    dr.find_element_by_xpath('//*[@id="tabs"]/div[1]/div[3]/ul/li[2]').click()
    dr.switch_to_frame('column_right')
    dr.switch_to_frame('right_detail')
    dr.find_element_by_xpath('//*[@id="selectall"]').click()
    dr.find_element_by_xpath('//*[@id="dialog-toolbar-panel"]/input[1]').click()
    sleep(1)
    dr.switch_to_default_content()
    dr.find_element_by_xpath('/html/body/div[10]/div[2]/div[3]/a').click()
    dr.switch_to_frame('dialog_frame')
    dr.switch_to_frame('column_right')
    dr.switch_to_frame('right_detail')
    dr.find_element_by_xpath('//*[@id="dialog-toolbar-panel"]/input[2]').click()
    dr.switch_to_default_content()

def create_organization_user(website_mail):
    dr.switch_to_frame('menu')
    dr.find_element_by_xpath('//*[@id="tree_3_span"]').click()
    sleep(0.5)
    dr.switch_to.parent_frame()
    dr.switch_to_frame('page')
    dr.switch_to_frame('deptuserlistframe')
    dr.switch_to_frame('deptlistframe')
    dr.find_element_by_xpath('//*[@id="grid_toolbar"]/div[1]/a[1]').click()
    sleep(0.5)
    dr.switch_to_default_content()
    dr.switch_to_frame('dialog_frame')

    column_name = '网站'+website_mail+'维护信息的机构'

    dr.find_element_by_xpath('//*[@id="vc_usergroupname"]').send_keys(column_name)
    dr.find_element_by_xpath('//*[@id="save"]').click()
    sleep(0.5)
    dr.switch_to_default_content()
    dr.switch_to_frame('page')
    list_li = dr.find_elements_by_tag_name('li')
    li_num = [list_li.index(i) for i in list_li if i.text == column_name][0]
    dr.find_element_by_xpath('//*[@id="tree_1_ul"]/li[%d]' %(li_num)).click()
    dr.switch_to_frame('deptuserlistframe')
    dr.find_element_by_xpath('//*[@id="tabs"]/div[1]/div[3]/ul/li[2]/a').click()
    dr.switch_to_frame('userlistframe')
    dr.find_element_by_xpath('//*[@id="grid_toolbar"]/div[1]/a[1]').click()
    sleep(1)
    dr.switch_to_default_content()
    dr.switch_to_frame('dialog_frame')
    dr.find_element_by_xpath('//*[@id="vc_username"]').send_keys('张三'+website_mail)
    dr.find_element_by_xpath('//*[@id="vc_loginid"]').send_keys('张三'+website_mail)
    dr.find_element_by_xpath('//*[@id="vc_password"]').send_keys('hanweb1')
    dr.find_element_by_xpath('//*[@id="toggle_setright"]/div').click()
    dr.find_element_by_xpath('//*[@id="save"]').click()
    sleep(1)
    dr.switch_to.parent_frame()
    dr.switch_to_frame('dialog_frame')
    dr.find_element_by_xpath('//*[@id="setRole"]').click()
    sleep(0.5)
    dr.switch_to.parent_frame()
    list_iframe = dr.find_elements_by_name('dialog_frame')
    dr.switch_to_frame(list_iframe[1])

    list_web = dr.find_elements_by_tag_name('a')
    list_web_num = [list_web.index(i) for i in list_web if i.text == website_mail][0]
    print(list_web_num)
    dr.find_element_by_xpath('//*[@id="dialog-content"]/ul/li/ul/li[%d]/span[2]'% (list_web_num-1)).click()
    # dr.find_element_by_xpath('//*[@id="tree_4_switch"]').click()
    # dr.find_element_by_xpath('//*[@id="tree_8_check"]').click()


    dr.find_element_by_xpath('//*[@id="saverole"]').click()
    sleep(0.5)
    dr.switch_to.parent_frame()
    dr.switch_to_frame('dialog_frame')
    dr.find_element_by_xpath('//*[@id="save"]').click()
    sleep(1)
    dr.switch_to_default_content()


if __name__ == '__main__':
    create_role('test', 'hanweb1')
    create_organization_user()
    logout()
    login('张三', 'hanweb1')