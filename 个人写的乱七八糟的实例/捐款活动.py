from threading import Thread, Lock
import time
import random

total = 0


class donate_action(Thread):
    def run(self):
        donate()


def donate():
    global total
    mutex.acquire()
    temp = total
    time.sleep(2)
    total = temp + random.randint(0,100)
    print("捐款成功，目前金额为%d元" % total)
    mutex.release()


if __name__ == "__main__":
    mutex = Lock()
    print("目前捐款金额为%d元" % total)
    people = []
    for i in range(10):
        person = donate_action(target=donate)
        people.append(person)
        person.start()
    for person in people:
        person.join()

运行结果：

目前捐款金额为0元
捐款成功，目前金额为96元
捐款成功，目前金额为172元
捐款成功，目前金额为202元
捐款成功，目前金额为262元
捐款成功，目前金额为275元
捐款成功，目前金额为341元
捐款成功，目前金额为438元
捐款成功，目前金额为506元
捐款成功，目前金额为519元
捐款成功，目前金额为559元

进程已结束,退出代码0

# 使用了产生随机数的函数，所以结果是不确定的
