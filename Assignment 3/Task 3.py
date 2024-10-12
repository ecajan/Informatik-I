#!/usr/bin/env python3

# Determine the BMI. Change the function
# below to calculate the BMI return which category the result is in.
# Your implementation should work with any specific value.


def get_bmi_category(height, weight):
    bminum = float(weight/(height**2))
    if weight < 0:
        bmi = "N/A"
        return bmi
    elif height < 0:
        bmi = "N/A"
        return bmi
    elif bminum <= 18.5:
        bmi = "BMI: {:.2f}".format(bminum) + ", Category: Underweight"
    elif bminum <= 25:
        bmi = "BMI: {:.2f}".format(bminum) + ", Category: Normal weight"
    elif bminum <= 30:
        bmi = "BMI: {:.2f}".format(bminum) + ", Category: Pre-obesity"
    elif bminum <= 35:
        bmi = "BMI: {:.2f}".format(bminum) + ", Category: Obesity class I"
    elif bminum <= 40:
        bmi = "BMI: {:.2f}".format(bminum) + ", Category: Obesity class II"
    elif bminum > 40:
        bmi = "BMI: {:.2f}".format(bminum) + ", Category: Obesity class III"
    return bmi
    # Return the BMI values and the correct category after you have calculated the BMI.


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
#print(get_bmi_category(1.8, 80))
