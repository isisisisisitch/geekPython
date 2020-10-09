import multiprocessing
import os
import time



#1.准备任务

def coding():
    coding_process_pid =  os.getpid()
    print("coding_process_pid:",coding_process_pid, multiprocessing.current_process())
    coding_parent_pid =  os.getppid()
    print("coding_parent_pid:",coding_parent_pid)
    for i in range(10):
        print("coding...")
        time.sleep(0.2)
        os.kill(coding_process_pid, 9)


def debugging():
    debugging_process_pid = os.getpid()
    print("debugging_process_pid:", debugging_process_pid, multiprocessing.current_process())
    debugging_parent_pid = os.getppid()
    print("coding_parent_pid:", debugging_parent_pid)
    for i in range(10):
        print("debugging...")
        time.sleep(0.2)

if __name__ == '__main__':
    main_pid = os.getpid()
    print("main_pid:", main_pid)
    #2.创建进程
    #Process([group [, target [, name]])
    coding_process = multiprocessing.Process(target=coding,name="coding_process")
    debugging_process = multiprocessing.Process(target=debugging,name="debugging_process")
    #3.启动进程
    coding_process.start()
    debugging_process.start()