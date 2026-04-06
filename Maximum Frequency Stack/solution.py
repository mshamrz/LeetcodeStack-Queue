class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
    def get_data(self):
        return self._data
    def get_next(self):
        return self._next
    def set_next(self, node):
        self._next = node
class Stack:
    def __init__(self):
        self._head = None
        self._top = None
    def push(self, x):
        node = Node(x)
        node.set_next(self._head)
        self._head = node
        self._top = x
    def pop(self):
        value = self._top
        self._head = self._head.get_next()
        self._top = self._head.get_data() if self._head else None
        return value
    def top(self):
        return self._top
    def empty(self):
        return self._head is None

class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.maxfreq = 0
    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        f = self.freq[val]
        if f not in self.group:
            self.group[f] = Stack()
        self.group[f].push(val)
        if f > self.maxfreq:
            self.maxfreq = f

    def pop(self) -> int:
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if self.group[self.maxfreq].empty():
            self.maxfreq -= 1
        return val
