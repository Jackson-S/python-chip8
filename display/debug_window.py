import pyglet

class DebugWindow(pyglet.window.Window):
    def __init__(self, processor, *args, **kwargs):
        self.processor = processor
        super().__init__(*args, **kwargs)

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
        # Convert the pixel array into a GLubyte array for drawing.
        raw_data = (pyglet.gl.GLubyte * len(self.processor.memory)) (*reversed(self.processor.memory))
        # Generate an image from the GLubyte array
        image_data = pyglet.image.ImageData(32, 128, 'L', raw_data)
        # Return the texture created from the image data.
        return image_data.get_texture()