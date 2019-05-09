import pyglet

from .keyboard_layout import KEY_MAP

class GlManager(pyglet.window.Window):
    def __init__(self, processor, *args, **kwargs):
        self.processor = processor
        self.key_map = KEY_MAP
        super(GlManager, self).__init__(*args, **kwargs)
    
    def on_draw(self):
        texture = self.createTexture()

        # Forces the sprite to be scaled nearest neighbour
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, 
                                  pyglet.gl.GL_TEXTURE_MAG_FILTER, 
                                  pyglet.gl.GL_NEAREST)
        
        # Scale the sprite to the window size
        texture.width = self.width
        texture.height = self.height

        # Draw the texture on screen
        texture.blit(0, 0)
        del texture

    def createTexture(self):
        # Flip each row of pixels so they draw properly.
        pixels = []
        for x in reversed(range(0, len(self.processor.display), 64)):
            pixels.extend(map(lambda x: int(x) * 255, self.processor.display._display[x:x+64]))

        # Convert the pixel array into a GLubyte array for drawing.
        raw_data = (pyglet.gl.GLubyte * len(self.processor.display)) (*pixels)
        # Generate an image from the GLubyte array
        image_data = pyglet.image.ImageData(64, 32, 'L', raw_data)
        # Return the texture created from the image data.
        return image_data.get_texture()

    def on_key_press(self, symbol, modifiers):
        try:
            self.processor.key[self.key_map[symbol]] = True
        except KeyError:
            pass
    
    def on_key_release(self, symbol, modifiers):
        try:
            self.processor.key[self.key_map[symbol]] = False
        except KeyError:
            pass
    
    def processor_cycle(self, dt):
        # Since the minimum timer resolution is 1/60 we have to perform
        # (dt * frequency) cycles.
        cycle_deficit = int(dt * 600)
        for _ in range(cycle_deficit):
            self.processor.execute_cycle()

        # Check to ensure processor integrity
        # if not self.processor.check_integrity():
        #     print("Failed integrity check!")

def initialize_graphics(processor, width=640, height=320):
    # Creates the game state and window using pygame.
    window = GlManager(processor, width=width, height=height)
    # Schedule the processor to run at 600hz (slightly higher than standard, 
    # but makes maths and timing code much easier)
    pyglet.clock.schedule_interval(window.processor_cycle, 1/600)
    pyglet.app.run()