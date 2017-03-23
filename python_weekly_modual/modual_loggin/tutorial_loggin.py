#-*- coding:utf-8 -*-

import logging
import logging.config

'''
#1

logging.warning('watch out')
logging.info('i told u')

# 输出 loggin 只会打印输出比 warning 更高级别的日志
WARNING:root:watch out

'''

'''
# 配置 logging      # 存入文件名             # 存入的类型
logging.basicConfig(filename='example.log',level=logging.INFO)

logging.debug('the message should go to the log file')
logging.info('so should this')
logging.warning('and this')

'''

'''
logging.basicConfig(format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this envent was logged')

'''

logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)


ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')


logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simple_example')

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')











#################################
