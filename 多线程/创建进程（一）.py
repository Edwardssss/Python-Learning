# multiprocessing模块有一个Process类来创建进程
# 参数说明：
# group:参数未使用，值始终为None
# target:表示当前进程启动时执行的可调用对象
# name:表示当前进程实例的别名
# args:表示传递给target函数的参数元组
# kwargs:表示传递给target函数的参数字典
# 例如:
from multiprocessing import Process


def test(interval):
    print("这个是子进程")


def main():
    print("主进程开始")
    p = Process(target=test, args=(1,))
    p.start()
    print("主进程结束")


if __name__ == "__main__":
    main()

运行结果：

主进程开始
主进程结束
这个是子进程

进程已结束,退出代码0
