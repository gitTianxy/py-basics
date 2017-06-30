# coding=utf-8
from time import sleep
import threading
from datetime import datetime


class myThread(threading.Thread):
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
    t1 = myThread("listen music", 5)
    threads.append(t1)
    t2 = myThread("watch movie", 10)
    threads.append(t2)
    # start threads
    for t in threads:
        t.start()
    # main-thread wait
    for t in threads:
        t.join()
    # finish
    print 'main thread FINISH'
