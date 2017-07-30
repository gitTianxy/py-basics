# encoding=utf-8
"""
INCLUDES:
    1. thread_local
"""
import threading
from time import sleep
import random


class ThreadLocalDemo:
    """
    ThreadLocal的作用: 用于定义'在线程间相互独立但类型相同的资源'
    用法:
        1. 定义一个ThreadLocal类型的共享变量
        2. 在子线程中把资源作为属性塞到共享变量中
        3. 此后各线程即可通过threadlocal变量独立访问各自的资源
    """

    def __init__(self):
        self.local_school = threading.local()
        t1 = threading.Thread(target=self.process_thread, args=('Alice',), name='Thread-A')
        t2 = threading.Thread(target=self.process_thread, args=('Bob',), name='Thread-B')
        t1.start()
        t2.start()
        t1.join()
        t2.join()

    def process_student(self):
        global mutex
        # 获取当前线程关联的student:
        std = self.local_school.student
        mutex.acquire()
        print('Hello, %s (in %s)' % (std, threading.current_thread().name))
        mutex.release()

    def process_thread(self, name):
        # 绑定ThreadLocal的student:
        self.local_school.student = name
        sleep(random.random())
        self.process_student()


mutex = threading.Lock()
if __name__ == "__main__":
    ThreadLocalDemo()
