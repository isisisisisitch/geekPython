import multiprocessing
import time



#1.准备任务

def coding():
    for i in range(10):
        print("coding...")
        time.sleep(0.5)


def debugging():
    for i in range(10):
        print("debugging...")
        time.sleep(0.5)

if __name__ == '__main__':

    #2.创建进程
    #Process([group [, target [, name]])
    coding_process = multiprocessing.Process(target=coding)
    debugging_process = multiprocessing.Process(target=debugging)
    #3.启动进程
    coding_process.start()
    debugging_process.start()