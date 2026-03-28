# Array data structure using insert, search and delete operation

class Array:
    def __init__(self):
        self.data = []
        self.size = 0

    #  ---------- APPEND ----------  
    def append(self):
        for _ in range(3):
            num = int(input("\nNumber: "))
            self.data.append(num)
            self.size += 1
            print(f"{num} is added in Array: {self.data}")
        return f"\n Array: {self.data} is size of {self.size}"
    
    # -------- INSERT ---------
    def insert(self, index=0):
        num = int(input("\nEnter Number to insert: "))
        if index >= 0 and index <= self.size:
            self.data.insert(index, num)
        else:
            print("Nothing happens")
        self.size += 1
        print(f"{num} inserted at index 3")
        return f"\n Array after insertion: {self.data} is size of {self.size}"
    
    # --------- SEARCH ----------
    def search(self):
        num = int(input("\nEnter number to search: "))
        for i in range(self.size):
            if self.data[i] == num:
                return f"\n {num} found at index {i}"
            
        return f"\n Number not found {num} in Array: {self.data} "
    
    def binary_search(self):
        num = int(input("Binary Search: "))

        # Sorting Array
        self.data.sort()
        low = 0
        high = self.size - 1

        while low <= high:
            # Find middle index
            mid = (low + high) // 2
            if self.data[mid] == num:
                return f"\n {num} found at index {mid}"
            
            # Go Right
            elif self.data[mid] < num:
                low = mid + 1
            # Go left
            else:
                high = mid - 1
        print(f"\n {num} not found")



        
if __name__ == "__main__":
   find = Array()
   print(find.append())
   print(find.insert(index=3))
   print(find.search())
   print(find.binary_search())

    # Time Complexity: O(n)
    # Space Complexity: O(1)



