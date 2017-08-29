# encoding=utf-8
"""
es operations with the package 'elasticsearch'
----------------------------------------------
ISSUES:
    1. CRUD index
    2. save document
    3. get document
    4. search with condition
"""
from util.date_utils import DateUtils
from elasticsearch import Elasticsearch
from time import sleep


def init_es(hosts, timeout=10):
    return Elasticsearch(hosts=hosts, timeout=timeout)


def create_idx(idx, settings, mappings):
    """
    Create index with `settings` and `mappings`
    :param idx:
    :param settings:
    :param mappings:
    :return:
    """
    global es
    body = {}
    if settings:
        body['settings'] = settings
    if mappings:
        body['mappings'] = mappings
    es.indices.create(index=idx, body=body, ignore=400)


def get_idx(idx):
    global es
    try:
        return es.indices.get(index=idx)
    except Exception, e:
        print e
        return None


def delete_idx(idx):
    global es
    es.indices.delete(index=idx)


def save_document(idx, doc_type, doc_id, doc):
    """
    Adds or updates a typed JSON document in a specific index, making it searchable.
    :param idx:
    :param doc_type:
    :param doc_id:
    :param doc:
    :return:
    """
    global es
    es.index(index=idx, doc_type=doc_type, id=doc_id, body=doc)


def get_document(idx, doc_type, doc_id):
    global es
    return es.get(index=idx, doc_type=doc_type, id=doc_id)


def search(idx, doc_type, query, sort=[], start=0, size=10):
    global es
    return es.search(index=idx, doc_type=doc_type, body={'query': query, 'sort': sort, 'from': start, 'size': size})


es = None
if __name__ == '__main__':
    # preparation
    es = init_es(hosts=[{'host': '127.0.0.1', 'port': 9200}])
    idx = 'my_index'
    if get_idx(idx):
        delete_idx(idx)
    # create index
    create_idx(idx=idx, settings=None, mappings=None)
    # save document
    doc = {"name": "kevin", "age": 18,
           "birthday": DateUtils.str2dt('2000-01-01', DateUtils.DATE_PATTERN_SHORT)}
    save_document(idx=idx, doc_type='test-type', doc_id=01, doc=doc)
    # get
    print get_document(idx=idx, doc_type="test-type", doc_id=01)
    # search -- there is a time-delay before search launch
    sleep(30)
    es_query = {"filtered": {
        "query": {"matchAll": {}},
    }}
    print search(idx=idx, doc_type="test-type", query=es_query)
