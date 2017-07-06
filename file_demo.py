# coding=utf-8

path = "file-demo.txt"
line = "hello, this is a write-line"
lines = []
for i in range(0, 10):
    lines.append("\nthis is line %s" % i)

with open(path, "w") as f:
    f.write(line)
    f.writelines(lines)

f.close()
