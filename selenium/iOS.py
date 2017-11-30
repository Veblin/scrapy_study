from selenium import webdriver
import json
with open('paths.json', 'r') as f:
    path = json.load(f)

driver_path  = path['chrome']
print("driverPath:" + driver_path)
browser = webdriver.Chrome(driver_path)
# browser = webdriver.Firefox(executable_path="firefox")
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS(executable_path="phantomjs")
# browser = webdriver.Safari()


browser.get("http://www.douban.com")

browser.close()