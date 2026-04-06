class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self._head = None
        self._size = 0
    def push(self, data):
        node = Node(data)
        node.next = self._head
        self._head = node
        self._size += 1
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self._head.data
        self._head = self._head.next
        self._size -= 1
        return value
    def is_empty(self):
        return self._head is None
    def peek(self):
        if self.is_empty():
            raise IndexError('peek from empty stack')
        return self._head.data
    def size(self):
        return self._size

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
