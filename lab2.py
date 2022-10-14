# class House:
#     color: str
#     window_count: int
#
#     def __init__(self, color: str, window_count: int) -> None:
#         self.color = color
#         self.window_count = window_count
#
#     def get_color(self) -> str:
#         return f'elewacja budynku jest koloru: {self.color}'
#
#     def add_windows(self, amount: int) -> None:
#         self.window_count += amount
#
#     def _private_method(self) -> None:
#         print("akopfjaopfa")
#
#
#
#
#
# house_1 = House('blue', 10)
# house_2 = House('pink', 21)
# house_1._private_method()
#
# print(f' dom nr 1 ma {house_1.window_count} okien')
# print(f' dom nr 2 ma {house_2.window_count} okien')
#
# house_2.add_windows(3)
# print(f' dom nr 1 ma {house_1.window_count} okien')
# print(f' dom nr 2 ma {house_2.window_count} okien')
#
# print(house_1.get_color())
# print(house_2.get_color())
#
# house_1.color = 'afroamerican'
#
# print(house_1.get_color())
# print(house_2.get_color())

#zad 1

from typing import Any

class Node:
    value: Any
    next: 'Node'

class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head: Node

 def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
