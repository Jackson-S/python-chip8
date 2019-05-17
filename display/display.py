from ctypes import c_ubyte

class Display():
    """ This class provides a wrapper for the display matrix,
        it adds the ability to access indices with tuple notation (x, y)
        and adds bounds checking.
    """
    def __init__(self):
        # Create a 64*32 1-bit display
        self.data = (c_ubyte * 2048) (0)
    
    def __getitem__(self, index):
        # Split the index into x and y components
        x, y = index
        # Only read if x and y are in bounds
        if x < 64 and y < 32:
            location = x - 64 * (y - 31)
            return bool(self.data[location])
    
    def __setitem__(self, index, value):
        # Split the index into x and y components
        x, y = index
        # Only write if x and y are in bounds
        if x < 64 and y < 32:
            location = x - 64 * (y - 31)
            self.data[location] = c_ubyte(int(value) * 255)
    
    def __len__(self):
        return 2048
    
    def clear(self):
        for x in range(2048):
            self.data[x] = c_ubyte(0)
