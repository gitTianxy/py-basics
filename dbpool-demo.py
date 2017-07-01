# coding=utf-8

import conf.db_config as DBConfig
import MySQLdb
from DBUtils.PooledDB import PooledDB
import threadpool
import threading
from time import sleep
import random


class MyDbPool:
    def __init__(self, db):
        self.pool = PooledDB(MySQLdb, mincached=DBConfig.LOCAL_MINCASHED, maxcached=DBConfig.LOCAL_MAXCASHED,
                             maxconnections=DBConfig.LOCAL_MAXCONNECTIONS,
                             host=DBConfig.LOCAL_HOST, user=DBConfig.LOCAL_USER, passwd=DBConfig.LOCAL_PASSWD,
                             port=DBConfig.LOCAL_PORT, db=db)

    def set_conn(self):
        # TODO
        pass

    def set_pool(self, mincached, maxcached, minconnections, maxconnections):
        # TODO
        pass

    def get_connect(self):
        return self.pool.connection()


def do_query(db_pool, tbSeq, results):
    try:
        conn = db_pool.get_connect()
        cur = conn.cursor()
        cur.execute("select * from tbl_%s", (tbSeq,))
        random_dur = random.choice(range(0, 10)) / 10.0
        sleep(random_dur)
        mutex.acquire()
        results.extend(cur.fetchall())
        mutex.release()
    except Exception, e:
        print 'error when doing query: ', e.message
    finally:
        cur.close()
        conn.close()


mutex = threading.Lock()
if __name__ == '__main__':
    results = []
    db_pool = MyDbPool('db_py')
    th_pool = threadpool.ThreadPool(10)
    paras = []
    for tbSeq in range(0, 10):
        paras.append((None, {'db_pool': db_pool, 'tbSeq': tbSeq, 'results': results}))
    requests = threadpool.makeRequests(do_query, paras)
    for req in requests:
        th_pool.putRequest(req)
    th_pool.wait()

    results.sort(key=lambda e: e[1])
    for r in results:
        print r
