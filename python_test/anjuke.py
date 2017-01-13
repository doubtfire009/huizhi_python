from selenium import webdriver
from bs4 import BeautifulSoup
import time

default_encoding = 'utf-8'

driver = webdriver.PhantomJS()  # webdriver.Firefox()

page_num_max = 6
page_num = 1
url1= 'http://shanghai.anjuke.com/sale/hongkou/p'
url2= '-rd1/?kw=%E5%9C%B0%E6%9A%96&from_url=kw_final'

while(page_num <= page_num_max):
    url3 = url1 + str(page_num) + url2
    print(url3)
    driver.get(url3)

    f=open(r'f:/data/anjukehk'+ str(page_num) +'.txt','w',encoding='utf-8')
    f.write(driver.page_source)
    time.sleep(3)
    page_num = page_num + 1

f.close()



driver.quit()
# driver.find_element_by_id('search-esf').send_keys("地暖")
# driver.find_element_by_id("search-button").click()
# print(driver.find_element_by_xpath("//span[@class='comm-address']").text)



# print(driver.page_source)
