from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()
browser.get('http://gmail.com')
action = webdriver.ActionChains(browser)
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('MyUserName')
nextButton = browser.find_element_by_id('next')
nextButton.click()
time.sleep(1)
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('MyPassword')
signinButton = browser.find_element_by_id('signIn')
signinButton.click()
