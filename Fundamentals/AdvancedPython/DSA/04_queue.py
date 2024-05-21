class Queue:
    def __init__(self):
        self.elements = []
        self.top = -1
        self.end = -1

    def insert(self,num):
        if self.top == -1 and self.end == -1:
            self.top = 0
            self.end = 0
            self.elements.append(num)
        
        else:
            self.end += 1
            self.elements.append(num)
    
    def pop(self,num):
        if self.top == -1 and self.end == -1:
            return None
        
        elif self.top == 0 and self.end == 0:
            self.top = -1
            self.end = -1
            return self.elements[self.top]
        
        else:
            top += 1
            return self.elements[self.top]