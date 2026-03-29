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
    
    # ---------- BINARY SEARCH ---------
    def binary_search(self):
        num = int(input("\nBinary Search: "))

        # Sorting Array
        self.data.sort()
        low = 0
        high = self.size - 1

        while low <= high:
            # Find middle index
            mid = (low + high) // 2
            if self.data[mid] == num:
                print(f"\n {num} found at index {mid}")
                break
            
            # Go Right
            elif self.data[mid] < num:
                low = mid + 1
            # Go left
            elif self.data[mid] > num:
                high = mid - 1
            else:
                print(f"\n{num} not found")
                
        return f"\n Array after sorted: {self.data}"
    
    # --------- Delete by Index ---------
    def delete_index(self, index=0):
        if index is None:
            print("Nothing here to delete here.")
        if index is not None:
            if index >= 0 and index < self.size:
                remove = self.data.pop(index)
                self.size -= 1
                print(f"\nIndex {remove} removed")
            return f"\n Array after deletion of an index: {self.data}"
        else:
            f"\n Invalid Index"

    # ---------- Delete by Value ----------
    def delete_value(self):
        num = int(input("\nEnter Nunmber to delete: "))
        if num in self.data:
            self.data.remove(num)
            self.size -= 1 
            return f"\n {num} deleted Array: {self.data} size of {self.size}"
        else:
            print(f"\n {num} is not in the Array: {self.data}")
    


        
if __name__ == "__main__":
   find = Array()
   print(find.append())
   print(find.insert(index=3))
   print(find.search())
   print(find.binary_search())
   print(find.delete_index())
   print(find.delete_value())

    # Time Complexity: O(n log n)
    # Space Complexity: O(n)



