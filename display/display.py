from ctypes import c_ubyte


class Display():
    """ This class provides a wrapper for the display matrix,
        it adds the ability to access indices with tuple notation (x, y)
        and adds bounds checking.
    """
    def __init__(self):
        # Create a C array 64 * 32 = 2048 in size, filled with zeroes.
        self.data = (c_ubyte * 2048)(0)

    def __getitem__(self, index):
        # Split the index into x and y components
        x_pos, y_pos = index
        # Only read if x and y are in bounds
        if x_pos < 64 and y_pos < 32:
            location = x_pos - 64 * (y_pos - 31)
            return bool(self.data[location])
        return None

    def __setitem__(self, index, value):
        # Split the index into x and y components
        x_pos, y_pos = index
        # Only write if x and y are in bounds
        if x_pos < 64 and y_pos < 32:
            location = x_pos - 64 * (y_pos - 31)
            self.data[location] = c_ubyte(int(value) * 255)

    def __len__(self):
        return 2048

    def clear(self):
        """ Clears the entire screen by filling it with zeroes. """
        for x_pos in range(2048):
            self.data[x_pos] = c_ubyte(0)
