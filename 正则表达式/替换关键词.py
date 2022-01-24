# 我们经常可以看到很多地方都会和谐关键词，有时候和谐的让人哭笑不得
# 具体操作就是通过正则表达式的替换
# 运用了re.sub()函数
# re.sub(pattern,repl,string,count,flags)
# pattern表示模式字符串，也就是正则表达式，表示要查找的字符
# repl表示关键词替换后的字符串
# string表示要进行替换检查的字符串
# count表示替换的最大次数，默认为0，即为全部替换
# flgas表示标志位，控制匹配方式，如是否区分大小写之类的，有A，I，M，S，X（具体用法见用法说明）
# 例如:

import re

if __name__ == "__main__":
    str_1 = '兵马未动，粮草先行'
    str_2 = '白色情人节'
    substring_1 = '*'
    substring_2 = '**'
    print(re.sub(r'(草)', substring_1, str_1))
    print(re.sub(r'(色情)', substring_2, str_2))

运行结果：

兵马未动，粮*先行
白**人节

进程已结束,退出代码0
