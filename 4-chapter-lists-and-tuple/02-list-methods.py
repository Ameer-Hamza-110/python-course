random = ["Harry", "Ron", "Hermione", 1, 2, 2.3, True]

random.append("Dumbledore") # Adding a new element to the end of the list
print(random) # ['Harry', 'Ron', 'Hermione', 1, 2, 2.3, True, 'Dumbledore']

random.reverse() # Reversing the order of the list
print(random) # ['Dumbledore', True, 2.3, 2,

l1 =[16,7,9,1,5]

l1.sort() # Sorting the list in ascending order
print(l1) 

l1.insert(2, 10) # Inserting an element at a specific index
print(l1) # [1, 5, 10, 7, 9

l1.pop(2) # Removing the element at index 2
print(l1) # [1, 5, 10, 7]

l1.remove(7) # Removing the first occurrence of the value 7
print(l1) # [1, 5, 10]

# diff b/w pop and remove
# pop() removes and returns the element at the specified index
# remove() removes the first occurrence of the specified value