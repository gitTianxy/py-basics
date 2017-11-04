import json
import xlrd


def loadJson(jsonPath):
    with open(jsonPath) as json_file:
        return json.load(json_file)


def read_excel():
    path = '../result/file_excel.xls'
    workbook = xlrd.open_workbook(path)
    sheet1 = workbook.sheet_by_index(0)
    nrows = sheet1.nrows
    ncols = sheet1.ncols
    # get all cell
    for rowx in range(0, nrows):
        for colx in range(0, ncols):
            print sheet1.cell(rowx, colx).value
    # get row
    for rowx in range(0, nrows):
        print sheet1.row_values(rowx)
    # get column
    for colx in range(0, ncols):
        print sheet1.col_values(colx)


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
    # read excel
    read_excel()
    # readlines from .txt
    lines = readlines_txt(root + "pgc-cid.txt")
    for l in lines:
        print l
    print '------------------'
    print read_txt(root + "pgc-cid.txt")
