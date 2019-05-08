import pyglet

def initialize_graphics(processor):
    window = Display(processor, width=640, height=320)
    pyglet.clock.schedule_interval(window.processor_cycle, 1/600)
    pyglet.app.run()

class Display(pyglet.window.Window):
    def __init__(self, processor, *args, **kwargs):
        self.processor = processor
        super(Display, self).__init__(*args, **kwargs)
    
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

    def createTexture(self):
        # Flip each row of pixels so they draw properly.
        pixels = []
        for x in reversed(range(0, len(self.processor.display), 64)):
            pixels.extend(map(lambda x: int(x) * 255, self.processor.display._display[x:x+64]))

        raw_data = (pyglet.gl.GLubyte * len(self.processor.display)) (*pixels)
        image_data = pyglet.image.ImageData(64, 32, 'L', raw_data)
        return image_data.get_texture()
    
    def processor_cycle(self, dt):
        # Since the minimum timer resolution is 1/60 we have to perform
        # (dt * frequency) cycles.
        cycle_defecit = int(dt * 600)
        for _ in range(cycle_defecit):
            self.processor.execute_cycle()
        # Check to ensure processor integrity
        if not self.processor.check_integrity():
            print("Failed integrity check!")
