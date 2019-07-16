import logging

logfile = 'example.log'
log_level = logging.INFO
log_to_console = True

logger = logging.getLogger('App_name')
logger.setLevel(log_level)

file_handler = logging.FileHandler(logfile)
file_handler.setLevel(log_level)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(log_level)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%d-%m-%Y %H:%M:%S')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
if log_to_console:
    logger.addHandler(stream_handler)


logger.info('example info message')
logger.debug('example debug message')
logger.warning('example warning message')
