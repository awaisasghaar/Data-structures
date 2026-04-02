# Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse(head):
    if head is None:
        print("Head node is NULL")
        return
    current = head
    while current is not None:
        print(f"{current.data}", end=' ')
        current = current.next
    print()

def insert_at_front(head, a):
    new_node = Node(a)
    new_node.next = head
    return new_node

def search_num(head, num):
    current = head
    while current is not None:
        if current.data == num:
            return True
        current = current.next
    return False

def insert_at_end(head, x):
    new_node = Node(x)
    if head is None:
        return new_node
    last = head
    while last.next is not None:
        last = last.next
    last.next = new_node
    return head

def print_list(head):
    current = head
    while current is not None:
        if current.next is not None:
            print(f"{current.data} -> ", end="")
        else:
            print(current.data)
        current = current.next

if __name__ == "__main__":
    head = Node(5)
    head.next = Node(10)
    head.next.next = Node(15)
    head.next.next.next = Node(20)

    traverse(head)               # 5 10 15 20

    head = insert_at_front(head, 1)
    print_list(head)             # 1 -> 5 -> 10 -> 15 -> 20

    print(search_num(head, 15))  # True
    print(search_num(head, 99))  # False

    head = insert_at_end(head, 92)
    print_list(head)             # 1 -> 5 -> 10 -> 15 -> 20 -> 92


    
    
    






