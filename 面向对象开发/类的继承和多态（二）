# 也别忘记，在继承的时候，如果子类重新定义了构造方法（也就是__init__(self)方法）
# 则父类的构造方法不会被自动调用
# 但是可以用super关键字来调用父类的构造函数
# 例如
class JULao:
    def __init__(self, name):
        self.name = name

    def play(self):
        print("我是", self.name)


class MengXin(JULao):
    def __init__(self):
        super(MengXin, self).__init__("菜菜")


dog = MengXin()
dog.play()

运行结果：

我是 菜菜

进程已结束,退出代码0

# 子类不能调用也不能继承父类的私有方法
