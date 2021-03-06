'''
Python当中的集合同数学当中的集合几乎无异
有很多操作和性质都和数学当中相同
集合不会包含重复的值（可用于筛选数据）
'''
# 具体操作
n1 = {1, 3, 5}
n2 = {2, 7, 1, 3}

print("n1", n1)
print("n2", n2)
print(n1 & n2)  # 交集
print(n1 | n2)  # 并集
print(n1 - n2)  # 差集
print(n1 ^ n2)  # 对称差集

运行结果：

n1 {1, 3, 5}
n2 {1, 2, 3, 7}
{1, 3}
{1, 2, 3, 5, 7}
{5}
{2, 5, 7}

进程已结束,退出代码0
