# coding=utf-8
import xlwt

path = "file-demo.txt"
line = "hello, this is a write-line"
lines = []
for i in range(0, 10):
    lines.append("\nthis is line %s" % i)

with open(path, "w") as f:
    f.write(line)
    f.writelines(lines)
f.close()


def write_excel():
    global lines
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('My Worksheet')
    for idx in range(0, len(lines)):
        worksheet.write(idx, 0, label=lines[idx])
    workbook.save('result/file_excel.xls')

if __name__=="__main__":
    write_excel()