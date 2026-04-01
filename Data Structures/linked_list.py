# Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

if __name__ == "__main__":

    # Create Nodes
    node1 = Node(4)
    node2 = Node(6)
    node3 = Node(8)
    node4 = Node(10)

    # Link Nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # Head will point to the first node
    head = node1

    # Traverse and print the Linked List
    current = head
    while current:
        print(f"{current.data} ->", end=" ")
        current = current.next
    print("None")


# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse(head):
    if head is None:
        return f"Head node is NULL"
    while head is not None:
        print(f"{head.data}", end=' ')
        head = head.next

def search_num(head, num):
    current = head
    while current is not None:
        if current.data == num:
            return True
        current = current.next
    return False
    
    
if __name__ == "__main__":
    head = Node(5)
    head.next = Node(10)
    head.next.next = Node(15)
    head.next.next.next = Node(20)
    print(traverse(head))
    num = 20
    num = 15
    print(search_num(head, num))
    
    






