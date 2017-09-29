# coding=utf-8
import xlwt
from xlutils.copy import copy
from xlrd import open_workbook
import os.path

line = None
lines = []


def init_content():
    global lines
    global line
    line = "hello, this is a write-line"
    for i in range(0, 10):
        lines.append("\nthis is line %s" % i)


def write_txt(path):
    global lines
    global line
    with open(path, "w") as f:
        f.write(line)
        f.writelines(lines)
    f.close()


def create_excel(path):
    global lines
    workbook = xlwt.Workbook(encoding='utf-8') # ascii
    worksheet = workbook.add_sheet('My Worksheet')
    for idx in range(0, len(lines)):
        worksheet.write(idx, 0, label=lines[idx])
    workbook.save(path)


def append_excel(path):
    """
    append column or row
    :param path:
    :return:
    """
    if not os.path.isfile(path):
        wb = xlwt.Workbook(encoding='utf-8')
        wb.add_sheet('my sheet')
        wb.save(path)
    # open file
    wb = open_workbook(path)
    sheet = wb.sheet_by_index(0)
    nrows = sheet.nrows
    ncols = sheet.ncols
    # creates a writeable copy
    book = copy(wb)
    sheet1 = book.get_sheet(0)
    # append column
    for colx in range(ncols, ncols+2):
        for rowx in range(0, nrows):
            sheet1.write(rowx, colx, 'new colume %s' % colx)
    # append row
    for rowx in range(nrows, nrows+10):
        sheet1.write(rowx, 0, 'new row %s' % rowx)
    # save
    book.save(path)


if __name__ == "__main__":
    init_content()
    write_txt('..result/file_txt.txt')
    create_excel('..result/file_excel.xls')
    append_excel('../result/file_excel.xls')
