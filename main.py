from processor import Processor
import time

processor = Processor()

with open("game.ch8", "rb") as gamefile:
  game = gamefile.read()
  processor.load_game(game)

while(True):
  for x in range(8):
    processor.execute_cycle()
  if processor.draw_screen:
    processor.display.draw()
    processor.draw_screen = False
    
    