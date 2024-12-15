class Stack:
    def __init__(self, size):
        self.stack_size = size
        self.stack = [None] * size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.stack_size - 1

    def push(self, value):
        if not self.is_full():
            self.top += 1
            self.stack[self.top] = value
        else:
            print("stack is full!")

    def pop(self):
        if not self.is_empty():
            value = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return value
        else:
            print("stack is empty!")

    def peek(self):
        if not self.is_empty():
            return self.stack[self.top]
        else:
            print("stack is empty!")

class Queque_with_stack:
    def __init__(self, size):
        self.size = size
        self.stack1 = Stack(size)
        self.stack2 = Stack(size)

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

    def is_full(self):
        return self.stack1.is_full() and not self.stack2.is_empty()

    def enqueue(self, value):
        if not self.is_full():
            self.stack1.push(value)
            print(f"the value = {value} is enquequed")
        else:
            print("queue is full")

    def dequeue(self):
        if self.is_empty():
            print("there is nothing in queque!")
        else:
            if self.stack2.is_empty():
                while not self.stack1.is_empty():
                    self.stack2.push(self.stack1.pop())
            temple = self.stack2.pop()
            print(f"the value = {temple} is dequeued")
            return temple

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            if self.stack2.is_empty():
                while not self.stack1.is_empty():
                    self.stack2.push(self.stack1.pop())
            print(f"the front item is {self.stack2.peek()}")


o1 = Queque_with_stack(5)
o1.enqueue(10)
o1.enqueue(20)
o1.enqueue(30)
o1.peek()
o1.dequeue()
o1.peek()
