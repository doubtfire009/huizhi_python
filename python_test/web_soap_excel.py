from bs4 import BeautifulSoup
import re
from html.parser import HTMLParser
import string
import xlrd
from xlutils.copy import copy
import time

data_num_sum = 3
data_num = 1
record_num = 0

rb = xlrd.open_workbook('anjukehk.xls',formatting_info=True)
r_sheet = rb.sheet_by_index(0)
wb = copy(rb)
sheet = wb.get_sheet(0)
while (data_num <= data_num_sum):
    f = open("f:/data/anjukehk"+ str(data_num) +".txt", "r", encoding="utf-8")
    content = f.read()
    soup = BeautifulSoup(content)
    houseListTitles_list = soup.find_all('a',class_="houseListTitle")
    spans_list = soup.select('span[class="comm-address"]')


    # r_sheet = rb.sheet_by_index(data_num-1)

    # sheet = wb.get_sheet(data_num-1)

    print(data_num)
    for index,span in enumerate(spans_list):


        str_houseListTitle = str(houseListTitles_list[index])
        soap_houseListTitle = BeautifulSoup(str_houseListTitle, 'html.parser')
        content_houseListTitle = soap_houseListTitle.find('a').get('title')

        span_list = span.string.split("\n")

        sheet.write(record_num, 0, str(record_num+1))

        # sheet.write(record_num, 1, str(span_list[1]))

        # sheet.write(record_num, 2, str(span_list[2]))
        sheet.write(record_num, 3, content_houseListTitle)
        record_num = record_num+1
        # print(str(index+1)+"+++"+span_list[1]+"+++"+span_list[2]+"+++"+content_houseListTitle)
        print(str(record_num) + "+++" + span_list[1] + "+++" + span_list[2] + "+++" + content_houseListTitle)


    print(record_num)
    data_num = data_num + 1


wb.save('anjukehk.xls')
f.close()