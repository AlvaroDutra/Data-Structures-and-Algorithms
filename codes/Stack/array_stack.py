class Stack:
    def __init__(self, max_lenght=1000):
        self.items = [0] * max_lenght
        self.max_lenght = max_lenght
        self.pointer = 0

    def push(self, item):
        if self.pointer >= self.max_lenght:
            raise IndexError("Stack Overflow")
        
        self.items[self.pointer] = item
        self.pointer += 1

    def pop(self):
        if self.pointer == 0:
            raise IndexError("Empty list")
        
        self.pointer -= 1
        return self.items[self.pointer]
    
    def peek(self):
        if self.pointer == 0:
            raise IndexError("Empty list")
        return self.items[self.pointer - 1]

    def size(self):
        return self.pointer