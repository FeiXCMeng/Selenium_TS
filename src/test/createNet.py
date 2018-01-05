# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from public import *
import string
import random
import os

#网站名称和网址随机
def websiteName():
	forSelect = string.ascii_letters + string.digits
	website_mail = ''
	for x in range(5):
		website_mail +=random.choice(forSelect)
	return website_mail

#新建网站
def createWebsite(website_mail):
	sleep(5)
	list_li = dr.find_elements_by_tag_name('li')
	print(len(list_li))
	if len(list_li) > 9:
		dr.find_element_by_xpath('//*[@id="nav"]/ul/li[8]/div').click()
	else:
		dr.find_element_by_xpath('//*[@id="nav"]/ul/li[1]/div').click()

	sleep(2)
	#切换到右侧iframe上,两层iframe,必须一层一层进；点击新增网站
	dr.switch_to_frame("page")
	dr.switch_to_frame("weblistframe")
	dr.find_element_by_xpath('//*[@id="grid_toolbar"]/div[1]/a[1]').click()
	sleep(3)
	dr.switch_to_default_content()
	dr.find_element_by_xpath("/html/body/div[8]/div[2]")
	dr.switch_to_frame('dialog_frame')
	dr.find_element_by_id('vc_webname').send_keys(website_mail)
	dr.find_element_by_id('vc_domains').send_keys('www.'+website_mail+'.gov.cn')
	dr.find_element_by_xpath('//*[@id="dialog-toolbar-panel"]/input[1]').click()
	sleep(15)
#新建栏目
def createColumn():
	# dr.switch_to_default_content()
	# sleep(2)
	dr.find_element_by_xpath('//*[@id="nav"]/ul/li[3]/div').click()
	sleep(2)
	dr.switch_to_frame('page')
	dr.find_element_by_xpath('//*[@id="grid_toolbar"]/div[1]/a[1]').click()
	dr.find_element_by_id('vc_cataname').send_keys('China Daily')
	dr.find_element_by_xpath('//*[@id="page-toolbar"]/div/table/tbody/tr/td[1]').click()
#新建信息
def createMessage():
	sleep(3)
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
	dr.find_element_by_id('vc_Title1').send_keys('速途网年终特刊：2017中国互联网十大新闻')

	''' 
	    无法在文章正文中输入内容，已经定位到了，但是无法输入，firefox就可以，很奇怪
	'''
	# dr.switch_to_frame('ueditor_0')
	# sleep(5)
	# dr.find_element_by_xpath('/html/body/p').click()
	# dr.find_element_by_xpath('/html/body/p').send_keys('123')
	# dr.switch_to.parent_frame()
	dr.find_element_by_id('editbutton').click()

def importIndexTemplate():
	#设置模板
	#导入首页模板
	sleep(5)
	dr.find_element_by_xpath('//*[@id="nav"]/ul/li[2]/div').click()
	sleep(1.5)
	dr.switch_to_frame('menu')
	dr.find_element_by_id('tree_3_a').click()
	dr.switch_to.parent_frame()
	dr.switch_to_frame('page')
	dr.find_element_by_xpath('//*[@id="grid_toolbar"]/div[1]/a[1]').click()
	sleep(0.8)

	#上传附件
	dr.switch_to_default_content()
	dr.switch_to_frame('dialog_frame')
	dr.find_element_by_xpath('//*[@id="oprform"]/table/tbody/tr[1]/td/a').click()
	sleep(1)
	dr.switch_to_default_content()
	#两个弹框的iframe名称一样，先获取所有iframe
	iframe_list = dr.find_elements_by_name('dialog_frame')
	dr.switch_to_frame(iframe_list[1])
	#上传附件
	'''上传附件处，添加文件的时候，必须等到“开始上传”按钮变灰才能点击，这边给一个5秒的等待时间'''
	sleep(5)
	dr.find_element_by_xpath('//*[@id="uploader_browse"]').click()
	sleep(1)
	#SendKeys第三方库，适用于python2
	# SendKeys.SendKeys('"E:\\jcms\\images.zip" "E:\\jcms\\shouye.htm"')
	# SendKeys.SendKeys("{ENTER}")
	os.system('E:\\jcms相关\\HTML模板\\首页\\images.exe "E:\\jcms相关\\HTML模板\\首页\\images.zip"')
	dr.find_element_by_xpath('//*[@id="uploader_container"]/div/div/div[2]/div[1]/div/a[2]').click()
	sleep(2)
	#上传第二个附件
	dr.switch_to_default_content()
	dr.switch_to_frame('dialog_frame')
	dr.find_element_by_xpath('//*[@id="oprform"]/table/tbody/tr[1]/td/a').click()
	sleep(1)
	dr.switch_to_default_content()
	#两个弹框的iframe名称一样，先获取所有iframe
	iframe1_list = dr.find_elements_by_name('dialog_frame')
	dr.switch_to_frame(iframe1_list[1])
	sleep(5)
	dr.find_element_by_xpath('//*[@id="uploader_browse"]').click()
	sleep(1)
	os.system('E:\\jcms相关\\HTML模板\\首页\\首页模板.exe "E:\\jcms相关\\HTML模板\\首页\\首页.htm"')
	dr.find_element_by_xpath('//*[@id="uploader_container"]/div/div/div[2]/div[1]/div/a[2]').click()
	sleep(1.5)

	#保存，让弹框消失
	dr.switch_to_default_content()
	dr.switch_to_frame('dialog_frame')
	#将滚动条向下拉动
	#chrome专属
	js = "var q = document.body.scrollTop = 10000"
	#Firefox
	# js = "var q = document.documentElement.scrollTop = 1000"
	dr.execute_script(js)
	sleep(1.5)
	dr.find_element_by_xpath('//*[@id="savebtn"]').send_keys(Keys.ENTER)

def importColumnTemplate():
	#导入栏目页模板
	dr.switch_to_default_content()
	dr.switch_to_frame('menu')
	dr.find_element_by_id('tree_4_a').click()
	dr.switch_to.parent_frame()
	dr.switch_to_frame('page')
	dr.find_element_by_xpath('//*[@id="grid_toolbar"]/div[1]/a[1]').click()
	sleep(0.8)

	dr.switch_to_default_content()
	dr.switch_to_frame('dialog_frame')
	dr.find_element_by_xpath('//*[@id="oprform"]/table/tbody/tr[1]/td/a').click()
	sleep(1)
	dr.switch_to_default_content()
	#两个弹框的iframe名称一样，先获取所有iframe
	iframe_list = dr.find_elements_by_name('dialog_frame')
	dr.switch_to_frame(iframe_list[1])
	sleep(5)
	dr.find_element_by_xpath('//*[@id="uploader_browse"]').click()
	sleep(1)
	os.system('E:\\jcms相关\\HTML模板\\栏目页\\images.exe "E:\\jcms相关\\HTML模板\\栏目页\\images.zip"')
	# SendKeys.SendKeys('"E:\\jcms\\images.zip" "E:\\jcms\\lanmuye.htm"')
	# SendKeys.SendKeys("{ENTER}")
	dr.find_element_by_xpath('//*[@id="uploader_container"]/div/div/div[2]/div[1]/div/a[2]').click()
	sleep(1.5)

	#第二个附件上传
	dr.switch_to_default_content()
	dr.switch_to_frame('dialog_frame')
	dr.find_element_by_xpath('//*[@id="oprform"]/table/tbody/tr[1]/td/a').click()
	sleep(1)
	dr.switch_to_default_content()
	# 两个弹框的iframe名称一样，先获取所有iframe
	iframe1_list = dr.find_elements_by_name('dialog_frame')
	dr.switch_to_frame(iframe1_list[1])
	sleep(5)
	dr.find_element_by_xpath('//*[@id="uploader_browse"]').click()
	sleep(1)
	os.system('E:\jcms相关\HTML模板\栏目页\招商引资页.exe "E:\jcms相关\HTML模板\栏目页\招商引资页.htm"')
	dr.find_element_by_xpath('//*[@id="uploader_container"]/div/div/div[2]/div[1]/div/a[2]').click()
	sleep(1.5)

	dr.switch_to_default_content()
	dr.switch_to_frame('dialog_frame')
	#将滚动条向下拉动
	#chrome专属
	js = "var q = document.body.scrollTop = 10000"
	#Firefox
	# js = "var q = document.documentElement.scrollTop = 1000"
	dr.execute_script(js)
	sleep(1.5)
	dr.find_element_by_xpath('//*[@id="savebtn"]').send_keys(Keys.ENTER)

def importArticleTemplate():
	#导入文章页模板
	dr.switch_to_default_content()
	dr.switch_to_frame('menu')
	dr.find_element_by_id('tree_6_a').click()
	dr.switch_to.parent_frame()
	dr.switch_to_frame('page')
	dr.find_element_by_xpath('//*[@id="grid_toolbar"]/div[1]/a[1]').click()
	sleep(0.8)

	#上传附件弹框
	dr.switch_to_default_content()
	dr.switch_to_frame('dialog_frame')
	dr.find_element_by_xpath('//*[@id="oprform"]/table/tbody/tr[1]/td/a').click()
	sleep(1)
	dr.switch_to_default_content()
	#两个弹框的iframe名称一样，先获取所有iframe
	iframe_list = dr.find_elements_by_name('dialog_frame')
	dr.switch_to_frame(iframe_list[1])
	sleep(5)
	dr.find_element_by_xpath('//*[@id="uploader_browse"]').click()
	sleep(1)
	os.system('E:\\jcms相关\\HTML模板\\文章页\\images.exe "E:\\jcms相关\\HTML模板\\文章页\\images.zip"')
	dr.find_element_by_xpath('//*[@id="uploader_container"]/div/div/div[2]/div[1]/div/a[2]').click()
	sleep(1.5)

	dr.switch_to_default_content()
	dr.switch_to_frame('dialog_frame')
	dr.find_element_by_xpath('//*[@id="oprform"]/table/tbody/tr[1]/td/a').click()
	sleep(1)
	dr.switch_to_default_content()
	# 两个弹框的iframe名称一样，先获取所有iframe
	iframe1_list = dr.find_elements_by_name('dialog_frame')
	dr.switch_to_frame(iframe1_list[1])
	sleep(5)
	dr.find_element_by_xpath('//*[@id="uploader_browse"]').click()
	sleep(1)
	os.system('E:\\jcms相关\\HTML模板\\文章页\\头条文章页.exe "E:\\jcms相关\\HTML模板\\文章页\\头条文章页.htm"')
	dr.find_element_by_xpath('//*[@id="uploader_container"]/div/div/div[2]/div[1]/div/a[2]').click()
	sleep(1.5)

	dr.switch_to_default_content()
	dr.switch_to_frame('dialog_frame')
	#将滚动条向下拉动
	#chrome专属
	js = "var q = document.body.scrollTop = 10000"
	#Firefox专属
	# js = "var q = document.documentElement.scrollTop = 1000"
	dr.execute_script(js)
	sleep(1.5)
	dr.find_element_by_xpath('//*[@id="savebtn"]').send_keys(Keys.ENTER)

def createIndexTempate():
	# 首页模板新增
	# 定位到左侧树
	dr.switch_to_default_content()
	dr.switch_to_frame('menu')
	dr.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[1]').click()
	sleep(1)
	dr.find_element_by_xpath('//*[@id="settingTree_2_a"]').send_keys(Keys.ENTER)
	sleep(2)

	dr.switch_to_default_content()
	dr.switch_to_frame('page')
	dr.find_element_by_xpath('//*[@id="obj1"]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[7]').click()
	sleep(1)
	dr.switch_to_default_content()
	dr.switch_to_frame('dialog_frame')
	s1 = Select(dr.find_element_by_id('firstElement'))
	s1.select_by_index('1')
	sleep(2)
	dr.find_element_by_xpath('//*[@id="secondElement"]/option[1]').click()
	dr.find_element_by_xpath('//*[@id="savemodal"]').click()
	sleep(6)

def createArticleTemplate():
	#文章页模板新增
	dr.switch_to_default_content()
	dr.switch_to_frame('page')
	dr.find_element_by_xpath('//*[@id="obj1"]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[7]').click()
	sleep(1)
	dr.switch_to_default_content()
	dr.switch_to_frame('dialog_frame')
	s2 = Select(dr.find_element_by_id('firstElement'))
	s2.deselect_all()
	s2.select_by_index('4')
	sleep(2)
	dr.find_element_by_xpath('//*[@id="secondElement"]/option[1]').click()
	dr.find_element_by_xpath('//*[@id="savemodal"]').click()
	sleep(4)

def createColumnTemplate():
	#栏目页模板新增
	dr.switch_to_default_content()
	dr.switch_to_frame('page')
	dr.find_element_by_xpath('//*[@id="obj1"]/table/tbody/tr[1]/td/table/tbody/tr[3]/td[7]').click()
	sleep(1)
	dr.switch_to_default_content()
	dr.switch_to_frame('dialog_frame')
	s2 = Select(dr.find_element_by_id('firstElement'))
	s2.deselect_all()
	s2.select_by_index('2')
	sleep(2)
	dr.find_element_by_xpath('//*[@id="secondElement"]/option[1]').click()
	dr.find_element_by_xpath('//*[@id="savemodal"]').click()
	sleep(4)

def setColumnTemplate():
	# 栏目页模板设置
	# 当前窗口句柄
	global main_windows
	main_windows = dr.current_window_handle
	dr.switch_to_default_content()
	dr.switch_to_frame('page')
	dr.find_element_by_xpath('//*[@id="obj1"]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[10]').click()
	sleep(1.5)
	all_windows = dr.window_handles
	print(all_windows)
	for handle in all_windows:
		if handle != main_windows:
			dr.switch_to_window(handle)
			dr.switch_to_frame('view')
			dr.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td').click()
			sleep(1)
			dr.switch_to.parent_frame()
			dr.switch_to_frame('panel')
			dr.find_element_by_xpath('//*[@id="style-selector"]').click()
			sleep(1)
			dr.switch_to.parent_frame()
			dr.switch_to_frame('dialog_frame')
			dr.find_element_by_xpath('//*[@id="1"]').click()
			sleep(1.5)
			dr.switch_to.parent_frame()
			dr.switch_to_frame('panel')
			dr.find_element_by_xpath('//*[@id="saveBtn1"]').click()
			sleep(1)
			dr.close()

def setArticleTemplate():
	#文章页模板设置
	# Article_window = dr.current_window_handle
	dr.switch_to_window(main_windows)
	# dr.switch_to_window(Article_window)
	dr.switch_to_default_content()
	dr.switch_to_frame('page')
	dr.find_element_by_xpath('//*[@id="obj1"]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[10]').click()
	sleep(1.5)
	all_window_wenzhang = dr.window_handles
	for handle in all_window_wenzhang:
		if handle != main_windows:
			dr.switch_to_window(handle)
			dr.switch_to_frame('view')
			dr.find_element_by_xpath('/html/body/table[8]/tbody/tr/td/table[2]/tbody/tr[1]/td[3]').click()
			sleep(1)
			dr.switch_to.parent_frame()
			dr.switch_to_frame('panel')
			dr.find_element_by_xpath('//*[@id="select_type"]').click()
			dr.find_element_by_xpath('//*[@id="select_type_menu"]/div/ul/li[6]').click()
			dr.find_element_by_xpath('//*[@id="style-selector"]').click()
			sleep(1)
			dr.switch_to.parent_frame()
			dr.switch_to_frame('dialog_frame')
			dr.find_element_by_xpath('//*[@id="25"]').click()
			sleep(1)
			dr.switch_to.parent_frame()
			dr.switch_to_frame('panel')
			dr.find_element_by_xpath('//*[@id="saveBtn1"]').click()
			sleep(1)
			dr.close()

def setTitleTemplate():
	#标题模板设置
	# title_windows = dr.current_window_handle
	dr.switch_to_window(main_windows)
	dr.switch_to_default_content()
	dr.switch_to_frame('page')
	dr.find_element_by_xpath('//*[@id="obj1"]/table/tbody/tr[1]/td/table/tbody/tr[3]/td[10]').click()
	sleep(1.5)
	all_window_lanmuye = dr.window_handles
	for handle in all_window_lanmuye:
		if handle != main_windows:
			dr.switch_to_window(handle)
			dr.switch_to_frame('view')
			dr.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td').click()
			sleep(0.5)
			dr.switch_to.parent_frame()
			dr.switch_to_frame('panel')
			dr.find_element_by_xpath('//*[@id="select_type"]').click()
			dr.find_element_by_xpath('//*[@id="select_type_menu"]/div/ul/li[2]').click()
			dr.find_element_by_xpath('//*[@id="style-selector"]').click()
			sleep(1)
			dr.switch_to.parent_frame()
			dr.switch_to_frame('dialog_frame')
			dr.find_element_by_xpath('//*[@id="8"]').click()
			sleep(1)
			dr.switch_to.parent_frame()
			dr.switch_to_frame('panel')
			dr.find_element_by_xpath('//*[@id="saveBtn1"]').click()
			sleep(1)
			dr.close()

def release():
	# 发布
	dr.switch_to_window(main_windows)
	sleep(2)
	dr.find_element_by_xpath('//*[@id="nav"]/ul/li[6]').click()
	sleep(0.5)
	dr.switch_to_frame('menu')
	dr.find_element_by_xpath('/html/body/ul/li[4]/a').click()
	sleep(0.5)
	dr.switch_to.parent_frame()
	dr.switch_to_frame('page')
	dr.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[3]/div/input').click()