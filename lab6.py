from __future__ import annotations
from graphviz import *
from typing import Any, Callable, List


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def min(self):
        temp = self
        while temp.left_child is not None:
            temp = temp.left_child
        return temp


    def show(self, g=Digraph('g')):
        g.node(str(self), str(self.value))
        if self.left_child:
            g.edge(str(self), str(self.left_child))
            self.left_child.show(g)
        if self.right_child:
            g.edge(str(self), str(self.right_child))
            self.right_child.show(g)
        return g

    def __str__(self) -> str:
        return str(self.value)


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root: 'BinaryNode') -> None:
        self.root = root

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node:
            if value < node.value:
                node.left_child = self._insert(node.left_child, value)
            else:
                node.right_child = self._insert(node.right_child, value)
        else:
            node = BinaryNode(value)
        return node

    def insert(self, value: Any) -> None:
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root = self._insert(self.root, value)

    def insert_list(self, list_: List[Any]) -> None:
        for i in list_:
            self.insert(i)

    def contains(self, value: Any) -> bool:
        if self.root is None:
            return False
        while self.root is not None:
            if self.root.value == value:
                return True
            elif self.root.value < value:
                self.root = self.root.right_child
            elif self.root.value > value:
                self.root = self.root.left_child
        return False

    def remove(self, value: Any) -> None:
        if self.contains(value):
            self.root = self._remove(self.root, value)

    def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value == node.value:
            if node.left_child and node.right_child:
                node.value = node.right_child.min().value
                node.right_child = self._remove(node.right_child, node.right_child.min().value)
            elif node.left_child:
                node = node.left_child
            elif node.right_child:
                node = node.right_child
            else:
                node = None
        elif node.value < value:
            node.right_child = self._remove(node.right_child, value)
        elif node.value > value:
            node.left_child = self._remove(node.left_child, value)
        return node

    def show(self) -> None:
        self.root.show().render(filename='bst',format='png', view=True)


root = BinaryNode(10)
korzen = BinarySearchTree(root)
print(korzen)
korzen.insert_list([11, 15, 1, 2, 5, 7, 3, 8, 21, 4, 16, 36, 12])
korzen.show()
korzen.remove(10)
print(korzen)
print(korzen.contains(11))
