"""
原来的类叫做父类
新的类叫做子类
类的继承本质上就是父类把自己有的方法和属性全部传给子类
一个子类可以同时继承于多个父类（现实生活当然不可以）

定义的写法很简单
class 子类标识符(父类1，父类2...):
    语法块
"""


# 举个栗子
class Fake:
    def __init__(self):
        print("这个是父类")

    def say(self):
        print("AK爷！")


class OIer(Fake):
    pass

class Huge_lao(OIer):
    def fake_say(self):
        print("我是菜菜")

meng_xin = OIer()
meng_xin.say()
xin_ren = Huge_lao()
xin_ren.fake_say()

# 类的继承可以省下来很多代码
# 类之间的继承关系想象起来就像是一个金字塔，从上至下（不太准确因为父类可以是多个）

运行结果：

这个是父类
AK爷！
这个是父类
我是菜菜

进程已结束,退出代码0
