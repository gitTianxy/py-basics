import MySQLdb
import conf.db_config2 as DBConfig
from DBUtils.PooledDB import PooledDB
from contextlib import closing
import threadpool
import threading


class MyDbUtils:
    __pools = {}

    def __init__(self):
        pass

    @staticmethod
    def get_connect(db_config):
        if not isinstance(db_config, DBConfig.DbConfig):
            raise ValueError("db_config should be instance of 'com.pptv.conf.db_config2.DbConfig'")

        pool_key = "%s:%s" % (db_config.type, db_config.db)
        if MyDbUtils.__pools.get(pool_key) is None:
            MyDbUtils.__pools[pool_key] = PooledDB(MySQLdb, mincached=db_config.mincached,
                                                   maxcached=db_config.maxcached,
                                                   maxconnections=db_config.maxconnections,
                                                   host=db_config.host, user=db_config.user,
                                                   passwd=db_config.passwd,
                                                   port=db_config.port, db=db_config.db)

        return MyDbUtils.__pools[pool_key].connection()


'''
for testing db connection
'''

mutex = threading.Lock()


def query_demo(sql, db_config):
    global mutex
    conn = MyDbUtils.get_connect(db_config)
    with closing(conn.cursor()) as cur:
        cur.execute(sql)
        mutex.acquire()
        print "OK"
        mutex.release()


def job_demo():
    pool = threadpool.ThreadPool(5)
    works = []
    sql = "SELECT * FROM tiny_test"
    for i in range(0, 10000):
        work = (None, {'sql': sql, 'db_config': DBConfig.local_config})
        works.append(work)
    requests = threadpool.makeRequests(query_demo, works)
    for req in requests:
        pool.putRequest(req)
    pool.wait()
    print "-------------------\nFINISH"


if __name__ == "__main__":
    job_demo()
