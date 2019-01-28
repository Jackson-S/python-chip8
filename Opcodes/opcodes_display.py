def op_display_clear(processor, *args):
    processor.display.clear_screen()
    processor.draw_screen = True
    processor.program_counter += 2

def op_draw(processor, *args):
    x_pos = processor.register[args[0]].value
    y_pos = processor.register[args[1]].value
    height = args[2]

    processor.register[0xF].value = 0

    for y in range(height):
        pixel = processor.memory[processor.immediate + y].value
        for x in range(8):
            if pixel & (0x80 >> x) != 0:
                position = (x_pos + x + (y_pos + y) * 64)

                if position < len(processor.display):
                    if processor.display.get_pixel(x_pos + x, y_pos + y) != True:
                        processor.register[0xF].value = 1
                    
                    value = processor.display.get_pixel(x_pos + x, y_pos + y) ^ True

                    processor.display.set_pixel(x_pos + x, y_pos + y, value)
    
    processor.draw_screen = True
    processor.program_counter += 2