from functools import total_ordering


@total_ordering
class Step:
    def __init__(self, name):
        self._name = name.strip().upper()

    @property
    def name(self):
        return self._name

    def str(self):
        return self.name

    def __eq__(self, other):
        """For sorting and the `in` operator."""
        return self.name == other.name

    def __lt__(self, other):
        """For sorting."""
        return self.name < other.name

    def __hash__(self):
        """For dicts and sets."""
        return hash(repr(self))

    def __repr__(self):
        return f'Step(name="{self.name}")'
