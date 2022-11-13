from typing import Any, List, Callable, Union
from lab import Queue
import graphviz

dot = graphviz.Digraph('TreeNode')

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value: Any):
        self.value = value
        self.children = []

    def is_leaf(self) -> bool:
        if len(self.children) != 0:
            return False
        elif len(self.children) == 0:
            return True

    def add(self, node):
        self.children.append(node)

    def for_each_deep_first(self, visit:Callable[['TreeNode'], None]) -> None:
        visit(self)
        for x in self.children:
            x.for_each_deep_first(visit)


    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        queue = Queue()
        queue.dequeue()
        queue.enqueue(self)
        while queue.len() != 0:
            y = queue.peek()
            queue.dequeue()
            visit(y)
            for x in range(len(y.children)):
                queue.enqueue(y.children[x])

    def show(self, dot):
        dot.node(str(self.value))
        for x in self.children:
            dot.edge(str(self.value), str(x.value))
            x.show(dot)
        return dot

    def search(self, value:Any)-> Union['TreeNode', None]:
        queue = Queue()
        queue.dequeue()
        queue.enqueue(self)
        y = queue.peek()
        while queue.len() != 0:
            y = queue.peek()
            if(y.value == value):
                return "element znajduje sie w drzewie"
            queue.dequeue()
            for x in range(len(y.children)):
                queue.enqueue(y.children[x])
        return "Taki element nie znajduje sie w drzewie"


f = print
def print(address:'TreeNode')->None:
    if isinstance(address, TreeNode):
        f(address.value)
    else:
        f(address)

class Tree:
    root: TreeNode

    def __init__(self, TreeNode):
        self.root:'TreeNode' = TreeNode

    def add(self, value: Any, parent_name: Any) -> None:
        parent_name.children.append(TreeNode(value))

    def for_each_deep_first(self, visit:Callable[['TreeNode'], None]) -> None:
        visit(self)
        for x in self.root.children:
            x.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        queue = Queue()
        queue.dequeue()
        queue.enqueue(self)
        while queue.len() > 0:
            y = queue.peek()
            queue.dequeue()
            visit(y)
            for x in range(len(y.children)):
                queue.enqueue(y.children[x])





root = TreeNode("F")
leaf = TreeNode("B")
leaf2 = TreeNode("G")
leaf3 = TreeNode("A")
leaf4 = TreeNode("D")
leaf5 = TreeNode("I")
leaf6 = TreeNode("C")
leaf7 = TreeNode("E")
leaf8 = TreeNode("H")


TreeNode.add(root, leaf)
TreeNode.add(root, leaf2)
TreeNode.add(leaf, leaf3)
TreeNode.add(leaf, leaf4)
TreeNode.add(leaf2, leaf5)
TreeNode.add(leaf5, leaf8)
TreeNode.add(leaf4, leaf6)
TreeNode.add(leaf4, leaf7)
print(root.is_leaf())
print(leaf8.is_leaf())
root.for_each_deep_first(print)
print("..........")
root.for_each_level_order(print)

tree=Tree(root)
print("..............")
print(root.search("H"))
root.show(dot).render(directory='doctest-output')
