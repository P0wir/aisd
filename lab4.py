from typing import Any, List, Callable


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, data):
        self.data = data
        self.children = []

    def is_leaf(self) -> bool:
        if len(self.children) != 0:
            return False
        elif len(self.children) == 0:
            return True

    def add(self, node):
        self.children.append(node)

    def for_each_deep_first(visit: Callable[['TreeNode'], None]) -> None:



root = TreeNode(1)
leaf = TreeNode(6)
leaf2 = TreeNode(9)

TreeNode.add(root, leaf)
TreeNode.add(leaf, leaf2)
print(TreeNode.is_leaf(root))
print(TreeNode.is_leaf(leaf))
print(TreeNode.is_leaf(leaf2))
