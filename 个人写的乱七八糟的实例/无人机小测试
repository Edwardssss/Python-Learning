import threading
from time import sleep

height = 100


def choice(fly, stop):
    a = input("请选择要执行的动作（1【前进】；其他【降落】）；")
    fly_1 = fly
    stop_1 = stop
    if a == '1':
        fly.run()
        choice(fly_1, stop_1)
    else:
        stop.run()


class Fly(threading.Thread):
    def run(self):
        global height
        height += 100
        sleep(2)
        print("无人机向前飞行······" + "%dm" % height)


class Stop(threading.Thread):
    def run(self):
        global height
        while height > 0:
            height -= 50
            sleep(1)
            print("高度为%dm" % height)
            if height <= 50:
                height = 0
                sleep(1)
                print("高度为%dm" % height)
                print("无人机降落成功")


if __name__ == "__main__":
    print("无人机起飞······（起始高度100m）")
    print("嗡嗡嗡")
    fly = Fly()
    stop = Stop()
    a = input("请选择要执行的动作（1【前进】；其他【降落】）；")
    if a == '1':
        fly.start()
        fly.join()
        choice(fly, stop)
    else:
        stop.start()

运行结果：

无人机起飞······（起始高度100m）
嗡嗡嗡
请选择要执行的动作（1【前进】；其他【降落】）；1
无人机向前飞行······200m
请选择要执行的动作（1【前进】；其他【降落】）；1
无人机向前飞行······300m
请选择要执行的动作（1【前进】；其他【降落】）；2
高度为250m
高度为200m
高度为150m
高度为100m
高度为50m
高度为0m
无人机降落成功

进程已结束,退出代码0
