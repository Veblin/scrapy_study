from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path="phantomjs")
driver.get('https://www.douban.com/')
# 等待3秒
time.sleep(3) 
print(driver.find_element_by_id('anony-sns').text)
driver.close()
