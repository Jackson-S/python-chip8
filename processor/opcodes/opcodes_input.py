def op_skip_if_key_pressed(processor, *args):
    if processor.key[processor.register[args[0]]]:
        processor.program_counter += 4
    else:
        processor.program_counter += 2

def op_skip_if_key_not_pressed(processor, *args):
    if processor.key[processor.register[args[0]]]:
        processor.program_counter += 2
    else:
        processor.program_counter += 4

def op_halt_until_key_pressed(processor, *args):
    if processor.key[processor.register[args[0]]]:
        processor.program_counter += 2