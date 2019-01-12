from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
chromedriver ="/Users/Lenovo/Downloads/chromedriver"
browser = webdriver.Chrome(chromedriver)

browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

inputs = browser.find_element_by_xpath('//input[@name="username"]')
inputs.click()
inputs.send_keys('Email')

ayush = browser.find_element_by_xpath('//input[@name="password"]')
ayush.click()
ayush.send_keys('password')

a = browser.find_element_by_xpath('//button[@type="submit"]')
a.click()

sleep(5)
b = browser.find_element_by_xpath('//button[text()="Not Now"]')
b.click()
body_elem = browser.find_element_by_tag_name('body')
browser.get('https://www.instagram.com/explore/tags/likeforlikes/')
sleep(3)
c = browser.find_element_by_xpath('//div[@class="_9AhH0"]')
c.click()
sleep(2)
d = browser.find_element_by_xpath("//span[@aria-label='Like'and @class='glyphsSpriteHeart__outline__24__grey_9 u-__7']")


sleep(1)

e = browser.find_element_by_xpath('//a[text()="Next"]')


while (True):
	d.click()
	sleep(1)
	e.click()
	sleep(2)
	d = browser.find_element_by_xpath("//span[@aria-label='Like'and @class='glyphsSpriteHeart__outline__24__grey_9 u-__7']")
	e = browser.find_element_by_xpath('//a[text()="Next"]')



