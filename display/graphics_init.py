import pyglet

from .gl_manager import GlManager
from .debug_display import DebugDisplay

def initialize_graphics(processor, speed, debug=False, width=640, height=320):
    # Creates the game state and window using pygame.
    game_window = GlManager(processor, speed, width=width, height=height)
    if debug:
        memory_layout = DebugDisplay(processor, width=160, height=640)
    # Schedule the processor to run at 600hz (slightly higher than standard, 
    # but makes maths and timing code much easier)
    pyglet.clock.schedule_interval(game_window.processor_cycle, 1/500)
    pyglet.app.run()