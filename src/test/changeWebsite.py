from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import sys
from public import *

def change_website(website_mail):
    dr.find_element_by_xpath('//*[@id="nav"]/ul/li[10]').click()
    dr.find_element_by_xpath('//*[@id="nav"]/ul/li[10]/ul/li[2]').click()
    sleep(1)
    dr.switch_to_frame('dialog_frame')
    dr.find_element_by_xpath('//*[@id="webname"]').send_keys(website_mail)
    sleep(0.5)
    dr.find_element_by_xpath('//*[@id="websiteId"]/option').click()
    dr.find_element_by_xpath('//*[@id="dialog-toolbar-panel"]/input[1]').click()
    sleep(1.5)
    dr.switch_to_default_content()
