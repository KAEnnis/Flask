"""
In Python, all data are objects. A variable for an object is actually 
a reference to the object. When you invoke a function with a parameter, 
the reference value of the argument is passed to the parameter. 
This is referred to as pass-by-value. For simplicity, we say that the 
value of an argument is passed to a parameter when invoking a function. 
Precisely, the value is actually a reference value to the object.

If the argument is a number or a string, the argument is not affected, 
regardless of the changes made to the parameter inside the function. 

Write an example code with two versions:
one passing an int and one passing a list
"""

##E.G. version 1 passing an int:
def main():
    x = 1
    print("Before the call, x is", x)
    increment(x)
    print("After the call, x is", x)

def increment(n): 
    n += 1
    print("\tn inside the function is", n)

main() # Call the main function
