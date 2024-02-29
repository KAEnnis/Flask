"""
Often the number of times a loop is executed is not predetermined. 
You may use an input value to signify the end of the loop. 
Such a value is known as a sentinel value. 

Write a program that reads and calculates the sum of an unspecified number of integers. 
The input 0 signifies the end of the input. 
"""
data = int(input("Enter an integer (the input exits " + 
    "if the input is 0): "))

# Keep reading data until the input is 0
sum = 0
while data != 0:
    sum += data

    data = int(input("Enter an integer (the input exits " +
        "if the input is 0): "))

print("The sum is", sum)
