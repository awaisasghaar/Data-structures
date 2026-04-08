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

    # ------- INSERT AFTER PREVIOUS VALUE ---------
    def insert_after_value(self, target, data):
        current = self.head
        while current:
            if current.data == target:
                node = Node(data)
                node.next = current.next
                current.next = node
                return True
            current = current.next
        return False
    
    # -------- DELETE A NODE BY VALUE --------
    def delete(self, data):
        if not self.head:
            return False
        if self.head.data == data:
            self.head == self.head.next
            return True
        prev, current = self.head, self.head.next
        while current:
            if current.data == data:
                prev.next = current.next
                return True
            prev, current = current, current.next
        return False

        

if __name__ == "__main__":
    l = LinkedList()
    l.insert_at_head(43)
    l.insert_at_tail(42)
    l.insert_after_value(42, 20)
    l.insert_after_value(20, 30)
    l.delete(20)
    l.traverse()

# Time complexity: O(n)
# Space Complexity: O(n)


    
    
    






