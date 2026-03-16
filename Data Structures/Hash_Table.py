# Hash Table
Hash_size = 100

# Hash function maps word to index 0-25 based on first letter
def hash_func(word):
    return ord(word[0].upper()) - ord('A')

# Hash Table: array of lists (chaining for collisions)
hash_table = [[]for _ in range(Hash_size)]


def insert(word):
    index = hash_func(word)
    hash_table[index].append(word)
    return f'{word} at index {index}'

def search(word):
    index = hash_func(word)
    return word in hash_table[index]
  
def delete(word):
    index = hash_func(word)
    if word in hash_table[index]:
        hash_table[index].remove(word)
        return True
    return False
  
def display():
    for i, char in enumerate(hash_table):
        if char:
           letter = str(i + ord('A'))
           print(f"Index is {i} {letter} -> {char}")

# Usage
print(insert('Awais'))
print(insert('Computer Science'))
print(insert('Student'))
print(insert('Aspiring'))

print(search('Computer Science'))
print(search('Boys'))

print('\nAfter deleting Aspiring')
print(delete('Aspiring'))
print(display())