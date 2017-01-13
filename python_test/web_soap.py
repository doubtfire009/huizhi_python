from bs4 import BeautifulSoup
import re
from html.parser import HTMLParser
import string
f = open("tt.txt","r",encoding='utf-8')
content = f.read()
# print(content)
soup = BeautifulSoup(content)
houseListTitles_list = soup.find_all('a',class_="houseListTitle")
spans_list = soup.select('span[class="comm-address"]')
for index,span in enumerate(spans_list):

    str_houseListTitle = str(houseListTitles_list[index])
    soap_houseListTitle = BeautifulSoup(str_houseListTitle, 'html.parser')
    content_houseListTitle = soap_houseListTitle.find('a').get('title')

    span_list = span.string.split("\n")
    print(str(index+1)+"+++"+span_list[1]+"+++"+span_list[2]+"+++"+content_houseListTitle)

    print("-------")
# for houseListTitle in houseListTitles_list:
#     # print(houseListTitle)
#     str_houseListTitle = str(houseListTitle)
#     soap_houseListTitle = BeautifulSoup(str_houseListTitle, 'html.parser')
#
#     content_test = soap_houseListTitle.find('a').get('title')
#     print(content_test)
#     print("-------")


# test = '<a class="houseListTitle " data-company="太平洋房屋" data-from="" href="http://shanghai.anjuke.com/prop/view/A654630269?from=structured_dict-saleMetro&amp;spread=commsearch_p&amp;position=1&amp;now_time=1479180630" target="_blank" title="前滩核心 超大花园房 落地窗精装修带地暖中央空调 送产权车位">'
# soap_test = BeautifulSoup(test,'html.parser')
# content_test = soap_test.find('a').get('title')
# print(content_test)


# spans_list = soup.select('span[class="comm-address"]')
# print(spans_list)


# print(len(spans_list))
# print(spans_list[0].string)
# print(spans_list[0].string.splitlines()[2])

# for span in spans_list:
#     print(span.string)
#     print("-------")

f.close()