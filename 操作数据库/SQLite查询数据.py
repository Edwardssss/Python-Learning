# 我们可以通过select 字段名1，字段名2... from 表名 where 查询条件在数据库中检索我们需要的数据
# 例如

import sqlite3

database = sqlite3.connect('MySQL_1')  # 链接数据库
cursor = database.cursor()  # 创建一个cursor
# 查询数据
cursor.execute("select * from user")
# 获取查询结果
result = cursor.fetchone()
print(result)  # 打印结果
cursor.close()  # 关闭游标
database.commit()  # 提交实务
database.close()  # 关闭connection


输出结果：

(1, 'Ed')

进程已结束,退出代码0
