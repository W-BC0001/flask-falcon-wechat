"""
Python settings for project.
"""

import os
import logging
from logging.config import dictConfig

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_LOG_DIR = os.path.join(BASE_DIR, 'logs')

DEBUG = True

WECHAT_URL = 'https://qyapi.weixin.qq.com'
WECHAT_CORPID = 'your corpid, type: string'
WECHAT_CORPSECRET = 'your secret, type: string'
WECHAT_AGENT_ID = 'your agent id, type: int'

HOST = '127.0.0.1'
PORT = '2333'

# override default config
try:
    from overrides import *
except ImportError:
    pass

"""
Documentation: 
https://work.weixin.qq.com/api/doc/90000/90135/90236#markdown%E6%B6%88%E6%81%AF
"""
WECHAT_TOKEN_URL = '{}/cgi-bin/gettoken?corpid={}&corpsecret={}'.format(
    WECHAT_URL,
    WECHAT_CORPID,
    WECHAT_CORPSECRET
)

WECHAT_SEND_MESSAGE_URL = '{}/cgi-bin/message/send?access_token='.format(
    WECHAT_URL
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s'
        }
    },
    'filters': {
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, "app.log"),
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 3,
            'formatter': 'simple',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}

dictConfig(LOGGING)
logger = logging.getLogger()