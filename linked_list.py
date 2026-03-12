#  Linked List
# Linked List prepend Nodes
class Node:
    def __init__(self, number):
        self.number = number
        self.next = None

head = None
for _ in range(3):
   number = int(input("Number: "))
   n = Node(number)
   n.next = head
   head = n # prepend

root = Node(3)