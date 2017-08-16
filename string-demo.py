# encoding=utf-8
sql_tpl = '''
    SELECT mac.fid,mac.ekey,mac.evalue,mac.insert_time,mac.last_update_time,man.ekey,man.evalue FROM fileextend_inner_0 mac LEFT JOIN
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
