from logging import exception

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None  # Points to next node
        self.prev = None  # Points to previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = DoubleNode(value)
        if self.head is None:  # Empty list
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            last = current
            current = current.next
        print("None")

    def display_backward(self):
        # Go to the last node
        current = self.head
        if current is None:
            print("None")
            return
        while current.next:
            current = current.next
        # Traverse backwards
        while current:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")

    def remove(self, value):
            current = self.head
            if current is None: #Si la lista está vacía.
                return Exception("Lista vacía.")
            while current:
                if current.value is value:
                    if current.prev:  # ¿No es el head?
                        current.prev.next = current.next
                    if current.next:  # ¿No es el tail?
                        current.next.prev = current.prev
                    if current is self.head:  # ¿Es el head?
                        self.head = current.next
                    return
                current = current.next


# Example
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(380)
dll.append(35)
dll.display_forward()   # 10 <-> 20 <-> 30 <-> 380 <-> 35 <-> None
dll.remove(30)
dll.display_forward()   # 10 <-> 20 <-> 380 <-> 35 <-> None
