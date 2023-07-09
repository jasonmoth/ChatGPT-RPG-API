import logging, os
from game_logger import setup_game_logger
from console import game_print


# Set up logging
setup_game_logger()
global logger
logger = logging.getLogger('game_logger')


# Environment Variables
os.environ['GAME_ENVIRONMENT_MODE'] = 'DEVELOPMENT'


def intro_scene():
    logger.info('Entering intro scene.')
    game_print('In a world torn apart by clashing kings...', 'ANTICIPATION')
    game_print('Where magic runs wild and untamed...', 'ANTICIPATION')
    game_print('And legends walk the mortal realm...', 'ANTICIPATION')
    game_print('Pendor Reborn', 'TITLE')
    game_print('By Jason McAdam', 'ANTICIPATION')


def main():
    logger.info('Entering Main Loop.')
    intro_scene()



if __name__ == '__main__':

    # Clear Terminal
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and macOS
        os.system('clear')
    
    logger.info('Program Started.')
    main()
    logger.info('Program Ended.\n\n')
