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

    def add_left_child(self, value: Any) -> None:
        if self.left_child:
            return
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        if self.right_child:
            return
        self.right_child = BinaryNode(value)

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

    def __insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node:
            if value < node.value:
                node.left_child = self.__insert(node.left_child, value)
            else:
                node.right_child = self.__insert(node.right_child, value)
        else:
            node = BinaryNode(value)
        return node

    def insert(self, value: Any) -> None:
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root = self.__insert(self.root, value)

    def insert_list(self, list_: List[Any]) -> None:
        for i in list_:
            self.insert(i)

    def remove(self, value: Any) -> None:
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root = self.__remove(self.root, value)

    def show(self) -> None:
        self.root.show().render(filename='bst', view=True)


root = BinaryNode(10)
korzen = BinarySearchTree(root)
print(korzen)
korzen.insert_list([11,15,1,2,5,7,3,8,21,4,16,36,12])
korzen.show()

print(korzen)
