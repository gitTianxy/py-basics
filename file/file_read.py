import json


def loadJson(jsonPath):
    with open(jsonPath) as json_file:
        return json.load(json_file)


def readlines_txt(path):
    with open(path) as f:
        return [l.rstrip() for l in f.readlines()]


def read_txt(path):
    with open(path, 'r') as f:
        return f.read()


if __name__ == '__main__':
    root = "../data/"
    # load json
    data = loadJson(root + 'statistic_170616-170623.json')
    for item in data:
        print "fid: ", item['fid']
    # readlines from .txt
    lines = readlines_txt(root + "pgc-cid.txt")
    for l in lines:
        print l
    print '------------------'
    print read_txt(root + "pgc-cid.txt")
