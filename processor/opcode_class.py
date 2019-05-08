from .opcodes.opcodes_flow import *
from .opcodes.opcodes_conditional import *
from .opcodes.opcodes_display import *
from .opcodes.opcodes_maths import *
from .opcodes.opcodes_memory import *
from .opcodes.opcodes_delay import *
from .opcodes.opcodes_input import *

class Opcode():
    FUNCTION_POINTERS = {
        "00e0": op_display_clear,
        "00ee": op_return,
        "1***": op_goto,
        "2***": op_call_subroutine,
        "3***": op_skip_if_register_equal_constant,
        "4***": op_skip_if_register_not_equal_constant,
        "5**0": op_skip_if_register_equal_register,
        "6***": op_assign_constant_to_register,
        "7***": op_add_constant_to_register, 
        "8**0": op_assign_register_to_register,
        "8**1": op_or_register_to_register, 
        "8**2": op_and_register_to_register,
        "8**3": op_xor_register_to_register,
        "8**4": op_add_register_to_register,
        "8**5": op_sub_register_to_register,
        "8**6": op_right_shift_register,
        "8**7": op_sub_reverse_register_to_register,
        "8**e": op_left_shift_register,
        "9**0": op_skip_if_register_not_equal_register,
        "a***": op_set_immediate_to_constant,
        "b***": op_goto_address_plus_register_zero,
        "c***": op_set_register_to_random_with_mask,
        "d***": op_draw,
        "e*9e": op_skip_if_key_pressed,
        "e*a1": op_skip_if_key_not_pressed,
        "f*07": set_register_to_delay_timer,
        "F*0a": op_halt_until_key_pressed,
        "f*15": set_delay_timer_to_register,
        "f*18": set_sound_timer_to_register,
        "f*1e": op_add_register_to_immediate,
        "f*29": op_set_immediate_to_sprite_address,
        "f*33": op_memory_at_immediate_to_binary_coded_decimal,
        "f*55": op_dump_registers_to_memory,
        "f*65": op_load_registers_from_memory,
        "****": op_nop,
    }

    def __init__(self, processor, address):
        self.processor = processor
        self.address = address
        self.opcode = self._join(address)
        pointers = self.get_function_call(self.opcode)
        self.function = pointers[0]
        self.parameters = pointers[1:]
    
    def _join(self, address):
        return self.processor.memory[address] << 8 | self.processor.memory[address+1]
    
    def run(self):
        # Check code has not been modified by running program
        if self._join(self.address) != self.opcode:
            print("Modified!")
            self.opcode = self._join(self.address)
            pointers = self.get_function_call(self.opcode)
            self.function = parameters[0]
            self.parameters = pointers[1:]
        
        # Run the function
        self.function(self.processor, *self.parameters)

        # Output function parameters
        # print("%.4X: %.4X (%s)" % (self.address, self.opcode, self.function.__name__), self.parameters)

    def get_function_call(self, opcode):
        hex_opcode = "{:04x}".format(opcode)
        parameters = []
        function_call = op_nop

        if hex_opcode in self.FUNCTION_POINTERS.keys():
            # Matches for functions with no parameters (00E0 - clear and 00EE - return)
            function_call = self.FUNCTION_POINTERS[hex_opcode]
        
        elif hex_opcode[0] + "*" + hex_opcode[2:] in self.FUNCTION_POINTERS.keys():
            # Retrieve the parameter as a base-16 integer
            parameters = [int(hex_opcode[1], 16)]
            # Replace the parameters with "*" and then get the function call from the dictionary
            opcode_without_parameters = hex_opcode[0] + "*" + hex_opcode[2:]
            function_call = self.FUNCTION_POINTERS[opcode_without_parameters]
        
        elif hex_opcode[0] + "**" + hex_opcode[3] in self.FUNCTION_POINTERS.keys():
            # Get the parameters from the opcode into a list
            parameters = [*map(lambda x: int(x, 16), hex_opcode[1:3])]
            opcode_without_parameters = hex_opcode[0] + "**" + hex_opcode[3]
            function_call = self.FUNCTION_POINTERS[opcode_without_parameters]
            # Return the function and parameters inside a tuple
        
        elif hex_opcode[0] + "***" in self.FUNCTION_POINTERS.keys():
            opcode_without_parameters = hex_opcode[0] + "***"
            if hex_opcode[0] in ("1", "2", "a", "b"):
                # Opcode like (*AAA), return the last 3 hex-values as a single parameter.
                parameters = [int(hex_opcode[1:], 16)]
                function_call = self.FUNCTION_POINTERS[opcode_without_parameters]
            
            elif hex_opcode[0] in ("3", "4", "6", "7", "c"):
                # Opcode like (*ABB), return 2nd digit as one parameter, and 3,4 digits as 1 parameter.
                parameters = [int(hex_opcode[1], 16), int(hex_opcode[2:], 16)]
                function_call = self.FUNCTION_POINTERS[opcode_without_parameters]
            
            elif hex_opcode[0] in ("d"):
                # Opcode like (*ABC), return each digit after first as separate parameter.
                parameters = [*map(lambda x: int(x, 16), hex_opcode[1:])]
                function_call = self.FUNCTION_POINTERS[opcode_without_parameters]

        if function_call == op_nop:
            print("NOP Generated from unknown instruction ({:04x})".format(opcode))

        # Return the resulting opcode
        return (function_call, *parameters)