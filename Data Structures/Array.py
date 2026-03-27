# Array data structure using insert, search and delete operation

class Array:
    def __init__(self):
        self.data = []
        self.size = 0
    
    # -------INSERT--------
    def insert(self, value, index=None):
        """Insert a value at given index"""
        if index is None:
            self.data.append(value)
        elif index >= 0 and index <= self.size:
            self.data.insert(index, value)
        else:
            raise IndexError(f"Index {index} out of range")
        self.size += 1
        return f"Value {value} inserted at index {index}"

    def display(self):
        print(f"Array {self.data} size {self.size}")


if __name__ == '__main__':
    find = Array()
    print(find.insert(10)) # append O(n) time complexity
    print(find.insert(20)) # append O(n) time complexity
    print(find.insert(30)) # append O(n) time complexity
    print(find.insert(15, index=1)) # O(n) time complexity
    find.display() # O(n) time complexity

    # Time Complexity: O(n)
    # Space Complexity: O(n)



