def op_set_register_to_delay_timer(processor, *args):
    processor.register[args[0]] = processor.delay_timer
    processor.program_counter += 2

def op_set_delay_timer_to_register(processor, *args):
    processor.delay_timer = processor.register[args[0]]
    processor.program_counter += 2

def op_set_sound_timer_to_register(processor, *args):
    processor.sound_timer = processor.register[args[0]]
    processor.program_counter += 2