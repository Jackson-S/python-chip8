class Chip8Byte():
    def __init__(self, value):
        if type(value) == bytes and len(bytes) == 1:
            self.value = int.from_bytes(value, byteorder="big")
        elif type(value) == Chip8Byte:
            self.value = value.value
        else:      
            self.value = value & 0xFF
    
    def __add__(self, other):
        if type(other) == Chip8Byte:
            return Chip8Byte(self.value + other.value)
        else:
            return Chip8Byte(self.value + other)
    
    def __sub__(self, other):
        if type(other) == Chip8Byte:
            return Chip8Byte(abs(self.value - other.value))
        else:
            return Chip8Byte(abs(self.value - other))

    def __lshift__(self, other):
        if type(other) == Chip8Byte:
            return Chip8Byte(self.value << other.value)
        else:
            return Chip8Byte(self.value << other)

    def __rshift__(self, other):
        if type(other) == Chip8Byte:
            return Chip8Byte(self.value >> other.value)
        else:
            return Chip8Byte(self.value >> other)
    
    def __and__(self, other):
        if type(other) == Chip8Byte:
            return Chip8Byte(self.value & other.value)
        else:
            return Chip8Byte(self.value & other)
    
    def __or__(self, other):
        if type(other) == Chip8Byte:
            return Chip8Byte(self.value | other.value)
        else:
            return Chip8Byte(self.value | other)

    def __xor__(self, other):
        if type(other) == Chip8Byte:
            return Chip8Byte(self.value | other.value)
        else:
            return Chip8Byte(self.value | other)
    
    def __gt__(self, other):
        if type(other) == Chip8Byte:
            return self.value > other.value
        return self.value > other

    def __eq__(self, other):
        if type(other) == Chip8Byte:
            return self.value == other.value
        return self.value == other
    
    def __ge__(self, other):
        if type(other) == Chip8Byte:
            return self.value >= other.value
        return self.value >= other
    
    def __lt__(self, other):
        if type(other) == Chip8Byte:
            return self.value < other.value
        return self.value < other
    
    def __le__(self, other):
        if type(other) == Chip8Byte:
            return self.value <= other.value
        return self.value <= other
    
    def __ne__(self, other):
        if type(other) == Chip8Byte:
            return self.value != other.value
        return self.value != other
    
    def join(self, low):
        return self.value << 8 | low.value

    def hex(self):
        return hex(self.value)
