from processor import Processor
from byte import Chip8Byte as Byte
from display_pyglet import Display

import pyglet

import sys

processor = Processor()
window = Display(processor)

with open(sys.argv[1], "rb") as gamefile:
  game = gamefile.read()
  processor.load_game(game)

def processor_cycle(dt):
  processor.execute_cycle()
  # Debug code
  if not processor.check_integrity():
    print("Failed integrity check!")

def counter_cycle(dt):
  processor.delay_timer.tick()
  processor.sound_timer.tick()

pyglet.clock.schedule_interval(processor_cycle, 1/500)
pyglet.clock.schedule_interval(counter_cycle, 1/60)

pyglet.app.run()
    
    