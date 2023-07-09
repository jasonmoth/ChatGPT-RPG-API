from colorama import Fore, Back, Style
from pyfiglet import Figlet

TEXT_FOREGROUND = Fore.GREEN
TEXT_BACKGROUND = Back.BLACK
ASCII_FORMATTER = Figlet(font='slant')


# print(Fore.BLACK + 'Red text')
# print(Back.GREEN + 'Green background')
# print(Style.BRIGHT + 'Bright text')
# print(Style.RESET_ALL + 'Normal text')



# animated_typingASCII_FORMATTER.renderText('ASCII Art')))



import time

def animated_typing(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)  # Print the character without a newline
        time.sleep(delay)  # Pause between characters
    print()  # Print a newline after the text is typed out

# Example usage
animated_typing("Hello, world!")
print(TEXT_FOREGROUND + TEXT_BACKGROUND + ASCII_FORMATTER.renderText('ASCII Art'))