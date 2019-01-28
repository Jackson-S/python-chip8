class Chip8Byte():
    def __init__(self, value):
        if type(value) == bytes and len(bytes) == 1:
            self.value = int.from_bytes(value, byteorder="little")
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
        return self.__cmp__(other)

    def __cmp__(self, other):
        if type(other) == Chip8Byte:
            return other.value - self.value
        else:
            return Chip8Byte(other).value - self.value
    
    def join(self, low):
        return self.value << 8 | low.value

    def hex(self):
        return hex(self.value)
