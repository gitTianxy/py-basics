# coding=utf-8
"""
日期相关方法
1. get_this_day
1. get_this_week
2. get_this_month
返回值类型: TimeRange(start_time, end_time)
"""
import datetime, time, calendar


class TimeRange:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time


def get_this_day():
    return get_day(datetime.datetime.now())


def get_this_week():
    return get_week(datetime.datetime.now())


def get_this_month():
    return get_month(datetime.datetime.now())


def get_day(input_time):
    if not isinstance(input_time, datetime.datetime):
        print 'input type: ', type(input_time)
        raise ValueError("please input datetime")
    current_ts = time.mktime(input_time.timetuple())
    start_ts = current_ts - input_time.hour * 3600 - input_time.minute * 60 - input_time.second
    end_ts = current_ts + (23 - input_time.hour) * 3600 + (59 - input_time.minute) * 60 + (60 - input_time.second)
    day_start = datetime.datetime.fromtimestamp(start_ts)
    day_end = datetime.datetime.fromtimestamp(end_ts)
    return TimeRange(start_time=day_start, end_time=day_end)


def get_week(input_time):
    if not isinstance(input_time, datetime.datetime):
        print 'input type: ', type(input_time)
        raise ValueError("please input datetime")
    input_day = get_day(input_time)
    week_day = input_time.weekday()
    week_start_ts = time.mktime(input_day.get_start_time().timetuple()) - week_day * 24 * 3600
    week_end_ts = time.mktime(input_day.get_end_time().timetuple()) + (6 - week_day) * 24 * 3600
    week_start = datetime.datetime.fromtimestamp(week_start_ts)
    week_end = datetime.datetime.fromtimestamp(week_end_ts)
    return TimeRange(start_time=week_start, end_time=week_end)


def get_month(input_time):
    if not isinstance(input_time, datetime.datetime):
        print 'input type: ', type(input_time)
        raise ValueError("please input datetime")
    input_day = get_day(input_time)
    month_range = calendar.monthrange(input_time.year, input_time.month)[1]
    month_start_ts = time.mktime(input_day.get_start_time().timetuple()) - (input_time.day - 1) * 24 * 3600
    month_end_ts = time.mktime(input_day.get_end_time().timetuple()) + (month_range - input_time.day) * 24 * 3600
    month_start = datetime.datetime.fromtimestamp(month_start_ts)
    month_end = datetime.datetime.fromtimestamp(month_end_ts)
    return TimeRange(start_time=month_start, end_time=month_end)
