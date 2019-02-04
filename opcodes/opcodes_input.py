def op_skip_if_key_pressed(processor, *args):
    processor.program_counter += 2

def op_skip_if_key_not_pressed(processor, *args):
    processor.program_counter += 4

def op_halt_until_key_pressed(processor, *args):
    processor.program_counter += 2