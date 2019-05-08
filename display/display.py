class Display():
    def __init__(self):
        self._display = [False for x in range(2048)]
        self.draw_screen = True
        self._length = 2048
    
    def __getitem__(self, index):
        # Split the index into x and y components
        x, y = index
        # Only read if x and y are in bounds
        if x < 64 and y < 32:
            return self._display[y * 64 + x]
    
    def __setitem__(self, index, value):
        # Split the index into x and y components
        x, y = index
        # Only write if x and y are in bounds
        if x < 64 and y < 32:
            self._display[y * 64 + x] = value
    
    def __iter__(self):
        index = 0
        while index < self._length:
            yield self._display[index]
            index += 1
    
    def __len__(self):
        return self._length
    
    def clear(self):
        self._display = [False for x in range(2048)]