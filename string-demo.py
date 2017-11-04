# encoding=utf-8
sql_tpl = '''
    SELECT mac.fid,mac.ekey,mac.evalue,mac.insert_time,mac.last_update_time,man.ekey,man.evalue FROM 
    fileextend_inner_0 mac LEFT JOIN
    fileextend_inner_0 man ON mac.fid=man.fid
    WHERE mac.insert_time>='2017-06-16 00:00:00' AND mac.insert_time<'2017-06-23 00:00:00' AND mac.ekey='av_scan_result'
    AND man.ekey='category' AND man.evalue='adult_video'
    '''

print sql_tpl

print ('__' in '__init__')

print ('__init__'.startswith('__'))

print ('__init__'.endswith('__'))

# join
print ','.join([str(i) for i in range(0, 5)])

# format
import math

# 小数位数控制
print 'e(3f)={:.3f}, e(6f)={:.6f}'.format(math.e, math.e)
# 总位数控制
print '12(3)={:03d}, e(6)={:06.3f}, e(8)={:08.3f}'.format(12, math.e, math.e)

# contain substring
print "'abc' in 'abc def':", 'abc' in 'abc def'
# substring--string is an array of char
print 'abc def'[:3]

# 编码问题(python 2.x存在的问题, python 3.x已统一)
'''
字符串在Python内部的表示是unicode编码, 因此，在做编码转换时，通常需要以unicode作为中间编码:
    即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。

系统默认编码通常是ascii

str.decode:将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
str.encode:先将str转成unicode编码字符(系统默认操作--用ascii方式解码, 所以当str为非ascii编码字符时,将会报错--
    除非写成str.decode('src-encode').encode('dest-encode')), 然后将unicode编码字符转换成指定编码的字符串;
    如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。
'''
tuple1 = (1, '\xe7\x8f\x8a\xe7\x8f\x8a')
tuple2 = (2, '\xe5\x88\x98')
print tuple1
print tuple2
'''
下面三句话是等价的: 注意它们都不会改变原字符串, 而是在原字符串基础上生成一个新字符串
'''
print '%s, %s' % (tuple1[0], tuple1[1])
print '%s: %s' % (tuple1[0], unicode(tuple1[1], encoding='utf8'))
print '%s: %s' % (tuple1[0], tuple1[1].decode('utf8'))

import sys

print sys.getdefaultencoding()
s = '中文'
s.decode('utf8').encode('gb18030')
'''
如下代码将报错
s.encode('gb18030')
'''

"""
关于编码:
# unicode是给各种不同的符号划分了编码序号范围,比如: 数字0-9占了[30,39]; 英文字符占了[41-7a],中文占了[4E00-9FCB].
# 而utf-8是基于unicode的一种存储方案, 它是一种变长存储方案: 比如数字/英文通常用一个字节存储, 而中文通常用3个字节存储; 
可想而知, 在unicode序列中越靠后的字符存储所需的字长越长。
"""
print len(bytearray("1234"))
print len(bytearray("hello"))
print len(bytearray("你好"))
