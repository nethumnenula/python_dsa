from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")

        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from a empty stack")
        print(f"{self.top.data}")

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.size