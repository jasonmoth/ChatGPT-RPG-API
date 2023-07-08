import logging
import os
from game_logger import setup_game_logger

os.environ['GAME_ENVIRONMENT_MODE'] = 'DEVELOPMENT'

def main():

    # Setup logger
    setup_game_logger()
    logger = logging.getLogger('game_logger')
    logger.info('Program Started')

    # Exit Game
    logger.info('Program Ended\n\n')

if __name__ == '__main__':
    main()
