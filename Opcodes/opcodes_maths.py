from random import randint

def op_assign_constant_to_register(processor, *args):
    processor.register[args[0]] = args[1]
    processor.program_counter += 2

def op_add_constant_to_register(processor, *args):
    result = processor.register[args[0]] + args[1]
    processor.register[args[0]] = result & 0xFF
    processor.program_counter += 2

def op_assign_register_to_register(processor, *args):
    processor.register[args[0]] = processor.register[args[1]]
    processor.program_counter += 2

def op_add_register_to_register(processor, *args):
    result = processor.register[args[0]] + processor.register[args[1]]
    # Check if a carry-out occurred by checking the 2**9th bit and 
    # shifting it to position 0.
    carry_bit = (result & 0x100) >> 8
    processor.register[args[0]] = result & 0xFF
    processor.register[0xF] = carry_bit
    processor.program_counter += 2

def op_sub_register_to_register(processor, *args):
    # Or in 0x100 as a carry-in bit, which will be removed later
    result = (processor.register[args[0]] | 0x100) - processor.register[args[1]]
    # Check if a borrow occurred, by seeing if the carry bit remains
    borrow_bit = (result & 0x100) >> 8
    processor.register[0xF] = borrow_bit
    # Assign the result and remove the carry bit with an AND
    processor.register[args[0]] = result & 0xFF
    processor.program_counter += 2

def op_sub_reverse_register_to_register(processor, *args):
    # Or in 0x100 as a carry-in bit, which will be removed later
    result = (processor.register[args[1]] | 0x100) - processor.register[args[0]]
    # Check if a borrow occurred, by seeing if the carry bit remains
    borrow_bit = (result & 0x100) >> 8
    processor.register[0xF] = borrow_bit
    # Assign the result and remove the carry bit with an AND
    processor.register[args[0]] = result & 0xFF
    processor.program_counter += 2

def op_or_register_to_register(processor, *args):
    processor.register[args[0]] |= processor.register[args[1]]
    processor.program_counter += 2

def op_and_register_to_register(processor, *args):
    processor.register[args[0]] &= processor.register[args[1]]
    processor.program_counter += 2

def op_xor_register_to_register(processor, *args):
    processor.register[args[0]] ^= processor.register[args[1]]
    processor.program_counter += 2

def op_left_shift_register(processor, *args):
    result = processor.register[args[0]] << 1
    # Take the 9th bit and assign it to the flag register
    processor.register[0xF] = (result & 0x100) >> 8
    # Assign result to the register without the 9th bit.
    processor.register[args[0]] = result & 0xFF
    processor.program_counter += 2

def op_right_shift_register(processor, *args):
    processor.register[0xF] = processor.register[args[0]] & 0x01
    processor.register[args[0]] >>= 1
    processor.program_counter += 2

def op_set_register_to_random_with_mask(processor, *args):
    processor.register[args[0]] = randint(0,255) & args[1]
    processor.program_counter += 2