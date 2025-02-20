# Variable Definitions
name = "Aleeza"  # str (Text Type)
age = 18  # int (Numeric Type)
is_Student = True  # bool (Boolean Type)

# Printing the types of variables
print(type(name))  # Output: <class 'str'>
print(type(age))  # Output: <class 'int'>
print(type(is_Student))  # Output: <class 'bool'>

# Data Types

# Text Type
# - str: Represents a string, a sequence of characters.
# - Used for storing text-based data.
# Example: name = "Aleeza"

# Numeric Types
# - int: Represents an integer (whole number).
# - float: Represents a floating-point number (decimal numbers).
# - complex: Represents a complex number with a real and imaginary part.
# Example: age = 18  # int
# Example: height = 5.5  # float
# Example: complex_number = 2 + 3j  # complex

# Boolean Type
# - bool: Represents a value that is either True or False.
# - Used for logical operations and comparisons.
# Example: is_active = True  # boolean
# Example: is_student = False  # boolean

# None Type
# - NoneType: Represents the absence of a value or a null value.
# - Used to signify that a variable does not have any assigned value.
# Example: my_var = None  # NoneType, no value assigned

# Memory Addresses
# id() function returns the memory address (unique identifier) of the variable
print("Memory Address of age:", id(age))  # Prints memory address of age
print("Memory Address of is_Student:", id(is_Student))  # Prints memory address of is_Student
