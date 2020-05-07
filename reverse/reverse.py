class Node:
    def __init__(self, value=None, next_node=None):
        # Value at this linked list node
        self.value = value
        # Reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # Set this node's next_node reference to the node passed in 
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # Reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # Reference of current node
        current = self.head
        # Check if node is valid
        while current:
            # Return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # Update our current node to the current node's next node
            current = current.get_next()
        # When failed return False
        return False

    def reverse_list(self):  # O(n)
        prev = None
        curr = self.head
        while curr:
            next = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = next
        self.head = prev