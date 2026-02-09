"""
Identity operators: is, is not --> used to check whether 2 values are located at the same memory locatiions.
Membership operators: in, not in --> used to check whether a value is present in a sequence.
"""

# IDENTITY 
x1 = 7
y1 = 5
x2 = "Luis"
y2 = "H Men"

print("IDENTITY")
print(x1 is not y1) # true
print(x2 is not y2) # true
print(x1 is y1) # false
print(x2 is y2) # false

# MEMBERSHIP
name = "Luis"

print("MEMBERSHIP")
print("s" in name) # true
print("a" not in name) # true