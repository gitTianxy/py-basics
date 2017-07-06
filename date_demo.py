# coding=utf-8
import time
import datetime
start = datetime.datetime.strptime('2017-01-01','%Y-%m-%d')
print 'start-day: ', start

ts = time.mktime(start.timetuple())

print 'next-day: ', datetime.datetime.fromtimestamp(ts + 24*3600)
