def op_return(processor, *args):
    result = processor.stack.pop()
    processor.program_counter = result + 2


def op_goto(processor, *args):
    processor.program_counter = args[0]


def op_call_subroutine(processor, *args):
    processor.stack.append(processor.program_counter)
    processor.program_counter = args[0]


def op_goto_address_plus_register_zero(processor, *args):
    processor.program_counter = args[0] + processor.register[0]


def op_nop(processor, *args):
    pass
