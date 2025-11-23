class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


# -----------------------
# Testing with inputs
# -----------------------

s = Stack()

# Sample input values
s.push(10)
s.push(20)
s.push(30)
s.push("Hello")
s.push(99)

print("Peek:", s.peek())   # Last pushed value → 99

print("Pop:", s.pop())     # Removes 99
print("Pop:", s.pop())     # Removes "Hello"
print("Pop:", s.pop())     # Removes 30

print("Is Empty:", s.is_empty())  # Should be False

print("Pop:", s.pop())     # Removes 20
print("Pop:", s.pop())     # Removes 10
print("Pop:", s.pop())     # Stack is empty
