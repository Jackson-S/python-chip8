def op_set_immediate_to_constant(processor, *args):
    processor.immediate = args[0]
    processor.program_counter += 2

def op_add_register_to_immediate(processor, *args):
    processor.immediate += processor.register[args[0]].value
    processor.program_counter += 2

def op_set_immediate_to_sprite_address(processor, *args):
    processor.immediate = processor.register[args[0]].value * 5
    processor.program_counter += 2

def op_memory_at_immediate_to_binary_coded_decimal(processor, *args):
    processor.memory[processor.immediate].value = int(processor.register[args[0]].value // 100)
    processor.memory[processor.immediate + 1].value = int((processor.register[args[0]].value / 10) % 10)
    processor.memory[processor.immediate + 2].value = int((processor.register[args[0]].value % 100) // 1)
    processor.program_counter += 2

def op_dump_registers_to_memory(processor, *args):
    for i in range(args[0] + 1):
        processor.memory[processor.immediate + i] = processor.register[i]
    processor.program_counter += 2

def op_load_registers_from_memory(processor, *args):
    for i in range(args[0] + 1):
       processor.register[i] = processor.memory[processor.immediate + i]
    processor.program_counter += 2