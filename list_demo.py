# coding=utf-8

"""
OPERATIONS on list
1. sort
2. filter
3. map
4. reduce
"""
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

# filter
print 'filter item>5 --------------'
for i in filter(lambda s: s > 50, list1):
    print i


# map
def get_mod(num):
    global span
    return num % span


span = 10
print 'map use func ---------------'
mod_list_func = map(get_mod, list1)
for mod in mod_list_func:
    print mod

print 'map use lambda ---------------'
mod_list_lambda = map(lambda num: num % span, list1)
for mod in mod_list_lambda:
    print mod

# reduce
print 'reduce ----------------'
print reduce(lambda s1, s2: s1 + s2, list1)
