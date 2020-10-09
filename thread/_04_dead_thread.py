import multiprocessing
import os
import threading
import time


g_num = 0
lock = threading.Lock()
#1.1添加数据任务
def task():
    #lock
    lock.acquire()
    for i in  range (1000000):
        global g_num
       # print("added:", i)
        g_num = g_num + 1

    print("task1 res :",g_num)
    # release lock
    #lock.release()



if __name__ == '__main__':

    #2.创建子进程
    task1_thread = threading.Thread(target=task, name="task1_thread")

    task2_thread = threading.Thread(target=task, name="task2_thread")

    #3.启动进程
    task1_thread.start()
    #task1_thread.join()
    task2_thread.start()