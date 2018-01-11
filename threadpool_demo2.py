# coding=utf-8
"""
multiprocessing.pool.ThreadPool demo
----------------------------
NOTE:
    1. 线程函数只能有一个参数: 下方'process','thr_tsk'只能带一个参数
    2. 在multiprocessing中用其Lock, 在threading中用对应的Lock
"""
from time import sleep
from multiprocessing.pool import ThreadPool
from multiprocessing import Lock
# from threading import Lock


def process(item):
    global mutex
    mutex.acquire()
    print 'do process ', item
    mutex.release()
    sleep(1)


def thr_tsk(param):
    global mutex
    mutex.acquire()
    print 'do thread task. id=%s, name=%s, seq=%s' % (param['obj']['id'], param['obj']['name'], param['seq'])
    mutex.release()
    sleep(1)


if __name__ == '__main__':
    # mutex = threading.Lock()
    mutex = Lock()
    """
    items = range(0, 50)
    print 'pool_default-----------------'
    pool_default = ThreadPool()
    pool_default.map(process, items)
    print 'pool_set-----------------'
    pool_set = ThreadPool(50)
    pool_set.map(process, items)
    """

    tasks = []
    for i in range(0, 20):
        tasks.append({'obj': {'id': 'id_%s' % i, 'name': 'name_%s' % i}, 'seq': i})
    tsk_pl = ThreadPool()
    tsk_pl.map(thr_tsk, tasks)
    tsk_pl.close()
    print 'thread tasks FINISHED.'
