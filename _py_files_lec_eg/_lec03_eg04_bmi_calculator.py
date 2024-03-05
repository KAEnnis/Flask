"""
Body Mass Index (BMI) is a measure of health on weight. 
It can be calculated by taking your weight in kilograms and 
dividing by the square of your height in meters. 
The interpretation of BMI for people 16 years or older is as follows:
+-------------+-----------------------+
| BMI         | Category              |
+-------------+-----------------------+
| < 18.5      | Underweight           |
| 18.5 - 24.9 | Normal weight         |
| 25 - 29.9   | Overweight            |
| >= 30       | Weight Issue (Class 1)|
| ...         | ...                   |
+-------------+-----------------------+
"""
#Below solution attempt... 
def KG_PER_POUND():
    return 0.45359237   # Constant

def MTR_PER_INCH():
    return 0.0254       # Constant 

# weight_lbs = float( input("Enter weight in pounds:"))
# height_in  = float( input("Enter your height in inches:") )
weight_lbs =   170  #test values
height_in  =   70   #test values

weight_kg  = weight_lbs * KG_PER_POUND()
height_mtr = height_in  * MTR_PER_INCH()

# bmi = weight_kg / (height_mtr**2)  #** means to "the power of"
bmi = 0
#How to test each branch...
msg = ""
if 1 < bmi < 18.5:     
    msg = "Underweight"
elif 18.5 < bmi < 24.9:
    msg = "Normal weight"
elif 25.0 < bmi < 29.9:  
    msg = "Overweight"
elif 29.9 < bmi <= 30: 
    msg = "Weight Issue (Class 1)"
else:
    if bmi <= 0:
        msg = "bmi can't be lower than 1"
    else:
        msg = "bmi too large to calc"     
print(f"your BMI is: {bmi}: you are classifed as: {msg}")
