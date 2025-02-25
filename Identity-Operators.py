# ------------------------------------Identity Operators ------------------------
# Identity operators are used to compare the objects, not if they are equal,
#  but if they are actually the same object, with the same memory location

# is 
x = ["apple", "banana"]
y = ["apple", "banana"]
z=x
print(x is z) #True

print(x is y) #False

print(x == y)#True

# is not

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z) #False 

print(x is not y) #True

print(x != y) #False