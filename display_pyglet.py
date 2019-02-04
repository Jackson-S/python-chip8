import pyglet

class Display(pyglet.window.Window):
    def __init__(self, processor, *args, **kwargs):
        self.processor = processor
        self.previous_frame = None
        super(Display, self).__init__(*args, *kwargs)
    
    def on_draw(self):
        self.clear()
        if self.processor.display.draw_screen:
            if self.previous_frame:
                self.previous_frame.delete()
            sprite = self.create_sprite()
            sprite.update(x=0, y=self.height, scale = self.width // 64, scale_y=-1)
            self.previous_frame = sprite
            sprite.draw()
            self.processor.display.draw_screen = False
        else:
            self.previous_frame.draw()
            
    
    def create_sprite(self):
        pixels = [int(x) * 255 for x in self.processor.display]
        raw_data = (pyglet.gl.GLubyte * len(pixels))(*pixels)
        image_data = pyglet.image.ImageData(64, 32, 'L', raw_data)
        return pyglet.sprite.Sprite(image_data)
