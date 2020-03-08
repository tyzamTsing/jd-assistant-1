# -*- coding:utf-8 -*-
import time
import datetime

from log import logger


class Timer(object):

    def __init__(self, buy_time, sleep_interval=0.01):

        # '2018-09-28 22:45:50.000'
        self.buy_time = datetime.datetime.strptime(buy_time, "%Y-%m-%d %H:%M:%S.%f")
        self.sleep_interval = sleep_interval

    def start(self, offset_time=0):
        logger.info('正在等待到达设定时间:%s' % self.buy_time)
        now_time = datetime.datetime.now
        while True:
            if now_time() - datetime.timedelta(milliseconds=offset_time) >= self.buy_time:
                logger.info('时间到达，开始执行……')
                break
            else:
                time.sleep(self.sleep_interval)
