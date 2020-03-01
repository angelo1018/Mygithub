# 导入pymysql模块
import pymysql
from openpyxl import load_workbook
# print(pymysql.__dict__) #查看pymsql模块下的目录
# 连接database
# from pymysql.connections import Connection

coon = pymysql.connect ( host='localhost', user='root', password='root1234',
                                  charset='utf8' )
# 创建游标
# 得到一个可以执行SQL语句的光标对象
cursor = coon.cursor ()  # 默认情况下，我们获取到的返回值是"元组"，只能看到每行的数据，却不知道每一列代表的是什么
coon.autocommit(1)
cursor = coon.cursor()
name = 'pyexcel'
cursor.execute('create database if not exists %s' %name)
coon.select_db(name)
table_name = 'info'
cursor.execute('create table if not exists %s(id MEDIUMINT NOT NULL AUTO_INCREMENT,name varchar(30),tel varchar(30),primary key (id))'%table_name)

wb2 = load_workbook('hpu.xlsx')
ws=wb2.get_sheet_names()
for row in wb2:
	print("1")
	for cell in row:
		value1=(cell[0].value,cell[4].value)
		cursor.execute('insert into info (name,tel) values(%s,%s)',value1)

print("overing...")
