from processor.processor import Processor
from display.display import Display
from display.window_init import initialize_windows

import argparse

def parse_arguments():
    program_description = "Chip-8 Emulator"
    memory_help_text = "Allotted memory size for program. Standard is 4096 bytes (4kb)"
    speed_help_text = "Execution speed in hz, this only affects instructions. Default is 500hz"

    parser = argparse.ArgumentParser(description=program_description)

    parser.add_argument("game")
    parser.add_argument("--debug", "-d", action="store_true", default=False)
    parser.add_argument("--memory", "-m", type=int, default=4096, help=memory_help_text)
    parser.add_argument("--speed", "-s", type=int, default=500, help=memory_help_text)

    return parser.parse_args()

arguments = parse_arguments()

display = Display()
processor = Processor(display, arguments.memory)

with open("ROM", "rb") as rom_file:
  rom = rom_file.read()
  processor.load_rom(rom)

with open(arguments.game, "rb") as game_file:
  game = game_file.read()
  processor.load_game(game)

initialize_windows(processor, arguments.speed, debug=arguments.debug)
