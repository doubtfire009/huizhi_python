from selenium import webdriver
from bs4 import BeautifulSoup
# import sys
# import string
# import os
# import string
default_encoding = 'utf-8'

driver = webdriver.PhantomJS()  # webdriver.Firefox()
driver.get('http://shanghai.anjuke.com/sale/hongkou/?from=SearchBar')
print(driver.title)
# driver.find_element_by_xpath("//span[@class='comm-address']")
print(driver.find_element_by_xpath("//span[@class='comm-address']").text)

f=open(r'f:/tt.txt','w',encoding='utf-8')
f.write(driver.page_source)
f.close()
driver.quit()