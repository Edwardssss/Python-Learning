# 鸭子类型就是关注对象类型的使用
# 如果用不了就报错
# 意思就是拿过来就直接调用里面的方法，管他是什么，能用就对了
# 可以通过写一个函数来接受类型为目标类型的对象，并且调用当中的方法
# 例如
class Student:
    def say(self):
        print("我是学生")


class Me(Student):
    def say(self):
        print("我是菜菜")


class Others(Student):
    def say(self):
        print("我考炸了")


def person_say(person):
    person.say()


me = Me()
others = Others()

person_say(me)
person_say(others)

运行结果：

我是菜菜
我考炸了

进程已结束,退出代码0
