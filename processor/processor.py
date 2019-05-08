from .opcode_class import Opcode

class Processor():
    def __init__(self, display):
        self.register = [0 for _ in range(0x10)]
        self.key = [False] * 0xF

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

        self.last_keypress = None
    
    def timer_tick(self):
        self.delay_timer = (self.delay_timer - 1) & 0xFF
        self.sound_timer = (self.sound_timer - 1) & 0xFF
    
    def load_rom(self, rom): 
        # Loads the character set (0-F) into the memory at location 0
        self.memory[:len(rom)] = rom
    
    def load_game(self, game):
        # Load the game into memory at 0x200+
        self.memory[0x200:0x200+len(game)] = game
        # Reset the processor state
        self.program_counter = 0x200
        self.immediate = 0

    def execute_cycle(self):
        # Due to a quirk of how the display class works this function is only called
        # at the game's frame-rate, which if 60fps will only update the timer at 60fps.
        # I plan to fix this to be 60fps always.
        self.timer_tick()
        
        # Check if there's an Opcode object already created
        if self.program_memory[self.program_counter] == None:
            self.program_memory[self.program_counter] = Opcode(self, self.program_counter)
        
        # Run the object
        self.program_memory[self.program_counter].run()
    
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
        