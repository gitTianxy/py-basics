# coding=utf-8
"""
1. dict复制
"""

# data
dict_demo = dict(a='a', b='b', c='c')

dict_new = dict(dict_demo)
dict_new['d'] = 'd'

# display
print '-----------'
for k, v in dict_demo.iteritems():
    print '%s: %s' % (k, v)
print '-----------'
for k, v in dict_new.iteritems():
    print '%s: %s' % (k, v)
