class Circle:
    def __init__(self):
        """
        First, the marble numbered 0 is placed in the circle... This marble is designated the current marble.
        """
        self._list = [0]
        self.current = 0

    def place(self, val):
        to, _ = self.move(1)
        to += 1
        self._list.insert(to, val)
        self.current = to

    def move(self, n):
        """
        Move n positions around the circle. n can be positive (clockwise) or negative (counter-clockwise).
        Return a tuple of the new position and the value there.
        """
        pos = (self.current + n) % len(self._list)
        return (pos, self._list[pos])

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value

    def __delitem__(self, i):
        del self._list[i]

    def __repr__(self):
        return f"Circle({repr(self._list)}, current index: {self.current})"
