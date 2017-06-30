# coding=utf-8

import conf.db_config as DBConfig
import MySQLdb
from DBUtils.PooledDB import PooledDB


class MyDbPool:
    def __init__(self, host, user, passwd, db, port):
        self.pool = PooledDB(MySQLdb, mincached=3, maxcached=100, maxconnections=10,
                             minconnections=3, host=host, user=user, passwd=passwd, db=db, port=port)

    def __init__(self, mincached, maxcached, minconnections, maxconnections, host, user, passwd, db, port):
        self.pool = PooledDB(creator=MySQLdb, mincached=mincached, maxcached=maxcached, maxconnections=maxconnections,
                             minconnections=minconnections,
                             host=host, user=user, passwd=passwd, db=db, port=port)

    def get_connect(self):
        return self.pool.connection()

if __name__ == '__main__':
    conf = DBConfig.CC_HOST
    print conf
    # db_pool = MyDbPool()
    # conn = db_pool.get_connect()

