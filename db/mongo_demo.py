# coding=utf-8
"""
python操作mongodb的基本用法
    1. MEntityBase: 需要提供to-dic方法(保存时用的是dic)
    2. CRUD方法

"""
import pprint  # pretty print
from util.mongo_connector import local_conn
from mongo_base import MEntityBase
from mongo_base import MaoBase
from bson import ObjectId
from util.date_utils import DateUtils


def get_db():
    return local_conn.get_db(db="pptv", user="kevin", pwd="1234")


def print_obj(obj):
    pprint.pprint(obj)


class MEntity(MEntityBase):
    """
    entity for test
    """

    def __init__(self, entity):
        MEntityBase.__init__(self, entity)
        self.f1 = entity.get("f1")
        self.f2 = entity.get("f2")
        self.innerEntity = None
        if entity.get("innerEntity") is not None:
            self.innerEntity = InnerEntity(entity.get("innerEntity"))

    def to_dic(self):
        dic = {}
        for k, v in self.__dict__.iteritems():
            if isinstance(v, InnerEntity):
                dic[k] = v.to_dic()
            else:
                dic[k] = v
        return dic


class InnerEntity:
    """
    inner entity of mentity
    """

    def __init__(self, entity):
        self.f1 = entity.get("f1")
        self.f2 = entity.get("f2")

    def to_dic(self):
        return dict(f1=self.f1, f2=self.f2)


class MEntityMao(MaoBase):
    def __init__(self):
        MaoBase.__init__(self, get_db(), "MEntity")

    def _convert_2_entity(self, db_dict):
        if db_dict is None:
            return None
        else:
            return MEntity(db_dict)


if __name__ == "__main__":
    mao = MEntityMao()
    """
    # create
    inner_dic = dict(f1="inner_f1", f2="inner_f2")
    entity_dic = dict(f1="f1", f2="f2", innerEntity=inner_dic)
    mentity = MEntity(entity_dic)
    mao.save(mentity)
    # retrieve
    db_entity = mao.get('59783a9f9a52c13ec0d0e3c9')
    # update
    db_entity.f1 = "f1_UPDATE"
    mao.save(db_entity)
    # delete
    mao.delete('597859f19a52c141bc7a5a40')
    # retrieve all entity
    for e in mao.get_all():
        e.display()
    # count all
    print mao.count_all()
    """
    '''
    query with conditions
    '''
    # query with key=val groups
    print "--------- query with 'key'='val' conditions ---------"
    for obj in mao.query(f1='f1'):
        pprint.pprint(obj.to_dic())
    # query with or condition
    or_cond = {'$or': [{'f1': 'f1'}, {'f1': 'f2'}]}
    print '--------- query with OR condition %s ---------' % or_cond
    for obj in mao.query(**or_cond):
        pprint.pprint(obj.to_dic())
    # query with and condition
    and_cond = {'$and': [{'f1': 'f1'}, {'update_time': {'$gte': DateUtils.str2dt('2017-07-26 09:40:00'), '$lt': DateUtils.str2dt('2017-07-26 09:50:00')}}]}
    print '--------- query with AND condition %s ---------' % and_cond
    for obj in mao.query(**and_cond):
        pprint.pprint(obj.to_dic())
    # query with in condition
    # in_cond = {'_id': {'$in': [ObjectId('597863df9a52c13c8053eeb8'), ObjectId('5978661d9a52c1271ccf71b6')]}}
    in_cond = {'f1': {'$in': ['f1', 'f2']}}
    print '--------- query with IN condition %s ---------' % in_cond
    for obj in mao.query(**in_cond):
        pprint.pprint(obj.to_dic())
