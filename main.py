from processor.processor import Processor
from display.display import Display
from display.gl_manager import initialize_graphics

import sys

display = Display()
processor = Processor(display)

with open("ROM", "rb") as rom_file:
  rom = rom_file.read()
  processor.load_rom(rom)

with open(sys.argv[1], "rb") as game_file:
  game = game_file.read()
  processor.load_game(game)

initialize_graphics(processor)