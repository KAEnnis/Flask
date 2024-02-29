"""
Write a program that simulates a simplified
lottery game.
The program should randomly generate a 2-digit
number between 0 and 99 and prompts the user 
to guess the number.

The program should check the guess and 
print the result according to the following rules:

If the user input matches the number exactly, the award is $10,000.
If the user input matches the digits but in the wrong order the award is $3,000.
If the user input matches any one digits the award is $1,000.
"""

import random

#FOR TESTING: Manually setting a guessable number but replace for random
lottery = 42
print("THE TEST NUMBER IS 42")
# lottery = random.randint(0, 99)

print("The lottery number is", lottery)


# Prompt the user to enter a guess

# Get digits from lottery
# Get digits from guess

# Check the guess
#if exactly right:
    # print("Exact match: you win $10,000")

#if right digits wrong order
    # print("Match all digits: you win $3,000")

#if match one digit
    # print("Match one digit: you win $1,000")

#otherwise
    # print("Sorry, no match")
