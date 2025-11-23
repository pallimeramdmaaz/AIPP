# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly Linked List class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Display the linked list
    def display(self):
        current = self.head
        if current is None:
            print("Linked list is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# -----------------------
# Test the linked list
# -----------------------
ll = SinglyLinkedList()

# Insert values at the beginning
ll.insert_at_beginning(3)
ll.insert_at_beginning(1)

# Insert values at the end
ll.insert_at_end(5)
ll.insert_at_end(7)
ll.insert_at_end(9)

# Display the linked list
ll.display()
