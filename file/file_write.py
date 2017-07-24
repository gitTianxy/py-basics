# coding=utf-8
import xlwt

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


def write_excel(path):
    global lines
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('My Worksheet')
    for idx in range(0, len(lines)):
        worksheet.write(idx, 0, label=lines[idx])
    workbook.save(path)


if __name__ == "__main__":
    init_content()
    write_txt('result/file_txt.txt')
    write_excel('result/file_excel.xls')
