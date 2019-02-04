from random import randint

def op_assign_constant_to_register(processor, *args):
    processor.register[args[0]].value = args[1]
    processor.program_counter += 2

def op_add_constant_to_register(processor, *args):
    processor.register[args[0]] += args[1]
    processor.program_counter += 2

def op_assign_register_to_register(processor, *args):
    processor.register[args[0]] = processor.register[args[1]]
    processor.program_counter += 2

def op_add_register_to_register(processor, *args):
    temp = processor.register[args[0]]
    processor.register[args[0]] += processor.register[args[1]]
    processor.register[0xF].value = int(temp > processor.register[args[0]])
    processor.program_counter += 2

def op_sub_register_to_register(processor, *args):
    flag = processor.register[args[0]] > processor.register[args[1]]
    processor.register[0xF].value = int(flag)
    processor.register[args[0]] -= processor.register[args[1]]
    processor.program_counter += 2

def op_sub_reverse_register_to_register(processor, *args):
    flag = processor.register[args[1]] > processor.register[args[0]]
    processor.register[0xF].value = int(flag)
    processor.register[args[0]] = processor.register[args[1]] - processor.register[args[0]]
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
    processor.register[0xF] = (processor.register[args[0]] & 0x80) >> 7
    processor.register[args[0]] <<= 1
    processor.program_counter += 2

def op_right_shift_register(processor, *args):
    processor.register[0xF] = processor.register[args[0]] & 0x01
    processor.register[args[0]] >>= 1
    processor.program_counter += 2

def op_set_register_to_random_with_mask(processor, *args):
    processor.register[args[0]].value = randint(0,255) & args[1]
    processor.program_counter += 2