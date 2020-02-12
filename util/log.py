from os import mkdir, path
from datetime import datetime
import logging
import traceback
from . import util

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def write_log(msg, log_type, execption=None):
    configs = util.get_configs()
    log_path = configs['log_path']
    escape = configs['escape']
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    if log_type == 'execution':
        log_path += escape + 'execution'
        if not path.exists(log_path):
            mkdir(log_path, 7777)

        log_path += escape + datetime.today().strftime('%Y')
        if not path.exists(log_path):
            mkdir(log_path, 7777)

        log_path += escape + datetime.today().strftime('%m')
        if not path.exists(log_path):
            mkdir(log_path, 7777)

        log_path += escape + 'execution_' + datetime.today().strftime('%d') + '.log'
        if not path.exists(log_path):
            handler = logging.FileHandler(log_path, mode='w')
        else:
            handler = logging.FileHandler(log_path, mode='a')

        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.info(msg)
        logger.removeHandler(handler)

    elif log_type == 'error':
        log_path += escape + 'error'
        if not path.exists(log_path):
            mkdir(log_path, 7777)

        log_path += escape + datetime.today().strftime('%Y')
        if not path.exists(log_path):
            mkdir(log_path, 7777)

        log_path += escape + datetime.today().strftime('%m')
        if not path.exists(log_path):
            mkdir(log_path, 7777)

        log_path += escape + 'error_' + datetime.today().strftime('%d') + '.log'
        if not path.exists(log_path):
            handler = logging.FileHandler(log_path, mode='w')
        else:
            handler = logging.FileHandler(log_path, mode='a')

        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.info(msg)
        logger.removeHandler(handler)

    elif log_type == 'exception':
        log_path += escape + 'exception'
        if not path.exists(log_path):
            mkdir(log_path, 7777)

        log_path += escape + 'exception_' + datetime.today().strftime('%Y%m%d_%H%M%S') + '.log'
        handler = logging.FileHandler(log_path, mode='w')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        msg += '\n' + traceback.format_exc()
        logger.error(msg)
        logger.removeHandler(handler)

    else:
        raise Exception('Log type not exists')
