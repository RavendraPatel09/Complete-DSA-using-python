class Stack:
    def __init__(self):
        self.stk = []

    def push(self, x):
        self.stk.append(x)

    def pop(self):
        if not self.is_empty():
            return self.stk.pop()
        return "Underflow"
    def peek(self):
        if not self.is_empty():
            return self.stk[-1]
        return "Empty"
    def is_empty(self):
        return len(self.stk) == 0
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.peek())