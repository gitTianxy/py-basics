# coding=utf-8
"""
multiprocessing.pool.ThreadPool demo
"""
from time import sleep
import threading
from multiprocessing.pool import ThreadPool

def process(item):
    global mutex
    mutex.acquire()
    print 'do process ', item
    mutex.release()
    sleep(1)

mutex = threading.Lock()
items = range(0, 50)
print 'pool_default-----------------'
pool_default = ThreadPool()
pool_default.map(process, items)
print 'pool_set-----------------'
pool_set = ThreadPool(50)
pool_set.map(process, items)