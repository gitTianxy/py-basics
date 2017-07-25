# coding=utf-8

import pymongo
from bson import json_util
from bson import ObjectId
import pprint  # pretty print
from util.mongo_connector import local_conn
import datetime


def get_db():
    return local_conn.get_db(db="pptv", user="kevin", pwd="1234")


def print_obj(obj):
    pprint.pprint(obj)


def bson_2_str(obj):
    return json_util.dumps(obj, default=json_util.default)


def get_entity(_id, f1):
    db = get_db()
    query = {}
    if _id is not None:
        query["_id"] = _id
    if f1 is not None:
        query["f1"] = f1
    return db.TestEntity.find_one(query)


def get_list():
    db = get_db()
    return db.TestEntity.find()


def save_entity(entity):
    db = get_db()
    _id = None
    if hasattr(entity, "_id"):
        _id = getattr(entity, "_id")
    f1 = None
    if hasattr(entity, "f1"):
        f1 = getattr(entity, "f1")
    old_entity = get_entity(_id, f1)
    if old_entity is None:
        db.TestEntity.insert_one(entity.to_json())
    else:
        db.TestEntity.update({
            "_id": old_entity.get("_id")
        }, {
            "$set": {
                "f1": entity.f1,
                "f2": entity.f2
            }
        })


def bulk_save():
    pass


class MEntityBase(object):
    """
    mongodb entity base
    """

    def __init__(self, db_entity):
        if db_entity.get("_id") is None:
            self._id = ObjectId()
        else:
            self._id = db_entity.get("_id")

        if db_entity.get("insert_time") is None:
            self.insert_time = datetime.datetime.utcnow()
        else:
            self.insert_time = db_entity.get("insert_time")

        if db_entity.get("update_time") is None:
            self.update_time = datetime.datetime.utcnow()
        else:
            self.update_time = db_entity.get("update_time")

    def pre_persist(self):
        if self.insert_time is None:
            self.insert_time = datetime.datetime.utcnow()
        self.update_time = datetime.datetime.utcnow()

    def to_json(self):
        self.pre_persist()
        entity_json = {}
        dics = self.__dict__.iteritems()
        for k, v in dics:
            entity_json[k] = v
        return entity_json


class TestEntity(MEntityBase):
    """
    entity for test
    """

    def __init__(self, entity):
        super(TestEntity, self).__init__(entity)
        self.f1 = entity.get("f1")
        self.f2 = entity.get("f2")


if __name__ == "__main__":
    entity_dic = {
        "f1": "field1",
        "f2": "field2"
    }
    save_entity(TestEntity(entity_dic))
    results = get_list()
    for r in results:
        print print_obj(r)
    old_entity = get_entity(ObjectId('597742b99a52c13b04d707ab'), None)
    old_entity["f2"] = "field2_NEW"
    save_entity(TestEntity(old_entity))
