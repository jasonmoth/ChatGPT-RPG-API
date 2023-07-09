import logging
from anytree import Node, RenderTree
from game_logger import setup_game_logger

# Set up logging
setup_game_logger()
global logger
logger = logging.getLogger('game_logger')

MainMenu = Node('Main Menu')
StartNewGame = Node('Start New Game', parent=MainMenu)
LoadGame = Node('Load Game', parent=MainMenu)
ExitGame = Node('Exit Game', parent=MainMenu)

def _unit_test():

    for pre, fill, node in RenderTree(MainMenu):
        print("%s%s" % (pre, node.name))

if __name__ == '__main__':
    _unit_test()