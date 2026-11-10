# ? list is a collection of items which can be of any data type. It is mutable which means that you can change the values of the list after it has been created. Lists are defined by using square brackets [] and the items are separated by commas.

random = ["Hamza", 3, 4.5, True, "Python"]

print(random[0]) # Hamza

random[0] = "Ali" # Changing the value of the first element in the list unlike strings which are immutable
print(random[0]) # Ali

# slicing in lists is similar to slicing in strings. You can use the slice operator [] to get a subset of the list.

print(random[1: 4: 2]) # [3, True] 1 is the starting index, 4 is the ending index and 2 is the step size. The slice operator will return a new list with the elements from index 1 to index 4 (excluding index 4) with a step size of 2.