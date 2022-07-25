from multiprocessing import Pool, cpu_count
import os
import time


def task_1():
    print('Process ID: {} - Task 1 - Begin'.format(os.getpid()))
    time.sleep(2)
    print("Result: {}".format(8 ** 10))


def task_2():
    print('Process ID: {} - Task 2 - Begin'.format(os.getpid()))
    time.sleep(2)
    print("Result: {}".format(4 ** 10))


if __name__ == '__main__':
    print("CPU cores:{}".format(cpu_count()))
    print('current: {}'.format(os.getpid()))
    start = time.time()
    p = Pool(4)
    p.apply_async(task_1)
    p.apply_async(task_2)
    p.close()
    p.join()
    end = time.time()
    print("总共用时{}秒".format((end - start)))