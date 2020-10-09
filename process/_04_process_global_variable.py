import multiprocessing
import os
import time


g_list = list()
#1.1添加数据任务
def add_data():
    add_data_process_pid = os.getpid()
    print("add_data_process_pid:", add_data_process_pid, multiprocessing.current_process())
    for i in  range (10):
        g_list.append(i)
        print("added:", i)
        time.sleep(0.3)

    print("after added:",g_list)



#1.2 读取数据任务
def read_data():
    read_data_process_pid = os.getpid()
    print("read_data_process_pid:", read_data_process_pid, multiprocessing.current_process())
    print("read:",g_list)


if __name__ == '__main__':

    #2.创建子进程
    add_data_process = multiprocessing.Process(target=add_data, name="add_data_process")

    read_data_process = multiprocessing.Process(target=read_data, name="read_data_process")

    #3.启动进程
    add_data_process.start()
    time.sleep(1)
    read_data_process.start()