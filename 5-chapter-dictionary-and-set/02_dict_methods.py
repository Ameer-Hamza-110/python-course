marks = {
    "Hamza": 90,
    "Ali": 85,
    "Ayesha": 95,
}


# 1. items() - Returns all key-value pairs.
print(marks.items())
# Output: dict_items([('Hamza', 90), ('Ali', 85), ('Ayesha', 95)])


# 2. keys() - Returns all keys.
print(marks.keys())
# Output: dict_keys(['Hamza', 'Ali', 'Ayesha'])


# 3. values() - Returns all values.
print(marks.values())
# Output: dict_values([90, 85, 95])


# 4. get() - Returns the value of a key.
# Returns None if the key doesn't exist.
print(marks.get("Ali"))
# Output: 85

print(marks.get("Omar"))
# Output: None


# 5. update() - Adds new key-value pairs or updates existing values.
marks.update({"Hamza": 95, "Omar": 96})
print(marks)
# Output: {'Hamza': 95, 'Ali': 85, 'Ayesha': 95, 'Omar': 96}


# 6. pop() - Removes a specific key and returns its value.
print(marks.pop("Ali"))
# Output: 85

print(marks)
# Output: {'Hamza': 95, 'Ayesha': 95, 'Omar': 96}


# 7. popitem() - Removes and returns the last inserted key-value pair.
print(marks.popitem())
# Output: ('Omar', 96)

print(marks)
# Output: {'Hamza': 95, 'Ayesha': 95}


# 8. setdefault() - Returns the value if the key exists.
# If the key doesn't exist, adds it with the default value.
print(marks.setdefault("Hamza", 100))
# Output: 95

print(marks.setdefault("Sara", 88))
# Output: 88

print(marks)
# Output: {'Hamza': 95, 'Ayesha': 95, 'Sara': 88}


# 9. copy() - Creates a shallow copy of the dictionary.
new_marks = marks.copy()
print(new_marks)
# Output: {'Hamza': 95, 'Ayesha': 95, 'Sara': 88}


# 10. clear() - Removes all key-value pairs.
new_marks.clear()
print(new_marks)
# Output: {}


# ============================================
# DICTIONARY-RELATED OPERATIONS
# ============================================

marks = {
    "Hamza": 90,
    "Ali": 85,
    "Ayesha": 95,
}


# 11. Access value using key.
print(marks["Hamza"])
# Output: 90


# 12. Add a new key-value pair.
marks["Omar"] = 96
print(marks)
# Output: {'Hamza': 90, 'Ali': 85, 'Ayesha': 95, 'Omar': 96}


# 13. Update an existing value.
marks["Ali"] = 92
print(marks["Ali"])
# Output: 92


# 14. Check whether a key exists using 'in'.
print("Hamza" in marks)
# Output: True

print("Sara" in marks)
# Output: False


# 15. Check whether a key does not exist using 'not in'.
print("Sara" not in marks)
# Output: True


# 16. Find the number of key-value pairs using len().
print(len(marks))
# Output: 4


# 17. Delete a key-value pair using del.
del marks["Ali"]
print(marks)
# Output: {'Hamza': 90, 'Ayesha': 95, 'Omar': 96}


# 18. Create a dictionary using fromkeys().
subjects = ["Math", "English", "Science"]
result = dict.fromkeys(subjects, 0)

print(result)
# Output: {'Math': 0, 'English': 0, 'Science': 0}