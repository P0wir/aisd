from typing import Any, Callable


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

    def __str__(self) -> str:
        return str(self.value)


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root: 'BinaryNode') -> None:
        self.root = root

    def insert(self, value: Any) -> None:
        if self.root is None:
            self.root = BinaryNode(value)
        if self.root.value < value:
            self.root.right_child = root._insert(value)
        

    # def _insert(self, value: Any) -> BinaryNode:
    #     if self.root is None:
    #         self.root = BinaryNode(value)
    #         return root
    #     else:
    #         if self.root.value == value:
    #             return self.root
    #         elif self.root.value < value:
    #             self.root.right_child = self.insert(value)
    #         else:
    #             self.root.left_child = self.insert(value)


root = BinaryNode(10)
root.add_left_child(7)
root.left_child.add_left_child(3)
root.left_child.left_child.add_left_child(2)
root.add_right_child(15)
korzen = BinarySearchTree(root)
print(korzen)
print(root.min())
korzen.insert(5)
