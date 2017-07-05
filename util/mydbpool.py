import MySQLdb
import conf.db_config as DBConfig
from DBUtils.PooledDB import PooledDB
from contextlib import closing


class MyDbPool:
    def __init__(self, type):
        self.__pools = {}
        self.type = type

    def set_conn(self):
        # TODO
        pass

    def set_pool(self, mincached, maxcached, minconnections, maxconnections):
        # TODO
        pass

    def get_connect(self, db):
        if self.__pools.get(self.type) is None:
            if self.type == DBConfig.TYPE_CC:
                pass
            elif self.type == DBConfig.TYPE_LOCAL:
                pool = PooledDB(MySQLdb, mincached=DBConfig.LOCAL_MINCASHED, maxcached=DBConfig.LOCAL_MAXCASHED,
                                maxconnections=DBConfig.LOCAL_MAXCONNECTIONS,
                                host=DBConfig.LOCAL_HOST, user=DBConfig.LOCAL_USER, passwd=DBConfig.LOCAL_PASSWD,
                                port=DBConfig.LOCAL_PORT, db=db)
                self.__pools[self.type] = pool
            elif self.type == DBConfig.TYPE_PCC:
                pass

        return self.__pools[self.type].connection()

'''
for testing db connection
'''
def test_db(sql, type, db):
    conn = MyDbPool(type).get_connect(db)
    with closing(conn.cursor()) as cur:
        cur.execute(sql)
        print "OK"

