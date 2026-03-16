# Hash Table
Hash_size = 100

# Hash function maps word to index 0-25 based on first letter
def hash_func(word):
    return ord(word[0].upper()) - ord('A')

# Hash Table: array of lists (chaining for collisions)
hash_table = [[] for _ in range(Hash_size)]

def insert(word):
    index = hash_func(word)
    hash_table[index].append(word)
    return f'{word} at index {index}'

def search(word):
    index = hash_func(word)
    return word in hash_table[index]


# Usage
print(insert('Awais'))
print(insert('Computer Science'))
print(insert('Student'))
print(insert('Aspiring'))

print(search('Computer Science'))
print(search('Boys'))