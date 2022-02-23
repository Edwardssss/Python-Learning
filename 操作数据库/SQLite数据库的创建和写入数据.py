# python当中有sqlite3库以供操作数据库
# 下面演示创建数据库并存储文件

import sqlite3

database = sqlite3.connect('MySQL_1')  # 链接数据库，如果数据库不存在则创建一个
cursor = database.cursor()  # 创建一个cursor
# 创建user表
cursor.execute('create table user (id int(10) primary key ,name varchar(20))')
# 插入数据
cursor.execute('insert into user (id ,name) values ("1","Ed")')
cursor.execute('insert into user (id ,name) values ("2","Dan")')
cursor.execute('insert into user (id ,name) values ("3","Eric")')
cursor.close()  # 关闭游标
database.commit()  # 提交实务
database.close()  # 关闭connection

# 使用完数据库之后要记得关闭connection和cursor
