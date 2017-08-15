#-*- coding:utf-8 -*-
'''
context_click()右击
double_click()双击
drag_and_drop()拖动
move_to_element()鼠标悬停
'''


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
brower = driver.get("https://www.baidu.com")


# keyword = driver.find_element_by_id("kw").click()
# ActionChains(driver).context_click(keyword).perform()

# name = driver.find_element_by_link_text(u"更多产品")
# ActionChains(driver).move_to_element(name).perform()

driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
driver.find_element_by_id("su").send_keys(Keys.ENTER)
driver.find_element_by_id("kw").clear
driver.refresh()