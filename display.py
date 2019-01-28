class Display():
    def __init__(self):
        self.display = [False for x in range(2048)]
    
    def get_pixel(self, x, y):
        if y * 256 + x * 4 < len(self.display):
            return self.display[y * 256 + x * 4]
        return False
    
    def set_pixel(self, x, y, value):
        position = y * 256 + x * 4
        if position < len(self.display):
            self.display[position] = value
    
    def clear_screen(self):
        self.display = [False for x in range(2048)]
    
    def draw(self):
        for y in range(32):
            for x in range(64):
                if self.get_pixel(x, y):
                    print("#", end="")
                else:
                    print(" ", end="")
            print()
    
    def __len__(self):
        return len(self.display)