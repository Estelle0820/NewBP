"""
Logging module
"""

import os
import time
import logging
import logging.config

# log formats
standard_format = '[%(levelname)s][%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s]' \
                  '\n[%(filename)s:%(lineno)d][%(message)s]'
simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

root_path = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(root_path, 'logs')
if not os.path.exists(log_path):
    os.makedirs(log_path)

log_time = time.strftime("%Y_%m_%d")

# log config
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'distinct': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'less_simple': {
            'format': id_simple_format
        },
    },
    # filter decides which log to be output
    'filters': {},
    # log handlers
    'handlers': {
        # print to terminal
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # print to common log files, collect log of level higher than INFO
        'common': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # save to file
            'formatter': 'simple',
            'filename': '%s/%s.log' % (log_path, log_time),   # log file path
            'maxBytes': 1024*1024*5,    # log file size 5MB
            'backupCount': 5,
            'encoding': 'utf-8',
        },
        # print to debug log files, collect log of level higher than DEBUG
        # 'debug': {
        #     'level': 'DEBUG',
        #     'class': 'logging.handlers.RotatingFileHandler',  # save to file
        #     'formatter': 'simple',
        #     # log file path
        #     'filename': '%s/%s_debug.log' % (log_path, log_time),
        #     'maxBytes': 1024*1024*128,    # log file size 128MB
        #     'backupCount': 5,
        #     'encoding': 'utf-8',
        # },
    },
    # logger instances
    'loggers': {
        '': {
            'handlers': ['console', 'common'],
            'level': 'DEBUG',
            'propagate': True,  # propagate to higher level logger
        },
        'default': {
            'handlers': ['console', 'common'],
            'level': 'INFO',
            'propagate': True,  # propagate to higher level logger
        },
        'common': {
            'handlers': ['console', 'common'],
            'level': 'INFO',
            'propagate': True,  # propagate to higher level logger
        }
    },
}


class Logging(object):
    """Wrapped logging module"""

    @staticmethod
    def getLogger(name=None):
        logging.config.dictConfig(LOGGING_DIC)  # import logging config
        if name:
            logger = logging.getLogger(name)
        else:
            logger = logging.getLogger(__name__)
        return logger


Logging.getLogger().info("Logger initialized.")
