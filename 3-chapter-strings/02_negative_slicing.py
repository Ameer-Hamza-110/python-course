name = "Hamza";

print(name[-4: -1]) # Output: amz (start from index -4 to -1, which is equivalent to index 1 to 4 in positive slicing)
print(name[1: 4]) # amz (converting negative slicing to positive slicing, -4 is equivalent to 1 and -1 is equivalent to 4)


print(name[1:]) # Output: amza (start from index 1 to the end of the string, which is "amza") - (By default, the end index is the length of the string if not specified)
print(name[:4]) # Output: Hamz (start from the beginning of the string to index 4, which is "Hamz") - (By default, the start index is 0 if not specified)