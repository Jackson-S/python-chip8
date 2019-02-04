from function_map import functions

def decode(opcode):
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