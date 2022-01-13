# 当我们不需要子类的行为和父类一致的时候，我们就可以采用多态的方法
# 多态就是指当子类和父类当中存在相同的方法的时候，子类的方法会覆盖掉父类的方法，代码运行的时候调用的是子类的方法
# 这样就可以对不同的类表现出不同的行为
# 如果要判断一个实例是不是某个对象，可以调用isinstance函数
# 例如
class Student:
    def say(self):
        print("我是好学生")


class Me(Student):
    def say(self):
        print("我是真滴菜狗")


class Others(Student):
    def say(self):
        print("我又考炸了！")


me = Me()
others = Others()

print(isinstance(me, Me))
print(isinstance(me, Student))
print(isinstance(others, Others))
print(isinstance(others, Others))

运行结果：

True
True
True
True

进程已结束,退出代码0
