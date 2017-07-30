# coding=utf-8
"""
NOTE:
    python里的多线程只能在'单核'上执行!因为解释器CPython的进程有一个GIL锁(Global Interpreter Lock)机制:
所有线程在获取时间片之前都要竞争GIL,所以某一时刻只有一个线程在执行,当然也就只能用到一个核.
    要实现多核任务, 可以通过多进程来实现
"""
from time import sleep
import threading
from datetime import datetime


class MyThread(threading.Thread):
    def __init__(self, operation, dur):
        threading.Thread.__init__(self)
        self.operation = operation
        self.dur = dur

    def run(self):
        print 'START ', self.operation
        start = datetime.now()
        while True:
            if (datetime.now() - start).seconds > self.dur:
                print 'STOP ', self.operation
                break
            mutex.acquire()
            print self.operation
            mutex.release()
            sleep(1)


threads = []
mutex = threading.Lock()

if __name__ == '__main__':
    print 'main thread START'
    # init
    t1 = MyThread("listen music", 5)
    threads.append(t1)
    t2 = MyThread("watch movie", 10)
    threads.append(t2)
    # start threads
    for t in threads:
        t.start()
    # main-thread wait
    for t in threads:
        t.join()
    # finish
    print 'main thread FINISH'
