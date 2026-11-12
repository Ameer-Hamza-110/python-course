# ============================================
# PYTHON SET METHODS
# ============================================

numbers = {1, 2, 3, 4, 5}


# 1. add() - Adds one element to the set.
numbers.add(6)
print(numbers)
# Output: {1, 2, 3, 4, 5, 6}


# 2. update() - Adds multiple elements from an iterable.
numbers.update([7, 8, 9])
print(numbers)
# Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}


# 3. remove() - Removes a specific element.
# Raises KeyError if the element doesn't exist.
numbers.remove(9)
print(numbers)
# Output: {1, 2, 3, 4, 5, 6, 7, 8}


# 4. discard() - Removes an element if it exists.
# Does not raise an error if the element doesn't exist.
numbers.discard(8)
print(numbers)
# Output: {1, 2, 3, 4, 5, 6, 7}


# 5. pop() - Removes and returns an arbitrary element.
removed = numbers.pop()
print(removed)  # Output: An arbitrary element
print(numbers)  # Output: Remaining elements


# 6. clear() - Removes all elements from the set.
numbers.clear()
print(numbers)
# Output: set()


# ============================================
# SET OPERATIONS
# ============================================

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}


# 7. union() - Returns all unique elements from both sets.
print(set1.union(set2))
# Output: {1, 2, 3, 4, 5, 6}


# 8. intersection() - Returns common elements from both sets.
print(set1.intersection(set2))
# Output: {3, 4}


# 9. difference() - Returns elements present in the first set
# but not in the second set.
print(set1.difference(set2))
# Output: {1, 2}


# 10. symmetric_difference() - Returns elements that are
# present in either set, but not in both.
print(set1.symmetric_difference(set2))
# Output: {1, 2, 5, 6}


# 11. intersection_update() - Keeps only common elements
# in the original set.
set1.intersection_update(set2)
print(set1)
# Output: {3, 4}


# 12. difference_update() - Removes elements found in
# the second set from the original set.
set1 = {1, 2, 3, 4}
set1.difference_update(set2)
print(set1)
# Output: {1, 2}


# 13. symmetric_difference_update() - Updates the original
# set with elements that are not common.
set1 = {1, 2, 3, 4}
set1.symmetric_difference_update(set2)
print(set1)
# Output: {1, 2, 5, 6}


# ============================================
# SET COMPARISON METHODS
# ============================================

set1 = {1, 2}
set2 = {1, 2, 3, 4}
set3 = {5, 6}


# 14. issubset() - Checks whether all elements of one
# set exist in another set.
print(set1.issubset(set2))
# Output: True


# 15. issuperset() - Checks whether a set contains
# all elements of another set.
print(set2.issuperset(set1))
# Output: True


# 16. isdisjoint() - Checks whether two sets have
# no common elements.
print(set1.isdisjoint(set3))
# Output: True


# 17. copy() - Creates a shallow copy of the set.
new_set = set1.copy()
print(new_set)
# Output: {1, 2}


# ============================================
# SET-RELATED OPERATIONS
# ============================================

# 18. Create a set using curly braces.
fruits = {"apple", "banana", "mango"}
print(fruits)
# Output: A set containing apple, banana, mango


# 19. Create an empty set using set().
empty_set = set()
print(empty_set)
# Output: set()


# 20. Remove duplicate values by converting a list into a set.
numbers = [1, 2, 2, 3, 3, 4]
unique_numbers = set(numbers)
print(unique_numbers)
# Output: {1, 2, 3, 4}


# 21. Check whether an element exists using 'in'.
fruits = {"apple", "banana", "mango"}
print("apple" in fruits)
# Output: True


# 22. Check whether an element does not exist using 'not in'.
print("orange" not in fruits)
# Output: True


# 23. Find the number of elements using len().
print(len(fruits))
# Output: 3


# 24. Delete a set using del.
del empty_set