class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def push(self, x):
        node = Node(x)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1
    def pop(self):
        if self.empty():
            raise IndexError('pop from empty queue')
        value = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return value
    def peek(self):
        if self.empty():
            raise IndexError('peek from empty queue')
        return self._head.data
    def empty(self):
        return self._head is None

class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        self.queue2.push(x)
        while not self.queue1.empty():
            self.queue2.push(self.queue1.pop())
        self.queue1, self.queue2 = self.queue2, self.queue1
 
    def pop(self) -> int:
        return self.queue1.pop()

    def top(self) -> int:
        return self.queue1.peek()

    def empty(self) -> bool:
        return self.queue1.empty()

# param_3 = obj.top()
# param_4 = obj.empty()
