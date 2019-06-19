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

    @classmethod
    def indent(cls):
        return Node.INDENT * Node._num_indents

    def __str__(self):
        Node._num_indents += 1
        s = f"\n{Node.indent()}Node("
        Node._num_indents += 1
        s += f"\n{Node.indent()}children: "
        for c in self.children:
            s += str(c)
        s += f"\n{Node.indent()}metadata: {self.metadata})"
        Node._num_indents -= 2
        return s
