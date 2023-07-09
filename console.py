import keyboard, logging, time
from colorama import Fore, Back, Style
from pyfiglet import Figlet
from game_logger import setup_game_logger


# Set up logging
setup_game_logger()
global logger
logger = logging.getLogger('game_logger')


# Environment Variables
TITLE_BACKGROUND = Back.BLACK
TITLE_FOREGROUND = Fore.RED

NARRATION_BACKGROUND = Back.BLACK
NARRATION_FOREGROUND = Fore.MAGENTA
NARRATION_DELAY = 0.04

DIALOG_BACKGROUND = Back.BLACK
DIALOG_FOREGROUND = Fore.CYAN
DIALOG_DELAY = 0.06

ANTICIPATION_BACKGROUND = Back.BLACK
ANTICIPATION_FOREGROUND = Fore.WHITE
ANTICIPATION_DELAY = 0.08

TITLE_FONT = Figlet(font='slant')



def _animated_typing(message, background, foreground, delay=0.1):

    if message is None or len(message) == 0:
        print(background + foreground + message)
        return
    
    remaining_text = message  # Initialize with the full text
    for char in message:
        if keyboard.is_pressed('z'):
            # If a key is pressed, instantly finish printing the remaining text
            print(background + foreground + remaining_text)
            break

        print(background + foreground + char, end='', flush=True)  # Print the character without a newline

        if char == '.':
            time.sleep(delay * 4)
        if char == ',':
            time.sleep(delay * 3)
        else:
            time.sleep(delay)  # Pause between characters

        remaining_text = remaining_text[1:]  # Remove the first character from the remaining text

    print(Style.RESET_ALL)  # Print a newline after the text is typed out


def game_print(message, type='NARRATION'):
    if type == 'NARRATION':
        logger.info('Narration Started.')
        _animated_typing(message, NARRATION_BACKGROUND, NARRATION_FOREGROUND, NARRATION_DELAY)

    elif type == 'DIALOG':
        logger.info('Dialog Started.')
        _animated_typing(message, DIALOG_BACKGROUND, DIALOG_FOREGROUND, DIALOG_DELAY)

    elif type == 'TITLE':
        logger.info('Title Started.')
        print(TITLE_BACKGROUND + TITLE_FOREGROUND + TITLE_FONT.renderText(message) + Style.RESET_ALL)

    elif type == 'ANTICIPATION':
        logger.info('Anticipation Started.')
        _animated_typing(message, ANTICIPATION_BACKGROUND, ANTICIPATION_FOREGROUND, ANTICIPATION_DELAY)
    
    else:
        raise ValueError(f"Unexpected type: {type}")




def _unit_test():
    game_print('My Title', 'TITLE')
    game_print('This is a test for narration. Here is a second sentance. And a third. And some commas, another one, and finally a third.', 'NARRATION')
    game_print('This is a test for Dialog. Here is a second sentance. And a third. And some commas, another one, and finally a third.', 'DIALOG')

if __name__ == '__main__':
    _unit_test()
    pass