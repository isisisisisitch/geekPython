import multiprocessing
import threading
import time



#1.准备任务

def coding():

    print("coding_thread:", threading.current_thread())

    for i in range(10):
        print("coding...")
        time.sleep(0.5)


def debugging():
    print("debugging_thread:", threading.current_thread())
    for i in range(10):
        print("debugging...")
        time.sleep(0.5)

if __name__ == '__main__':

    #2.创建进程
    #Process([group [, target [, name]])
    coding_thread = threading.Thread(target=coding,name="coding_thread")
    debugging_thread = threading.Thread(target=debugging,name="debugging_thread")
    #3.启动进程
    coding_thread.start()
    debugging_thread.start()