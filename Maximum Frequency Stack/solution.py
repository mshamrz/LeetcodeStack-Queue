class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0
from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(Stack)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].push(val)
        if self.freq[val] > self.maxfreq:
            self.maxfreq = self.freq[val]

    def pop(self) -> int:
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if self.group[self.maxfreq].empty():
            self.maxfreq -= 1
        return val
