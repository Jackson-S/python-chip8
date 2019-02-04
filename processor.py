from rom import rom
from byte import Chip8Byte as Byte
from timer import Timer
from display import Display
from opcode_class import Opcode

class Processor():
    def __init__(self):
        self.register = [Byte(0) for _ in range(16)]
        self.key = [False] * 16
        self.memory = [Byte(0) for _ in range(4096)]
        self.program_memory = [None for _ in range(4096)]
        self.stack = [0 for _ in range(16)]
        self.stack_pointer = 0
        self.immediate = 0
        self.program_counter = 0x200
        self.delay_timer = Timer()
        self.sound_timer = Timer()
        self.display = Display()
        self.draw_screen = True
        self.last_keypress = None
        
        # Load in rom code
        for x in range(80):
            self.memory[x] = Byte(rom[x])
    
    def pop(self):
        if self.stack_pointer == 0:
            self.stack_pointer = 15
        else:
            self.stack_pointer -= 1
        return self.stack[self.stack_pointer]
    
    def push(self, value):
        self.stack[self.stack_pointer] = value
        if self.stack_pointer == 15:
            self.stack_pointer = 0
        else:
            self.stack_pointer += 1
    
    def load_game(self, game):
        for x in range(len(game)):
            self.memory[x+0x200] = Byte(game[x])

    def execute_cycle(self):
        # Check if there's an Opcode object already created
        if self.program_memory[self.program_counter] == None:
            self.program_memory[self.program_counter] = Opcode(self, self.program_counter)
        
        # Run the object
        self.program_memory[self.program_counter].run()
    
    def check_integrity(self):
        for r in self.register:
            if type(r) != Byte:
                return False
            if type(r.value) != int:
                return False
        for m in self.memory:
            if type(m) != Byte:
                return False
        