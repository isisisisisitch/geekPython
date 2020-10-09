import multiprocessing
import os
import threading
import time



lock = threading.Lock()
#1.1添加数据任务
def get_val(index):
    print(threading.current_thread())


    lock.acquire()
    my_list = [10, 11, 12]
    try:
        print(threading.current_thread(), "+", my_list[index])

    except Exception as result:

        print(result)


    lock.release()


if __name__ == '__main__':


    #2.创建子进程
    for i in range (10):
        thread = threading.Thread(target=get_val, args=(i,))
        #3.启动进程
        thread.start()
