import multiprocessing
import os
import threading
import time


g_list = list()
#1.1添加数据任务
def add_data():

    for i in  range (10):
        g_list.append(i)
        print("added:", i)
        time.sleep(0.3)

    print("after added:",g_list)



#1.2 读取数据任务
def read_data():

    print("read:",g_list)


if __name__ == '__main__':

    #2.创建子进程
    add_data_thread = threading.Thread(target=add_data, name="add_data_thread")

    read_data_thread = threading.Thread(target=read_data, name="read_data_thread")

    #3.启动进程
    add_data_thread.start()
    time.sleep(1)
    read_data_thread.start()