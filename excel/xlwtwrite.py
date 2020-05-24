#- * - coding: UTF- 8 -*-
# 如何创建和写入xls
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')
import xlwt

# workbook
wb =xlwt.Workbook(encoding='utf-8') # 一个excel

sheet = wb.add_sheet(u'倚天屠龙记')

# 写入excel 的基本操作
# sheet.write(3，4，"陈友谅") 在第三行第4列写入陈友谅

lst =[
    {"id" : 1 ,"name" : "张三丰", "age" : "100"},
    {"id" : 2 ,"name" : "张翠山", "age" : "50"},
    {"id" : 3 ,"name" : "张无忌", "age" : "20"},
    {"id" : 4 ,"name" : "殷野王", "age" : "50"},
    {"id" : 5 ,"name" : "殷素素", "age" : "40"},
    {"id" : 6 ,"name" : "殷离",   "age" : "20"}
]

"""
1  张三丰  100
2  张翠山  50
3  张无忌  20
4  殷野王  50
5  殷素素  40
"""
# 除去表头

titles = [ "id","name" ,"age"]
for i in range(len(titles)):    # 0, 1, 2
    sheet.write(0 , i ,titles[i])

titles_rows = 1
for i in range(len(lst)):
    dic = lst[i]
    sheet.write(titles_rows + i, 0, dic["id"])
    sheet.write(titles_rows + i, 1, dic["name"])
    sheet.write(titles_rows + i, 2, dic["age"])

wb.save("1.xls")













