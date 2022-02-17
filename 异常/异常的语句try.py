# 在python当中我们可以自定义异常情况进行准确的报错，以便于准确找到错误原因
# 例如：
number = int(input("请输入个数\n"))
people = int(input("请输入人数\n"))

try:
    result = number // people
except ValueError:
    print("数值输入错误")
except ZeroDivisionError:
    print("分配的人不能为0")
else:
    print("分配成功")
finally:
    print("完成一次分配")

输出结果：

请输入个数
100
请输入人数
0
分配的人不能为0
完成一次分配

进程已结束,退出代码0
