class Timer():
    def __init__(self):
        self.value = 0
    
    def tick(self):
        if self.value != 0:
            self.value -= 1
    
    def set(self, value):
        self.value = value & 0xFF