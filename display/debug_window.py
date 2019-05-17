import pyglet

from pyglet.gl import glTexParameteri, GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST


class DebugWindow(pyglet.window.Window):
    """ Display a debug window, showing a map of the main memory in the emulated processor. """
    def __init__(self, processor, *args, **kwargs):
        self.processor = processor
        super().__init__(*args, **kwargs)

    def on_draw(self):
        """ Called automatically, redraws the debug window. """
        texture = self.create_texture()

        # Forces the sprite to be scaled nearest neighbour
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        # Scale the sprite to the window size
        texture.width = self.width
        texture.height = self.height

        # Draw the texture on screen
        texture.blit(0, 0)
        del texture

    def create_texture(self):
        """ Convert the memory array in the processor into an OpenGL displayable image. """
        # Convert the pixel array into a GLubyte array for drawing.
        memory_size = len(self.processor.memory)
        raw_data = (pyglet.gl.GLubyte * memory_size)(*reversed(self.processor.memory))
        # Generate an image from the GLubyte array
        image_data = pyglet.image.ImageData(32, 128, 'L', raw_data)
        # Return the texture created from the image data.
        return image_data.get_texture()
