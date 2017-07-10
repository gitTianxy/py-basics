# coding=utf-8

import random

# prepare data
list1 = []
dics = []
tuples = []
for i in range(0, 10):
    val = random.randrange(0, 100)
    list1.append(val)
    dics.append({'key%s' % i: val})
    tuples.append(('key%s' % i, val))

# do sort
print 'dics_before_sort: ', dics
dics.sort(key=lambda f: f.values()[0])
print 'dics_after_sort: ', dics
print 'tuples_before_sort: ', tuples
tuples.sort(key=lambda f: f[1])
print 'tupels_after_sort: ', tuples
# test sort
print 'list1_before_copy_sort: ', list1
list1_copy = list(list1)
list1_copy.sort()
print 'list1_after_copy_sort: ', list1
print 'list1_copy_after_sort: ', list1_copy

