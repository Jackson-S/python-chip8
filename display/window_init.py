import pyglet

from .game_window import GameWindow
from .debug_window import DebugWindow


def initialize_windows(processor, key_map, arguments):
    """ Initializes the game window and the debug window if required. """
    # Creates the game state and window using pyglet.
    width, height = arguments.size
    game_window = GameWindow(processor, arguments.frequency, key_map, width, height)
    pyglet.clock.schedule_interval(game_window.processor_cycle, 1/500)

    if arguments.debug:
        DebugWindow(processor, width=160, height=640)

    pyglet.app.run()
