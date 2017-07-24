import json


def loadJson(jsonPath):
    with open(jsonPath) as json_file:
        return json.load(json_file)


if __name__ == '__main__':
    # load json
    data = loadJson('./data/statistic_170616-170623.json')
    for item in data:
        print "fid: ", item['fid']
