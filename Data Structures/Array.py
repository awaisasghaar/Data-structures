# Array data structure using insert, search and delete operation

class Array:
    def __init__(self):
        self.data = []
        self.size = 0
        
    def append(self):
        for _ in range(3):
            num = int(input("\nNumber: "))
            self.data.append(num)
            self.size += 1
            print(f"{num} is added in Array: {self.data}")
        return f"\n Array {self.data} is size of {self.size}"
        
    def insert(self, index=0):
        num = int(input("\nNumber: "))
        if index >= 0 and index <= self.size:
            self.data.insert(index, num)
        else:
            print("Nothing happens")
        self.size += 1
        print(f"{num} inserted at index 3")
        return f"\n Array {self.data} is size of {self.size}"
        

find = Array()
print(find.append())
print(find.insert(index=3))

    # Time Complexity: O(n)
    # Space Complexity: O(1)



