from processor.processor import Processor
from display.display import Display
from display.gl_output import initialize_graphics

import sys

display = Display()
processor = Processor(display)

with open(sys.argv[1], "rb") as gamefile:
  game = gamefile.read()
  processor.load_game(game)

initialize_graphics(processor)