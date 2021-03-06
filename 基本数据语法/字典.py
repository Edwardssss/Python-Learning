#字典是记录量之间的映射关系的一个序列
dictionary = {"we": "我们", "they": "他们", "world": "世界"}
print(dictionary)
"""基本操作"""
print(dictionary["we"])  # 访问字典成员
dictionary["world"] = "城市"  # 修改成员
print(dictionary)
dictionary["He"] = "他"  # 添加成员
print(dictionary)

"""函数操作"""
# dictionary.clear()  # 字典的清空
# dictionary.fromkeys(seq,x)  # 创建一个新字典，seq的元素为字典的键，x为所有参数的初始值
# dictionary.get("we")  # 使用get返回键对应的值，如果字典不存在对应的值则返回默认值
# dictionary.keys()  # 返回字典当中所有的键（作为列表输出）
# dictionary.values()  # 返回字典当中的所有的值
# keys和values常用于判断一个键或值是否在字典当中，如："city" in dictionary.keys()
# dictionary.items()  # 使用items返回一个类似列表的数据，包含了所有键和值，可用于for遍历字典
# 字典元素和整体的删除以及字典发函数复制与列表相同(copy是浅拷贝，如果字典内部还有嵌套，则元素内部还是引用)

运行结果：

{'we': '我们', 'they': '他们', 'world': '世界'}
我们
{'we': '我们', 'they': '他们', 'world': '城市'}
{'we': '我们', 'they': '他们', 'world': '城市', 'He': '他'}

进程已结束,退出代码0
