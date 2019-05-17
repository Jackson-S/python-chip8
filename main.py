import argparse

from processor.processor import Processor
from display.display import Display
from display.window_init import initialize_windows

from keyboard_layout import KEY_MAP


def parse_arguments():
    """Parses command line arguments."""
    program_description = "Chip-8 Emulator"
    speed_help_text = "Execution speed in hz, this only affects instructions. Default is 500hz"

    parser = argparse.ArgumentParser(description=program_description)

    parser.add_argument("game")
    parser.add_argument("--debug", "-d", action="store_true", default=False)
    parser.add_argument("--size", "-s", type=int, nargs=2, default=(640, 360))
    parser.add_argument("--frequency", "-f", type=int, default=500, help=speed_help_text)

    return parser.parse_args()


def main():
    arguments = parse_arguments()

    display = Display()
    processor = Processor(display)

    with open("ROM", "rb") as rom_file:
        rom = rom_file.read()
        processor.load_rom(rom)

    with open(arguments.game, "rb") as game_file:
        game = game_file.read()
        processor.load_game(game)

    initialize_windows(processor, KEY_MAP, arguments)


if __name__ == "__main__":
    main()
