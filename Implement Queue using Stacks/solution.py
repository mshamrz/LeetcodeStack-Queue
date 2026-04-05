class Stack:
    def __init__(self):
        self.data = []
    def push(self, data):
        self.data.append(data)
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.data.pop()
    def is_empty(self):
        return len(self.data) == 0
    def peek(self):
        if self.is_empty():
            raise IndexError('peek from empty stack')
        return self.data[-1]
    def size(self):
        return len(self.data)

class MyQueue:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def push(self, x: int) -> None:
        self.in_stack.push(x)

    def pop(self) -> int:
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()
    def peek(self) -> int:
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.peek()
        
    def empty(self) -> bool:
        return self.in_stack.is_empty() and self.out_stack.is_empty()
