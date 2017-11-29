from selenium import webdriver
# TODO chrome 等 webdriver 使用 ： https://sites.google.com/a/chromium.org/chromedriver/getting-started
browser = webdriver.Chrome('~/Downloads/chromedriver')
# browser = webdriver.Firefox(executable_path="firefox")
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS(executable_path="phantomjs")
# browser = webdriver.Safari()


browser.get("http://www.douban.com")

browser.close()