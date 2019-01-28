from Opcodes.opcodes_flow import *
from Opcodes.opcodes_conditional import *
from Opcodes.opcodes_display import *
from Opcodes.opcodes_maths import *
from Opcodes.opcodes_memory import *
from Opcodes.opcodes_delay import *

def op_nop(processor, *args):
    processor.program_counter += 2

def function(opcode):
    functions = {
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
        "b***": op_nop,
        "c***": op_set_register_to_random_with_mask,
        "d***": op_draw,
        "e*9e": op_nop,
        "e*a1": op_nop,
        "f*07": set_register_to_delay_timer,
        "F*0a": op_nop,
        "f*15": set_delay_timer_to_register,
        "f*18": set_sound_timer_to_register,
        "f*1e": op_add_register_to_immediate,
        "f*29": op_set_immediate_to_sprite_address,
        "f*33": op_memory_at_immediate_to_binary_coded_decimal,
        "f*55": op_dump_registers_to_memory,
        "f*65": op_load_registers_from_memory,
    }

    hex_opcode = "%.4x" % opcode

    if hex_opcode in functions.keys():
        return (functions[hex_opcode], )
    elif hex_opcode[0] + "*" + hex_opcode[2:] in functions.keys():
        parameter = int(hex_opcode[1], 16)
        return (functions[hex_opcode[0] + "*" + hex_opcode[2:]], parameter)
    elif hex_opcode[0] + "**" + hex_opcode[3] in functions.keys():
        parameter_a = int(hex_opcode[1], 16)
        parameter_b = int(hex_opcode[2], 16)
        return (functions[hex_opcode[0] + "**" + hex_opcode[3]], parameter_a, parameter_b)
    elif hex_opcode[0] + "***" in functions.keys():
        if hex_opcode[0] in ("1", "2", "a", "b"):
            parameter_a = int(hex_opcode[1:], 16)
            return (functions[hex_opcode[0] + "***"], parameter_a)
        elif hex_opcode[0] in ("3", "4", "6", "7", "c"):
            parameter_a = int(hex_opcode[1], 16)
            parameter_b = int(hex_opcode[2:], 16)
            return (functions[hex_opcode[0] + "***"], parameter_a, parameter_b)
        elif hex_opcode[0] in ("d"):
            parameter_a = int(hex_opcode[1], 16)
            parameter_b = int(hex_opcode[2], 16)
            parameter_c = int(hex_opcode[3], 16)
            return (functions[hex_opcode[0] + "***"], parameter_a, parameter_b, parameter_c)
    else:
        # not valid opcode
        return (None)

class Opcode():
    def __init__(self, processor, address):
        self.processor = processor
        self.address = address
        self.opcode = processor.memory[address].join(processor.memory[address+1])
        pointers = function(self.opcode)
        self.function = pointers[0]
        self.parameters = pointers[1:]
    
    def run(self):
        # Check code has not been modified by running program
        if self.processor.memory[self.address].join(self.processor.memory[self.address+1]) != self.opcode:
            self.opcode = self.processor.memory[self.address].join(self.processor.memory[self.address+1])
            pointers = function(self.opcode)
            self.function = parameters[0]
            self.parameters = pointers[1:]
        
        print("%.4x (%s)" % (self.opcode, self.function.__name__), self.parameters)
        
        # Run the function
        self.function(self.processor, *self.parameters)