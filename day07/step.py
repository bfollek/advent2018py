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


# -------------------------------------------------------------------


class TimedStep(Step):
    def start(self, time_now):
        """
        Each step takes 60 seconds plus an amount corresponding to its letter: A=1, B=2, C=3, and so on.
        So, step A takes 60+1=61 seconds, while step Z takes 60+26=86 seconds. No time is required between steps.
        """
        self._completion_time = ord(self.name) - ord("A") + 61 + time_now

    def completed(self, time_now):
        return self._completion_time <= time_now
