import opcode_decoder

class Opcode():
    def __init__(self, processor, address):
        self.processor = processor
        self.address = address
        self.opcode = processor.memory[address].join(processor.memory[address+1])
        pointers = opcode_decoder.decode(self.opcode)
        self.function = pointers[0]
        self.parameters = pointers[1:]
    
    def run(self):
        # Check code has not been modified by running program
        if self.processor.memory[self.address].join(self.processor.memory[self.address+1]) != self.opcode:
            self.opcode = self.processor.memory[self.address].join(self.processor.memory[self.address+1])
            pointers = opcode_decoder.decode(self.opcode)
            self.function = parameters[0]
            self.parameters = pointers[1:]
        
        # Run the function
        self.function(self.processor, *self.parameters)

        # Output function parameters
        # print("%.4X: %.4X (%s)" % (self.address, self.opcode, self.function.__name__), self.parameters)
