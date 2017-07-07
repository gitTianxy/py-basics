# coding=utf-8

import random

list1 = []
for i in range(0, 10):
    list1.append(random.randrange(0, 100))

list1_copy = list(list1)
list1_copy.sort()
print "-------- list1 ---------"
for i1 in list1:
    print i1
print "-------- sorted list1_copy ---------"
for i2 in list1_copy:
    print i2