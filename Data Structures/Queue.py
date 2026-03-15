# Queue 
from collections import deque

data = 100
class Queue:
    def __init__(self):
        self.people = deque()
        self.size = 0

    def enqueue(self, person):
        if self.size < data:
            self.people.append(person)
            self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.people.popleft()
        return None
    
if __name__ == '__main__':

    # Created a Queue
    q = Queue()

    # Add people
    q.enqueue('Awais')
    q.enqueue(22)
    q.enqueue('Virtual University')

    # print Queue
    print(q.people)
    print(q.size)

    # Dequeue
    print(q.dequeue())
    print(q.people)
