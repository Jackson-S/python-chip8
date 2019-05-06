def op_display_clear(processor, *args):
    processor.display.clear()
    processor.display.draw_screen = True
    processor.program_counter += 2

def op_draw(processor, *args):
    x_origin = processor.register[args[0]].value % 64
    y_origin = processor.register[args[1]].value % 32
    sprite_height = args[2]

    # Reset the flag register so that it can be changed later
    processor.register[0xF].value = 0

    for sprite_y in range(sprite_height):
        if (y_origin + sprite_y < 32):
            # Chip-8 pixels are stored as 1-bit values in groups of 8. This reads the
            # group of 8 and creates a map object that will iterate through the sprite
            # pixel by pixel.
            sprite_line = processor.memory[processor.immediate + sprite_y]
            sprite_bits = map(lambda x: bool(sprite_line & (1 << x)), reversed(range(8)))

            for sprite_x, pixel in enumerate(sprite_bits):
                if (x_origin + sprite_x < 64):
                    # Add the original x and y positions to the current sprite x, y
                    position = (x_origin + sprite_x, y_origin + sprite_y)

                    old_pixel = processor.display[position]
                    new_pixel = pixel ^ old_pixel
                    processor.display[position] = new_pixel

                    # Set the 0xF (flag) register if a pixel is unset.
                    if old_pixel == True and new_pixel == False:
                        processor.register[0xF].value = 1
    
    # Mark that the screen should be updated.
    processor.display.draw_screen = True
    processor.program_counter += 2