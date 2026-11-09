# Python String Methods
# Each method is explained in simple words and prints its output.
# Run this file with: python string_methods.py


# --------------------------------------------------
# 1. CASE CONVERSION METHODS
# --------------------------------------------------

text = "hello world"

# upper() - Changes all letters to uppercase.
print("upper():", text.upper())  # HELLO WORLD

# lower() - Changes all letters to lowercase.
print("lower():", "HELLO WORLD".lower())  # hello world

# capitalize() - Makes the first character uppercase and the rest lowercase.
print("capitalize():", "hELLO WORLD".capitalize())  # Hello world

# title() - Makes the first letter of each word uppercase.
print("title():", text.title())  # Hello World

# swapcase() - Changes uppercase letters to lowercase and lowercase to uppercase.
print("swapcase():", "Hello World".swapcase())  # hELLO wORLD

# casefold() - Makes text lowercase for reliable case-insensitive comparisons.
print("casefold():", "HELLO".casefold())  # hello


# --------------------------------------------------
# 2. REMOVING WHITESPACE OR CHARACTERS
# --------------------------------------------------

# strip() - Removes whitespace from both the beginning and end.
print("strip():", "  hello  ".strip())  # hello

# lstrip() - Removes whitespace from the beginning (left side).
print("lstrip():", "  hello  ".lstrip())  # hello__

# rstrip() - Removes whitespace from the end (right side).
print("rstrip():", "  hello  ".rstrip())  # __hello

# strip() can also remove specified characters from both ends.
print('strip("#"):', "###hello###".strip("#"))  # hello


# --------------------------------------------------
# 3. SEARCHING AND FINDING
# --------------------------------------------------

text = "hello world"

# find() - Returns the position of the first match. Returns -1 if not found.
print("find():", text.find("o"))  # 4

# rfind() - Searches from the right and returns the last matching position.
print("rfind():", text.rfind("o"))  # 7

# index() - Returns the position of the first match. Raises an error if not found.
print("index():", text.index("e"))  # 1

# count() - Counts how many times a character or substring appears.
print("count():", "hello".count("l"))  # 2

# startswith() - Checks whether the string starts with the given text.
print("startswith():", text.startswith("he"))  # True

# endswith() - Checks whether the string ends with the given text.
print("endswith():", text.endswith("world"))  # True


# --------------------------------------------------
# 4. REPLACING, SPLITTING AND JOINING
# --------------------------------------------------

# replace() - Replaces one part of a string with another.
print("replace():", "I like Java".replace("Java", "Python"))  # I like Python

# split() - Breaks a string into a list. By default, it splits at whitespace.
print("split():", "apple,banana,mango".split(","))  # ['apple', 'banana', 'mango']

# rsplit() - Splits from the right side. The second argument limits the number of splits.
print("rsplit():", "a-b-c".rsplit("-", 1))  # ['a-b', 'c']

# join() - Joins items from an iterable into one string using this string as a separator.
print("join():", "-".join(["a", "b", "c"]))  # a-b-c

# partition() - Splits into three parts: before, separator, and after the first match.
print("partition():", "a-b-c".partition("-"))  # ('a', '-', 'b-c')


# --------------------------------------------------
# 5. CHECKING STRING CONTENT
# These methods return True or False.
# --------------------------------------------------

# isalpha() - True if all characters are letters and the string is not empty.
print("isalpha():", "Hello".isalpha())  # True

# isdigit() - True if all characters are digits and the string is not empty.
print("isdigit():", "12345".isdigit())  # True

# isalnum() - True if all characters are letters or numbers and the string is not empty.
print("isalnum():", "abc123".isalnum())  # True

# isspace() - True if the string contains only whitespace and is not empty.
print("isspace():", "   ".isspace())  # True

# islower() - True if all cased letters are lowercase.
print("islower():", "hello".islower())  # True

# isupper() - True if all cased letters are uppercase.
print("isupper():", "HELLO".isupper())  # True

# istitle() - True if each word follows title-case rules.
print("istitle():", "Hello World".istitle())  # True

# isascii() - True if every character belongs to the ASCII character set.
print("isascii():", "Hello 123".isascii())  # True


# --------------------------------------------------
# 6. FORMATTING METHODS
# --------------------------------------------------

# format() - Inserts values into placeholders marked with curly braces.
print("format():", "Hello, {}!".format("Ali"))  # Hello, Ali!

# zfill() - Adds zeros to the beginning until the string reaches the given length.
print("zfill():", "42".zfill(5))  # 00042

# center() - Centers the text inside a string of the given width.
print("center():", "Hi".center(6, "-"))  # --Hi--

# ljust() - Places the text on the left and fills the remaining space on the right.
print("ljust():", "Hi".ljust(5, "-"))  # Hi---

# rjust() - Places the text on the right and fills the remaining space on the left.
print("rjust():", "Hi".rjust(5, "-"))  # ---Hi


# --------------------------------------------------
# 7. OTHER USEFUL METHODS
# --------------------------------------------------

# removeprefix() - Removes the given text only if it appears at the beginning.
print("removeprefix():", "unhappy".removeprefix("un"))  # happy

# removesuffix() - Removes the given text only if it appears at the end.
print("removesuffix():", "file.txt".removesuffix(".txt"))  # file

# expandtabs() - Replaces each tab character (\t) with spaces.
print("expandtabs():", "Name\tAge".expandtabs(4))  # Name    Age


# --------------------------------------------------
# IMPORTANT NOTE
# --------------------------------------------------
# Strings in Python are immutable. This means string methods return a
# new string; they do not change the original string.
#
# Example:
original = "python"
new_text = original.upper()

print("Original string:", original)  # python
print("New string:", new_text)        # PYTHON
