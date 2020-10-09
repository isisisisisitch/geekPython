import multiprocessing
import time


def task():
    while True:
        print("task executing...")
        time.sleep(0.3)



if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=task, name="sub_process")
    sub_process.daemon = True

    sub_process.start()
    time.sleep(1)
    print("main over")
#解决方法：设置守护主进程的目的是主进程退出子进程销毁，不让主进程再等待子进程去执行。