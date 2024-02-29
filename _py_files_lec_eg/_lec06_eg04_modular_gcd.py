"""
Functions can be used to reduce redundant coding and enable code reuse. 
Functions can also be used to modularize code 
and improve the quality of the program.
"""

#e.g. store this in a file:
# `my_math_module.py`
def gcd(n1, n2):
    gcd = 1 # Initial gcd is 1
    k = 2   # Possible gcd

    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k # Update gcd
        k += 1

    return gcd # Return gcd


#THEN from another .py file...

# from my_math_module import gcd # Import the module

# Prompt the user to enter two integers
n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))

print("The greatest common divisor for", n1,
    "and", n2, "is", gcd(n1, n2))

