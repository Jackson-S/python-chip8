import pyglet
from pyglet.window import key

from .keyboard_layout import KEY_MAP

class GlManager(pyglet.window.Window):
    def __init__(self, processor, frequency, *args, **kwargs):
        self.processor = processor
        self.key_map = KEY_MAP
        self.frequency = frequency
        super(GlManager, self).__init__(*args, **kwargs)
        pyglet.clock.get_default().set_fps_limit(60)

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
        if symbol == key.ESCAPE:
            exit(0)
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
        cycle_deficit = int(dt * self.frequency)
        for _ in range(cycle_deficit):
            self.processor.execute_cycle()
        self.processor.timer_tick()