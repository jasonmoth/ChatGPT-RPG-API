import logging, time

def setup_game_logger():
    # LOG_FILE_START_TIME = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    # LOG_FILE_PATH = './logs/log-' + LOG_FILE_START_TIME + '.log'

    LOG_FILE_PATH = './logs/log_file.log'

    # Create the logger
    logger = logging.getLogger('game_logger')
    logger.setLevel(logging.INFO)

    # Create a file handler
    file_handler = logging.FileHandler(LOG_FILE_PATH)
    file_handler.setLevel(logging.INFO)

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter and add it to the handlers
    FILE_LOGGING_FORMAT = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    file_handler.setFormatter(FILE_LOGGING_FORMAT)

    CONSOLE_LOGGING_FORMAT = logging.Formatter('%(levelname)s: %(message)s')
    CONSOLE_LOGGING_FORMAT.formatMessage = lambda record: f"{record.levelname.capitalize()}: {record.getMessage()}"
    console_handler.setFormatter(CONSOLE_LOGGING_FORMAT)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Log messages
    # logger.debug('This is a debug message')
    # logger.info('This is an info message')
    # logger.warning('This is a warning message')
    # logger.error('This is an error message')