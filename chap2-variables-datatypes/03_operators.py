#? Arthimetic Operators are used to perform mathematical operations like addition, subtraction, multiplication, etc. on numbers.
# a = 10;
# b = 35;
# c= a + b; # Addition
# print("Addition of a and b is: ", c);


#? Assignment Operators are used to assign values to variables. The most common assignment operator is the equal sign (=).  
a = 10; # a is the variable that stores the value 10
b = 5; # This is equivalent to b = b + 5
b += 5; # This is equivalent to b = b + 5
b *= 2; # This is equivalent to b = b * 2
print("Value of a is: ", a);
print("Value of b is: ", b);



#? Comparison Operators are used to compare two values. They return a boolean value (True or False) based on the comparison.
a = 5<4;
print("Is 5 less than 4? ", a); # False



#? Logical Operators are used to combine conditional statements. The most common logical operators are and, or, and not.

# truth table of or operator
print("Truth or false is: ", True or False); # True
print("False or True is: ", False or True); # True
print("True or True is: ", True or True); # True
print("False or False is: ", False or False); # False

# truth table of and operator
print("Truth and false is: ", True and False); # False
print("False and True is: ", False and True); # False
print("True and True is: ", True and True); # True
print("False and False is: ", False and False); # False

# truth table of not operator
print("Not True is: ", not True); # False
print("Not False is: ", not False); # True