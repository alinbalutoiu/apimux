import logging
import sys

from apimux.constants import LOGGER_NAME, LOG_LEVEL, LOG_TO_FILE


class Logger(object):
    _LEVELS = [logging.CRITICAL, logging.ERROR,
               logging.WARNING, logging.INFO,
               logging.DEBUG]

    def __init__(self, name=LOGGER_NAME, log_stdout=True,
                 file_log=None, loglevel=LOG_LEVEL):
        self._logger = logging.getLogger(name)
        self.log_to_file = file_log is not None
        self.file_log = file_log
        if loglevel <= len(self._LEVELS):
            loglvl = self._LEVELS[loglevel - 1]
        else:
            loglvl = self._LEVELS[-1]
        formatter = logging.Formatter(
            fmt=('%(asctime)s.%(msecs)03d - %(levelname)s - %(threadName)s - '
                 '%(module)-8s %(message)s'),
            datefmt='%Y-%m-%d %H:%M:%S')

        if file_log:
            fh = logging.FileHandler(file_log)
            fh.setFormatter(formatter)
            self._logger.addHandler(fh)

        if log_stdout:
            ch = logging.StreamHandler(stream=sys.stdout)
            ch.setFormatter(formatter)
            self._logger.addHandler(ch)

        self._logger.setLevel(loglvl)


Logger(name=LOGGER_NAME, loglevel=LOG_LEVEL,
       file_log=LOG_TO_FILE, log_stdout=False)
logger = logging.getLogger(LOGGER_NAME)
logger.debug("Logger initialized")
logger.debug("Writing to file enabled: %s" % (LOG_TO_FILE is not None))
if LOG_TO_FILE is not None:
    logger.debug("Writing to file: %s" % LOG_TO_FILE)
