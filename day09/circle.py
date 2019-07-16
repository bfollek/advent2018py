from data_structures.circular_doubly_linked_list.cdll import (
    CircularDoublyLinkedList,
    Node,
)


class Circle:
    def __init__(self):
        """
        First, the marble numbered 0 is placed in the circle... This marble is designated the current marble.
        """
        self._data = CircularDoublyLinkedList()
        node = Node(0)
        self._data.insert_at_beg(node)
        self.current = node

    def move(self, n):
        """
        Move n positions around the circle. n can be positive (clockwise) or negative (counter-clockwise).
        Return the node at the new position.
        """
        node = self.current
        while n:
            if n > 0:
                node = node.next
                n -= 1
            else:
                node = node.prev
                n += 1
        return node

    def place(self, val):
        node = Node(val)
        to = self.move(1)
        self._data.insert_after(to, node)
        self.current = node

    @property
    def data(self):
        return self._data.to_list()

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value

    def remove(self, node):
        self._data.remove(node)
        # Make sure current stays valid.
        # Did we remove the only node, or the current node?
        if self._data.first == None:
            self.current = None
        elif self.current == node:
            self.current = node.next

    def __repr__(self):
        return f"Circle(data: {repr(self._data)}, current node: {self.current.data})"
