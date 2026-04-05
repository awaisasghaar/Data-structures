# Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # pointer to next node
    
class LinkedList:
    def __init__(self):
        # empty list
        self.head = None
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        return

    # ------ INSERT AT HEAD ------
    def insert_at_head(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # ------- INSERT AT TAIL -------
    def insert_at_tail(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = node

        

if __name__ == "__main__":
    l = LinkedList()
    l.insert_at_head(43)
    l.insert_at_tail(42)
    l.traverse()


    
    
    






