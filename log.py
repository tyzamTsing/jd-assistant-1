#!/usr/bin/env python
# -*- encoding=utf8 -*-
import logging
import logging.handlers
import colorlog  # 控制台日志输入颜色

LOG_FILENAME = 'jd-assistant.log'

logger = logging.getLogger()

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}


def set_logger():
    logger.setLevel(logging.INFO)
    formatter = colorlog.ColoredFormatter('%(log_color)s%(asctime)s %(levelname)s: %(message)s',
                                          log_colors=log_colors_config)
    console_handler = colorlog.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILENAME, maxBytes=10485760, backupCount=5, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


set_logger()
