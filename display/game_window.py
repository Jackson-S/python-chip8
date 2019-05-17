import pyglet
from pyglet.gl import glTexParameteri, GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST
from pyglet.window import key

from .keyboard_layout import KEY_MAP

class GameWindow(pyglet.window.Window):
    def __init__(self, processor, frequency, *args, **kwargs):
        self.processor = processor
        self.frequency = frequency
        super().__init__(*args, **kwargs)

    def on_draw(self):
        image_data = pyglet.image.ImageData(64, 32, "L", self.processor.display.data)
        texture = image_data.get_texture()

        # Forces the sprite to be scaled nearest neighbour
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        # Scale the sprite to the window size
        texture.width = self.width
        texture.height = self.height

        # Draw the texture on screen
        texture.blit(0, 0)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            exit(0)
        try:
            self.processor.key[KEY_MAP[symbol]] = True
        except KeyError:
            pass
    
    def on_key_release(self, symbol, modifiers):
        try:
            self.processor.key[KEY_MAP[symbol]] = False
        except KeyError:
            pass
    
    def processor_cycle(self, dt):
        # Since the minimum timer resolution is 1/60 we have to perform
        # (dt * frequency) cycles.
        cycle_deficit = int(dt * self.frequency)
        for _ in range(cycle_deficit):
            self.processor.execute_cycle()
        self.processor.timer_tick()