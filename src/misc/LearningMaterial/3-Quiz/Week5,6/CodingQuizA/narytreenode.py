class NaryTreeNode:
    def __init__(self, val: str, children: 'list[NaryTreeNode | None]'):
        self.val = val
        self.children = children
