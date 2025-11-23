class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


# -----------------------
# Test the Queue
# -----------------------
q = Queue()

# Sample input values
q.enqueue(5)
q.enqueue(15)
q.enqueue(25)
q.enqueue(35)
q.enqueue(45)

print("Dequeue:", q.dequeue())   # 5
print("Dequeue:", q.dequeue())   # 15
print("Is Empty:", q.is_empty()) # False
print("Dequeue:", q.dequeue())   # 25
print("Dequeue:", q.dequeue())   # 35
print("Dequeue:", q.dequeue())   # 45
print("Dequeue:", q.dequeue())   # Queue is empty
