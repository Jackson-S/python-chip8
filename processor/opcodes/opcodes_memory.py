def op_set_immediate_to_constant(processor, *args):
    processor.immediate = args[0]
    processor.program_counter += 2

def op_add_register_to_immediate(processor, *args):
    processor.immediate += processor.register[args[0]]
    processor.program_counter += 2

def op_set_immediate_to_sprite_address(processor, *args):
    processor.immediate = processor.register[args[0]] * 5
    processor.program_counter += 2

def op_memory_at_immediate_to_binary_coded_decimal(processor, *args):
    number = processor.register[args[0]]
    for x in reversed(range(3)):
        # Destroy any opcode objects that may have been created
        processor.program_memory[processor.immediate + x] = None
        processor.memory[processor.immediate + x] = number % 10
        number //= 10
    processor.program_counter += 2

def op_dump_registers_to_memory(processor, *args):
    for i in range(args[0] + 1):
        processor.program_memory[processor.immediate + i] = None
        processor.memory[processor.immediate + i] = processor.register[i]
    processor.program_counter += 2

def op_load_registers_from_memory(processor, *args):
    for i in range(args[0] + 1):
       processor.register[i] = processor.memory[processor.immediate + i]
    processor.program_counter += 2