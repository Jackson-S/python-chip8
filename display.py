class Display():
    def __init__(self):
        self._display = [False for x in range(2048)]
        self.draw_screen = True
        self._length = 2048
    
    def __getitem__(self, index):
        # Index is a single number
        if type(index) == int:
            return self._display[index]

        # Index is a tuple e.g. (1, 1)
        elif type(index) == tuple:
            return self._display[index[1] * 64 + index[0]]
    
    def __setitem__(self, index, value):
        if type(index) == int:
            self._display[index] = value
        elif type(index) == tuple:
            self._display[index[1] * 64 + index[0]] = value
    
    def __iter__(self):
        index = 0
        while index < self._length:
            yield self._display[index]
            index += 1
    
    def clear(self):
        self._display = [False for x in range(2048)]
    
    def draw(self):
        for y in range(32):
            for x in range(64):
                if self[x, y]:
                    print("#", end="")
                else:
                    print(" ", end="")
            print()
    
    def __len__(self):
        return self._length