from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def add_left_child(self, value: Any) -> None:
        if self.left_child:
            return
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        if self.right_child:
            return
        self.right_child = BinaryNode(value)

    def is_leaf(self) -> bool:
        if self.left_child or self.right_child is None:
            return False
        return True

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def __str__(self) -> str:
        return str(self.value)


class BinaryTree:
    root: BinaryNode

    def __init__(self, root: 'BinaryNode') -> None:
        self.root = root

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)


root = BinaryNode(10)
root.add_left_child(15)
root.add_right_child(7)
root.traverse_in_order(print)
root.traverse_pre_order(print)
root.traverse_post_order(print)
