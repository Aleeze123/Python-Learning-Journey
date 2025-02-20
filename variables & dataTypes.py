# Variables in Python
name = "Aleeza"  # String 
age = 18  # Integer 
is_Student = True  # Boolean 

print(name) #Aleeza
# types of variables
print(type(name)) 
print(type(age)) 
print(type(is_Student))
# Data Types

# Text Type
# - str: Represents a string, a sequence of characters.
# - Used for storing text-based data.
# name = "Aleeza"

# Numeric Types
# - int: Represents an integer (whole number).
# - float: Represents a floating-point number (decimal numbers).
# - complex: Represents a complex number with a real and imaginary part.
# age = 18  # int
# height = 5.5  # float
# complex_number = 2 + 3j  # complex

# Boolean Type
# - bool: Represents a value that is either True or False.
# - Used for logical operations and comparisons.
# is_active = True  # boolean
# is_student = False  # boolean

# None Type
# - NoneType: Represents the absence of a value or a null value.
# - Used to signify that a variable does not have any assigned value.
#my_var = None  # NoneType, no value assigned



# Memory addresses
# id() function returns the memory address (unique identifier) of the variable
print("Memory Address of age:", id(age)) 
print("Memory Address of is_Student:", id(is_Student))  
