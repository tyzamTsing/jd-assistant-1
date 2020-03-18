# -*- coding:utf-8 -*-
import time
import datetime
from util import get_jd_time
from log import logger


class Timer(object):
    offset_time = 0

    def __init__(self, buy_time, sleep_interval=0.01):
        start_time = datetime.datetime.now()
        jd_time, elapsed = get_jd_time()
        # 开始请求时间戳
        start_time_stamp = int(time.mktime(start_time.timetuple()) * 1000) + int(start_time.microsecond / 1000)
        # 请求用时
        elapsed_time_stamp = elapsed.seconds * 1000 + int(elapsed.microseconds / 1000)
        # 电脑和京东服务器的时间差
        self.offset_time = (start_time_stamp + elapsed_time_stamp) - jd_time
        logger.info('电脑与京东服务器时差:%s毫秒' % self.offset_time)
        # '2018-09-28 22:45:50.000'
        self.buy_time = datetime.datetime.strptime(buy_time, "%Y-%m-%d %H:%M:%S.%f")
        self.sleep_interval = sleep_interval

    def start(self):
        logger.info('正在等待到达设定时间:%s' % self.buy_time)
        now_time = datetime.datetime.now
        while True:
            if now_time() - datetime.timedelta(milliseconds=self.offset_time) >= self.buy_time:
                logger.info('时间到达，开始执行……')
                break
            else:
                time.sleep(self.sleep_interval)
