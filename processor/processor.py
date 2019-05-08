from .rom import rom
from .opcode_class import Opcode

class Processor():
    def __init__(self, display):
        self.register = [0 for _ in range(16)]
        self.key = [False] * 16
        self.memory = [0 for _ in range(4096)]
        self.program_memory = [None for _ in range(4096)]
        self.stack = [0 for _ in range(16)]
        self.stack_pointer = 0
        self.immediate = 0
        self.program_counter = 0x200
        self.delay_timer = 0
        self.sound_timer = 0
        self.display = display
        self.last_keypress = None
        self.cycles = 0
        
        # Load in rom code
        for x in range(80):
            self.memory[x] = rom[x]
    
    def timer_tick(self):
        self.delay_timer = (self.delay_timer - 1) & 0xFF
        self.sound_timer = (self.sound_timer - 1) & 0xFF
    
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
            self.memory[0x200 + x] = game[x]

    def execute_cycle(self):
        self.timer_tick()
        
        # Check if there's an Opcode object already created
        if self.program_memory[self.program_counter] == None:
            self.program_memory[self.program_counter] = Opcode(self, self.program_counter)
        
        # Run the object
        self.program_memory[self.program_counter].run()

        self.cycles += 1
    
    def check_integrity(self):
        for index, r in enumerate(self.register):
            if r > 255 or r < 0:
                print("Register ({}) range error: {}".format(index, r))
                exit(-1)
                return False
        for m in self.memory:
            if m < 0 or m > 255:
                print("Register value error: ", m)
                return False
        for p in self.display:
            if type(p) != bool:
                print("Pixel type error: ", type(p))
                return False
        for s in self.stack:
            if type(s) != int:
                print("stack type error")
                return False
        if type(self.immediate) != int:
            print("Immediate type error")
            return False
        return True
        