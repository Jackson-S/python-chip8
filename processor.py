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
            self.memory[0x200 + x] = Byte(game[x])

    def execute_cycle(self):
        # Check if there's an Opcode object already created
        if self.program_memory[self.program_counter] == None:
            self.program_memory[self.program_counter] = Opcode(self, self.program_counter)
        
        # Run the object
        self.program_memory[self.program_counter].run()
    
    def check_integrity(self):
        for r in self.register:
            if type(r) != Byte:
                print("Register type error: ", type(r))
                return False
            if type(r.value) != int:
                print("Register value type error: ", type(r.value))
                return False
            if r.value < 0 or r.value > 255:
                print("Register value error: ", r.value)
                return False
        for m in self.memory:
            if type(m) != Byte:
                print("Memory type error: ", type(m))
                return False
            if m.value < 0 or m.value > 255:
                print("Register value error: ", r.value)
                return False
        for p in self.display:
            if type(p) != bool:
                print("Pixel type error: ", type(p))
                return False
        for m_a, m_b, pm in zip(self.memory[::2], self.memory[1::2], self.program_memory[::2]):
            if pm != None and m_a.join(m_b) != pm.opcode:
                print("Progmem validity error: ", m_a.join(m_b), pm.opcode)
                return False
        for r, m in zip(rom, self.memory[:80]):
            if r != m.value:
                print("Rom validity error: ", r, m)
                return False
        for s in self.stack:
            if type(s) != int:
                print("stack type error")
                return False
        if type(self.immediate) != int:
            print("Immediate type error")
            return False
        return True
        