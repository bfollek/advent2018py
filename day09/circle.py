class Circle:
    def __init__(self):
        """
        First, the marble numbered 0 is placed in the circle... This marble is designated the current marble.
        """
        self._list = [0]
        self._current = 0

    def place(self, val):
        to = self.move(1) + 1
        self._list.insert(to, val)
        self._current = to

    def move(self, n):
        """
        n can be positive or negative
        """
        to = (self._current + n) % len(self._list)
        return to

    def __getitem__(self, i):
        return self._list[i]

    def __delitem__(self, i):
        del self._list[i]

    def __repr__(self):
        return f"Circle({repr(self._list)}, current index: {self._current})"
