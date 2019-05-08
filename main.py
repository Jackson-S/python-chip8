from processor import Processor
from display_pyglet import initialize_graphics

import sys

processor = Processor()

with open(sys.argv[1], "rb") as gamefile:
  game = gamefile.read()
  processor.load_game(game)

initialize_graphics(processor)