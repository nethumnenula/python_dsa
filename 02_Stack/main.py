from stack import Stack

number = Stack()


try:
    # number.push(2)
    # number.peek()
    number.pop()
except IndexError as e:
    print(f"{e}")
