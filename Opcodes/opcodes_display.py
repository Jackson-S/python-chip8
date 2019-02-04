def op_display_clear(processor, *args):
    processor.display.clear()
    processor.display.draw_screen = True
    processor.program_counter += 2

def op_draw(processor, *args):
    x_pos = processor.register[args[0]].value
    y_pos = processor.register[args[1]].value
    height = args[2]

    for y in range(height):
        # Get the str rep. of the sprite binary (eg 0b1000110) and remove '0b'
        sprite_line = bin(processor.memory[processor.immediate + y].value)[2:]
        sprite_bits = map(lambda x: int(x), sprite_line)
        for x, pixel in enumerate(sprite_bits):
            position = x_pos + x, y_pos + y
            
            new_pixel = processor.display[position] ^ pixel
            
            processor.register[0xF].value = new_pixel
            processor.display[position] = bool(new_pixel)
    
    processor.display.draw_screen = True
    processor.program_counter += 2