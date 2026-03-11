# Arrays (Fixed size list)
# fixed size list of 3 elements
list  = [0] * 3

list[0] = 1
list[1] =  2
list[2] = 3

print('\n Output of fixed size array')
for i in range(3):
    print(list[i])

# Dynamic Array
# Intial list of size 3
list = [1, 2, 3]

# Grow to size 4 by copying manually
l = [0] * 4
for i in range(3):
    l[i] = list[i]

l[3] = 4
list = l

print('\n Ouput of Dynamic array which copied manually')
for i in range(4):
    print(list[i])

# Dynamic array using append method
list = [1, 2, 3]
list.append(4) # Time complexity is O(1)

print('\n Ouput of Dynamic array using append') 
for num in list:
    print(num)

# Dynamic array using inserting
list = [1, 2, 3]
list.insert(3, 4) # Time complexity is O(n)

print('\n Ouput of Dynamic array using insertion')
for num in list:
    print(num)



