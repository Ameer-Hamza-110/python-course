# ============================================
# PYTHON LIST AND TUPLE METHODS
# Simple explanations with examples and output
# ============================================

# ============================================
# 1. LIST METHODS
# ============================================

# Lists are ordered and mutable.
# Mutable means we can add, remove, or change items.

print("\n========== LIST METHODS ==========")


# A. ADDING ELEMENTS

fruits = ["apple", "banana"]

# append() - Adds one item at the end of the list.
fruits.append("mango")
print("append():", fruits)
# Output: ['apple', 'banana', 'mango']

# extend() - Adds multiple items from another iterable.
fruits.extend(["orange", "grapes"])
print("extend():", fruits)
# Output: ['apple', 'banana', 'mango', 'orange', 'grapes']

# insert() - Adds an item at a specific index.
fruits.insert(1, "kiwi")
print("insert():", fruits)
# Output: ['apple', 'kiwi', 'banana', 'mango', 'orange', 'grapes']


# B. REMOVING ELEMENTS

fruits = ["apple", "banana", "mango", "orange"]

# remove() - Removes the first matching item by value.
fruits.remove("banana")
print("remove():", fruits)
# Output: ['apple', 'mango', 'orange']

# pop() - Removes and returns an item. Without an index,
# it removes the last item.
removed_item = fruits.pop()
print("pop() removed:", removed_item)
print("pop() list:", fruits)
# Output: orange
#         ['apple', 'mango']

# pop(index) - Removes and returns the item at that index.
removed_item = fruits.pop(0)
print("pop(0) removed:", removed_item)
print("pop(0) list:", fruits)
# Output: apple
#         ['mango']

# clear() - Removes all items from the list.
fruits.clear()
print("clear():", fruits)
# Output: []


# C. SEARCHING AND COUNTING

fruits = ["apple", "banana", "mango", "apple"]

# index() - Returns the index of the first matching item.
print("index():", fruits.index("banana"))
# Output: 1

# count() - Counts how many times an item appears.
print("count():", fruits.count("apple"))
# Output: 2


# D. SORTING AND REVERSING

numbers = [5, 2, 8, 1, 9]

# sort() - Sorts the original list in ascending order.
numbers.sort()
print("sort():", numbers)
# Output: [1, 2, 5, 8, 9]

# sort(reverse=True) - Sorts the original list in descending order.
numbers.sort(reverse=True)
print("sort(reverse=True):", numbers)
# Output: [9, 8, 5, 2, 1]

# reverse() - Reverses the current order of the list.
numbers.reverse()
print("reverse():", numbers)
# Output: [1, 2, 5, 8, 9]

# copy() - Creates a shallow copy of the list.
new_numbers = numbers.copy()
print("copy():", new_numbers)
# Output: [1, 2, 5, 8, 9]


# ============================================
# 2. TUPLE METHODS
# ============================================

# Tuples are ordered and immutable.
# Immutable means we cannot add, remove, or change their items.
# Tuples have only two built-in methods: count() and index().

print("\n========== TUPLE METHODS ==========")

fruits = ("apple", "banana", "mango", "apple")

# count() - Counts how many times an item appears.
print("count():", fruits.count("apple"))
# Output: 2

# index() - Returns the index of the first matching item.
print("index():", fruits.index("banana"))
# Output: 1


# ============================================
# 3. USEFUL BUILT-IN FUNCTIONS
# These are functions, not list or tuple methods.
# They work with both lists and tuples.
# ============================================

print("\n========== BUILT-IN FUNCTIONS ==========")

numbers = [10, 20, 30, 40, 50]

# len() - Returns the number of items.
print("len():", len(numbers))
# Output: 5

# max() - Returns the largest item.
print("max():", max(numbers))
# Output: 50

# min() - Returns the smallest item.
print("min():", min(numbers))
# Output: 10

# sum() - Adds all numeric items.
print("sum():", sum(numbers))
# Output: 150

# sorted() - Returns a NEW sorted list without changing the original.
print("sorted():", sorted([5, 2, 8, 1]))
# Output: [1, 2, 5, 8]

# any() - Returns True if at least one item is truthy.
print("any():", any([0, False, 5]))
# Output: True

# all() - Returns True if every item is truthy.
print("all():", all([1, True, "hello"]))
# Output: True


# ============================================
# 4. LIST VS TUPLE
# ============================================

print("\n========== LIST VS TUPLE ==========")

# A list can be changed.
my_list = ["apple", "banana"]
my_list.append("mango")
print("Updated list:", my_list)
# Output: ['apple', 'banana', 'mango']

# A tuple cannot be changed directly.
my_tuple = ("apple", "banana")
print("Tuple:", my_tuple)
# Output: ('apple', 'banana')

# To modify tuple contents, convert it to a list,
# make the changes, and convert it back to a tuple.
temporary_list = list(my_tuple)
temporary_list.append("mango")
my_tuple = tuple(temporary_list)
print("Updated tuple:", my_tuple)
# Output: ('apple', 'banana', 'mango')


# ============================================
# IMPORTANT NOTES
# ============================================

# 1. append() adds one item; extend() adds items from an iterable.
# 2. remove() removes by value; pop() removes by index (last by default).
# 3. sort() changes the original list; sorted() returns a new sorted list.
# 4. Lists are mutable; tuples are immutable.
# 5. List and tuple indexes start from 0.
