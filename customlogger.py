import inspect
import logging


def customLogger(logLevel=logging.DEBUG):

    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    filehandler = logging.FileHandler("automation.log", mode='a')
    filehandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                                datefmt='%m/%d/%Y : %I:%M:%S:%p')
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)

    return logger
