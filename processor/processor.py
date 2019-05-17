from typing import List

from display.display import Display
from processor.opcode_class import Opcode


class Processor():
    """ Virtual processor that executes chip-8 instructions and handles memory and registers. """
    def __init__(self, display: Display):
        self.register = [0 for _ in range(0x10)]
        self.key = [False for _ in range(0x10)]

        # The raw memory for the processor.
        self.memory = [0 for _ in range(0x1000)]

        # Contains opcode objects with pre-decoded instruction pointers
        # and parameters, avoiding unnecessary decoding and acting as a
        # pseudo-dynamic re-compiler.
        self.program_memory = [None for _ in range(0x1000)]

        # Not quite standard behavior as the original stack only has 16 positions
        # however the programs cannot directly access the stack so having infinite
        # indices shouldn't affect any correctly written games.
        self.stack = []

        self.immediate = 0
        self.program_counter = 0x200

        self.delay_timer = 0
        self.sound_timer = 0

        self.display = display

    def timer_tick(self):
        """ Ticks the sound and delay timer, and ensures they remain in the range [0, 256). """
        self.delay_timer = (self.delay_timer - 1) & 0xFF
        self.sound_timer = (self.sound_timer - 1) & 0xFF

    def load_rom(self, rom: List[int]):
        """ Loads the rom into memory. """
        # Loads the character set (0-F) into the memory at location 0
        self.memory[:len(rom)] = rom

    def load_game(self, game: List[int]):
        """ Loads the game into memory. """
        # Load the game into memory at 0x200+
        self.memory[0x200:0x200+len(game)] = game
        # Reset the processor state
        self.program_counter = 0x200
        self.immediate = 0

    def execute_cycle(self):
        """ Executes a single processor cycle. """
        # Check if there's an Opcode object already created
        if self.program_memory[self.program_counter] is None:
            self.program_memory[self.program_counter] = Opcode(self, self.program_counter)

        # Run the object
        self.program_memory[self.program_counter].run()
