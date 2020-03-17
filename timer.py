# -*- coding:utf-8 -*-
import time
import datetime

import requests
from util import (
    parse_json
)
from log import logger


class Timer(object):
    offset_time = 0

    def __init__(self, buy_time, sleep_interval=0.01):
        jd_time = self.get_jd_time()
        # 当前时间戳
        now_time = datetime.datetime.now()
        obj_stamp = int(time.mktime(now_time.timetuple()) * 1000.0 + now_time.microsecond / 1000.0)
        # 时间偏移
        self.offset_time = obj_stamp - jd_time

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

    def get_jd_time(self):
        html = requests.get('https://a.jd.com//ajax/queryServerData.html')
        resp_json = parse_json(html.text)
        return resp_json.get('serverTime')
