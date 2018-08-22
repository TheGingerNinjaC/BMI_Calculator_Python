"""
Author: Chané van der Berg
Date modified: 29/03/2018

Write a program that receives the weight and length of a person as input
from the user. The program should start by asking if the user would like to
enter the weight and length in kilograms and meters or in pounds and inches by
entering either a 1 or a 2.

After the person entered the information the program should write a report that
summarises the weight, length, BMI and the result of the BMI “underweight,
normal overweight, obese”.

The calculations for the BMI are as follows:

a. For kilograms and meters: The formula is BMI = kg/m2 where kg is a person's
weight in kilograms and m2 is their height in metres squared, round to one
decimal place.
b. For pounds and inches:  The formula is weight (lb) / [height (in)]2 x 703,
divide weight (lb) by height (in) squared, multiply by 703, round to one decimal
place.

Lastly the results are depended on the BMI and are as follows:
a. BMI larger or equal to 30: Obese
b. BMI between 29 and 25: Overweight
c. BMI between 25 and 18.5: Normal
d. BMI smaller than 18.5: Underweight
"""
print("BMI Calculator")
print()

# determine input choices
print("1. Weight in pounds, height in inches")
print("2. Weight in kilograms, height in meters")
print()

# define variable for choices and provide input
choice = int(input("Choice: "))
print()

# define if statement for choice 1
if choice==1:
    wlbs = float(input("Weight in pounds?: "))
    print()
    hinch = float(input("Height in inches?: "))

    print()
    print()

    #calculations
    BMI_imp = round(wlbs / (hinch) ** 2 * 703, 1)

    # define parameters
    if BMI_imp >= 30:
        result = "Obese"
    elif BMI_imp > 25:
        result = "Overweight"
    elif BMI_imp > 18.5:
        result = "Normal"
    else:
        result = "Underweight"

    print("Result..............")
    print()

    # provide outputs
    print(" Weight:"," " * 5,str(wlbs),"pounds")
    print(" Height:"," " * 5,str(hinch),"inches")
    print(" BMI:"," " * 8,str(BMI_imp))
    print(" Status:"," " * 5,result)

# define statement for choice 2
if choice==2:
    wkg = float(input("Weight in kilograms?: "))
    print()
    hmeter = float(input("Height in meters?: "))

    print()
    print()

    # calculations
    BMI_met = round(wkg / (hmeter) ** 2, 1)

    # define parameters
    if BMI_met >= 30:
        result = "Obese"
    elif BMI_met > 25:
        result = "Overweight"
    elif BMI_met > 18.5:
        result = "Normal"
    else:
        result = "Underweight"

    print("Result..............")
    print()

    # provide outputs
    print(" Weight:"," " * 5,str(wkg),"kilograms")
    print(" Height:"," " * 5,str(hmeter),"meters")
    print(" BMI:"," " * 8,str(BMI_met))
    print(" Status:"," " * 5,result)

print()
input("Please press enter to quit the program. ")
