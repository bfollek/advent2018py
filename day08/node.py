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

    @property
    def value(self):
        return self._value()

    def _value(self):
        """
        If a node has no child nodes, its value is the sum of its metadata entries.

        However, if a node does have child nodes, the metadata entries become indexes
        which refer to those child nodes. The value of this node is the sum of the
        values of the child nodes referenced by the metadata entries.
        """
        if not self.children:
            return sum(self.metadata)
        valid_children = self._valid_metachildren()
        return sum(map(Node._value, valid_children))

    def _valid_metachildren(self):
        """
        A metadata entry of 1 refers to the first child node, 2 to the second, 3 to
        the third, and so on. If a referenced child node does not exist, that
        reference is skipped. A child node can be referenced multiple times and
        counts each time it is referenced. A metadata entry of 0 does not refer to
        any child node.
        """
        valid = []
        for i in self.metadata:
            if len(self.children) >= i > 0:
                # metadata values start at 1, not 0
                valid.append(self.children[i - 1])
        return valid

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
