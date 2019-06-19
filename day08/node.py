class Node:

    INDENT = "  "
    _num_indents = 0

    def __init__(self):
        self.children = []
        self.metadata = []

    def add_child(self, child):
        self.children.append(child)
        return self.children

    def add_metadata(self, metadata):
        self.metadata.append(metadata)
        return self.metadata

    @property
    def total_metadata(self):
        total = sum(self.metadata)
        for c in self.children:
            total += c.total_metadata
        return total

    @classmethod
    def indent(cls, inc=True):
        if inc:
            Node._num_indents += 1
        return Node.INDENT * Node._num_indents

    @classmethod
    def dedent(cls, num=1):
        Node._num_indents -= num
        return Node._num_indents

    def __str__(self):
        s = f"\n{Node.indent()}Node =>"
        s += f"\n{Node.indent()}metadata: {self.metadata}"
        s += f"\n{Node.indent(False)}children"
        if len(self.children):
            s += " =>"
            for c in self.children:
                s += str(c)
        else:
            s += ": []"
        Node.dedent(2)
        return s
