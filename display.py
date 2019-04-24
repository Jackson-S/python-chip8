class Display():
    def __init__(self):
        self._display = [False for x in range(2048)]
        self.draw_screen = True
        self._length = 2048
    
    def __getitem__(self, index):
        if type(index) == tuple:
            index = index[1] * 64 + index[0]
        return self._display[index % 2048]
    
    def __setitem__(self, index, value):
        if type(index) == tuple:
            index = index[1] * 64 + index[0]
        self._display[index % 2048] = value
    
    def __iter__(self):
        index = 0
        while index < self._length:
            yield self._display[index]
            index += 1
    
    def __len__(self):
        return self._length
    
    def clear(self):
        self._display = [False for x in range(2048)]