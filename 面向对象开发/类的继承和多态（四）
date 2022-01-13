# 有时候我们可以不必过多关注其他的，只需要关注是不是某个类的子类即可，这样代码会更简洁
# 例如
class Student:
    def say(self):
        print("我是学生")


class Me(Student):
    def say(self):
        print("我是菜菜")


class JuLao(Student):
    def say(self):
        print("我是萌新")


def person_say(person: Student):
    person.say()


me = Me()
julao = JuLao()

person_say(me)
person_say(julao)

运行结果：

我是菜菜
我是萌新

进程已结束,退出代码0
