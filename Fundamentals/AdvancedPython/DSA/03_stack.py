# implementing stack in python list

class Stack:
    def __init__(self):
        self.elements = []
        ptr = -1
    
    def push(self,element):
        self.elements.append(element)
        ptr += 1
    
    def pop(self):
        if ptr == -1:
            return None
        ptr -= 1
        return self.elements.pop()
    
    def peek(self):
        return self.elements[self.ptr]
    
    def size(self):
        return self.ptr - 1