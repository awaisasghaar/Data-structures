# Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

        # ------- INSERT OPERATION -------
        def insert_at_beginning(self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            print(f"\n Insert data at the beginning")



if __name__ == "__main__":
    main = Linkedlist
    main.insert_at_beginning()


    
    
    






