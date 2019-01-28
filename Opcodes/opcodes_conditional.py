def op_skip_if_register_equal_constant(processor, *args):
    if processor.register[args[0]].value == args[1]:
        processor.program_counter += 4
    else:
        processor.program_counter += 2

def op_skip_if_register_not_equal_constant(processor, *args):
    if processor.register[args[0]].value != args[1]:
        processor.program_counter += 4
    else:
        processor.program_counter += 2

def op_skip_if_register_equal_register(processor, *args):
    if processor.register[args[0]] == processor.register[args[1]]:
        processor.program_counter += 4
    else:
        processor.program_counter += 2

def op_skip_if_register_not_equal_register(processor, *args):
    if processor.register[args[0]] != processor.register[args[1]]:
        processor.program_counter += 4
    else:
        processor.program_counter += 2