from .opcode_decoder import get_function_call

class Opcode():
    def __init__(self, processor, address):
        self.processor = processor
        self.address = address
        self.opcode = self._join(address)
        pointers = get_function_call(self.opcode)
        self.function = pointers[0]
        self.parameters = pointers[1:]
    
    def _join(self, address):
        return self.processor.memory[address] << 8 | self.processor.memory[address+1]
    
    def run(self):
        # Check code has not been modified by running program
        if self._join(self.address) != self.opcode:
            self.opcode = self._join(self.address)
            pointers = get_function_call(self.opcode)
            self.function = parameters[0]
            self.parameters = pointers[1:]
        
        # Run the function
        self.function(self.processor, *self.parameters)

        # Output function parameters
        # print("%.4X: %.4X (%s)" % (self.address, self.opcode, self.function.__name__), self.parameters)
