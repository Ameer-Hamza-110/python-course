# ? Set is a collection of unordered, unique elements. It is mutable, meaning you can add or remove elements from it. Sets are commonly used for membership testing, removing duplicates from a sequence, and performing mathematical operations like union, intersection, and difference.

empty = set()  # Empty set


s = {1, 2, 3, 4, 5,5,5}
print(s, type(s))  # Output: {1, 2, 3, 4, 5} <class 'set'> duplicate values are removed