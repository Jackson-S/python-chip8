def op_display_clear(processor, *args):
    processor.display.clear()
    processor.display.draw_screen = True
    processor.program_counter += 2

def op_draw(processor, *args):
    x_pos = processor.register[args[0]].value
    y_pos = processor.register[args[1]].value
    height = args[2]
    processor.register[0xF].value = 0

    for y in range(height):
        sprite_line = processor.memory[processor.immediate + y].value
        sprite_bits = (bool(sprite_line & (1 << x)) for x in reversed(range(8)))

        for x, pixel in enumerate(sprite_bits):
            position = (x_pos + x, y_pos + y)

            old_pixel = processor.display[position]
            processor.display[position] ^= pixel

            if processor.display[position] != old_pixel and old_pixel == True:
                processor.register[0xF].value = 1
    
    processor.display.draw_screen = True
    processor.program_counter += 2