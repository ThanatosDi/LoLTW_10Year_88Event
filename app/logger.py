import logging
import logging.config
import os
import sys

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"


class Logger(object):
    """Logger
    Logger level:
        CRITICAL    50
        ERROR	    40
        WARNING	    30
        INFO	    20
        DEBUG	    10
        NOTSET	     0
    """

    # def __init__(self, name='logger', level=logging.DEBUG):
    # logging.basicConfig(format='%(asctime)s %(levelname)s :\n%(message)s',
    #                    level=level, datefmt='%Y-%m-%d %H:%M:%S', filename='DBAPI.log', filemode='w')

    def __init__(self, name='logger', filehandler='INFO', streamhandler='INFO', workpath=None):
        """Logger
        Keyword Arguments:
            name {str} -- [name of logging] (default: {'logger'})
        """

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '%(asctime)s %(name)-8s %(levelname)-8s : %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        if not workpath:
            workpath = os.path.abspath(
                os.path.join(sys.argv[0], os.path.pardir))

        # log 檔案 handler
        file_handler = logging.handlers.TimedRotatingFileHandler(
            f'{workpath}/app.log', encoding='utf-8', when='D', backupCount=3)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(getattr(logging, filehandler.upper()))

        # stdout handler
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(formatter)
        self.stream_handler.setLevel(getattr(logging, streamhandler.upper()))

        if not self.logger.hasHandlers():
            self.logger.addHandler(file_handler)
            self.logger.addHandler(self.stream_handler)

    def levelColor(self, level):
        default_color = {
            'WARNING': MAGENTA,
            'INFO': GREEN,
            'DEBUG': CYAN,
            'CRITICAL': YELLOW,
            'ERROR': RED
        }
        color = default_color.get(level.upper(), WHITE)
        formatter = f'%(asctime)s %(name)-8s {COLOR_SEQ % (30+color)}%(levelname)-8s{RESET_SEQ} : %(message)s'
        return formatter

    def debug(self, msg):
        """ logging debug level
        Arguments:
            function {str} -- message of function
            msg {str} -- message
        """
        formatter = logging.Formatter(self.levelColor(
            'debug'), datefmt='%Y-%m-%d %H:%M:%S')
        self.stream_handler.setFormatter(formatter)
        self.logger.debug(msg)

    def info(self, msg):
        """ logging info level
        Arguments:
            function {str} -- message of function
            msg {str} -- message
        """
        # message = f" * function: {function}, * msg: {msg}"
        formatter = logging.Formatter(self.levelColor(
            'info'), datefmt='%Y-%m-%d %H:%M:%S')
        self.stream_handler.setFormatter(formatter)
        self.logger.info(msg)

    def warning(self, msg):
        """ logging warning level
        Arguments:
            function {str} -- message of function
            msg {str} -- message
        """
        # message = f" * function: {function}, * msg: {msg}"
        formatter = logging.Formatter(self.levelColor(
            'warning'), datefmt='%Y-%m-%d %H:%M:%S')
        self.stream_handler.setFormatter(formatter)
        self.logger.warning(msg)

    def error(self, msg):
        """ logging error level
        Arguments:
            function {str} -- message of function
            msg {str} -- message
        """
        # message = f" * function: {function}, * msg: {msg}"
        formatter = logging.Formatter(self.levelColor(
            'error'), datefmt='%Y-%m-%d %H:%M:%S')
        self.stream_handler.setFormatter(formatter)
        self.logger.error(msg)

    def critical(self, msg):
        formatter = logging.Formatter(self.levelColor(
            'critical'), datefmt='%Y-%m-%d %H:%M:%S')
        self.stream_handler.setFormatter(formatter)
        self.logger.critical(msg)
