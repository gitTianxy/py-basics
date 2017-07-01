# coding=utf-8

import conf.db_config as DBConfig
import MySQLdb
from DBUtils.PooledDB import PooledDB


class MyDbPool:
    def __init__(self, host, user, passwd, port, db):
        self.pool = PooledDB(MySQLdb, mincached=3, maxcached=100, maxconnections=10,
                             host=host, user=user, passwd=passwd, port=port, db=db)

    def set_conn(self):
        # TODO
        pass

    def set_pool(self, mincached, maxcached, minconnections, maxconnections):
        # TODO
        pass

    def get_connect(self):
        return self.pool.connection()


if __name__ == '__main__':
    db_pool = MyDbPool(DBConfig.LOCAL_HOST, DBConfig.LOCAL_USER, DBConfig.LOCAL_PASSWD, DBConfig.LOCAL_PORT,
                       DBConfig.LOCAL_DB)
    conn = db_pool.get_connect()
