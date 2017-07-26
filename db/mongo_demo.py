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
