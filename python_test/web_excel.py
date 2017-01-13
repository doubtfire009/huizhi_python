# -*- coding: utf-8 -*-
# from xlrd import *
# from xlwt import *
import xlrd
from xlutils.copy import copy
import os.path
# # w = Workbook()
# # ws = w.add_sheet('xlwt was here')
# book = xlrd.open_workbook('mini.xls')
# # book = xlrd.open_workbook("mini.xls")
# sh = book.sheet_by_index(0)
# sh.write(0,0,'A1')
#
# book.save('mini.xls')

rb = xlrd.open_workbook('mini.xls',formatting_info=True)
r_sheet = rb.sheet_by_index(0)
wb = copy(rb)
sheet = wb.get_sheet(0)
sheet.write(0,"sdfdsfs","jhh","165465")
# sheet.write(0,1,"yjhgjghj")
# sheet.write(0,2,"iuil")
wb.save('mini.xls')