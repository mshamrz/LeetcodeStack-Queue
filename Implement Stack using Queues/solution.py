class Queue:
    def __init__(self):
        self.data = []
    def push(self, x):
        self.data.append(x)
    def pop(self):
        if self.empty():
            raise IndexError('pop from empty queue')
        return self.data.pop(0)
    def peek(self):
        if self.empty():
            raise IndexError('peek from empty queue')
        return self.data[0]
    def empty(self):
        return len(self.data) == 0

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


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
