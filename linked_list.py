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

# Print using while loop
ptr = head
while ptr is not None:
    print(ptr.number, end=' -> ')
    ptr = ptr.next
print('None\n')

# Linked list -- Append Nodes
class Node:
    def __init__(self, number):
        self.number = number
        self.next = None

head = None
for _ in range(3):
    number = int(input("Number: "))
    n = Node(number)

    if head is None:
        head = n
    else:
        ptr = head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = n # append to end
        
# Print
ptr = head
while ptr is not None:
    print(ptr.number, end=' -> ')
    ptr = ptr.next
print('None\n')

# Linked List - Sorted Insert
class Node:
    def __init__(self, number):
        self.number = number
        self.next = None

head = None
for _ in range(3):
    number = int(input("Number: "))
    n = Node(number)

    if head is None:
        head = n
    elif n.number > head.number:
        n.next = head
        head = n
    else:
        ptr = head
        while ptr.next is not None:
            if n.number < ptr.next.number:
                n.next = ptr.next
                ptr.next = n
                break
            ptr = ptr.next
        else:
            ptr.next = n # append at end

# Print
ptr = head
while ptr is not None:
    print(ptr.number, end=' -> ')
    ptr = ptr.next
print('None')


