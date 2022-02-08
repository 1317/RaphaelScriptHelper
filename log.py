import logging,time

log_filename = r'./log/rg' + time.strftime('_%Y%m%d') + '.log'

logger = logging.getLogger('rg_log')
logger.setLevel(logging.INFO)

# 调用模块时,如果错误引用，比如多次调用，每次会添加Handler，造成重复日志，这边每次都移除掉所有的handler，后面在重新添加，可以解决这类问题
while logger.hasHandlers():
    for i in logger.handlers:
        logger.removeHandler(i)



# file log
format='%(asctime)s [%(levelname)s] %(message)s'
date_format= '%Y/%m/%d %H:%M:%S'

formatter = logging.Formatter(fmt=format,datefmt=date_format)

handler = logging.FileHandler(log_filename, encoding='utf-8')
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)


def debug(msg, exc_info=False, stack_info=False):
    logger.debug(msg,exc_info=exc_info,stack_info=stack_info)

def info(msg, exc_info=False, stack_info=False):
    logger.info(msg,exc_info=exc_info,stack_info=stack_info)

def warning(msg, exc_info=False, stack_info=False):
    logger.warning(msg,exc_info=exc_info,stack_info=stack_info)

def error(msg, exc_info=False, stack_info=False):
    logger.error(msg,exc_info=exc_info,stack_info=stack_info)

def critical(msg, exc_info=False, stack_info=False):
    logger.critical(msg,exc_info=exc_info,stack_info=stack_info)

if __name__ == '__main__':

    logger.debug('debug')
    logger.info('info')
    logger.warning('warning')
    logger.error('error')
    logger.critical('critical')


