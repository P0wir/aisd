from typing import Any

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self, value: Any):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def append(self, value: Any):
        nod3 = Node(value)
        if self.head is None:
            self.head = nod3
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = nod3

    def node(self, at: int) -> Node:
        temp = self.head
        for x in range(at):
            temp = temp.next
        return temp




    def insert(self, value:Any, after:Node):
        if after is None:
            return
        nod3 = Node(value)
        nod3.next = after.next
        after.next = nod3



    def pop(self):
        temp = self.head
        if temp is not None:
            self.head = temp.next
            temp = None
            return

    def remove_last(self):
        if self.head == None:
            return None
        if self.head.next == None:
            head = None
            return None
        second_last = self.head
        while (second_last.next.next):
            second_last = second_last.next
        second_last.next = None
        return self.head

    def remove(self, after: Node):
        if after is None:
            print("Error")
            return
        temp = after.next.next
        after.next = temp


    def print(self):
        temp = self.head
        while (temp):
            if temp.next is None:
                print(temp.data)
            else:
                print(temp.data, "-> ", end="")
            temp = temp.next

    def len(self):
        length = 0
        temp = self.head
        while (temp):
            length += 1
            temp = temp.next
        return length





lista=LinkedList()
lista.push(3)
lista.push(5)
lista.push('x')
lista.insert(2,lista.head)
lista.append(10)
lista.print()
lista.pop()
lista.remove_last()
lista.remove(lista.head)
lista.print()
