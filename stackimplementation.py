class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

# Create a new stack
stack = Stack()

# Push items onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Get the size of the stack
print(stack.size())  # Output: 3

# Peek at the top item
print(stack.peek())  # Output: 30

# Pop items from the stack
print(stack.pop())   # Output: 30
print(stack.pop())   # Output: 20

# Check if the stack is empty
print(stack.is_empty())  # Output: False

# Pop the remaining item
print(stack.pop())   # Output: 10

# Check if the stack is empty
print(stack.is_empty())  # Output: True
