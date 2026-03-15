data = 50
class Stack:
    def __init__(self):
        self.number = []
        self.size = 0
    
    def push(self, int):
        if self.size < data:
            self.number.append(int)
            self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.number.pop()
        return None
    
    def __str__(self):
        return str(self.number)
    
    def __len__(self):
        return self.size
    
if __name__ == '__main__': 
    s = Stack()

    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)

    print(s)
    print(len(s))

    print(s.pop())
    print(s)
    