#!/usr/bin/env python3


# Calculate the tax.
# Change the functions below to calculate the right tax and return the amount.

# Standard tax rate is 8.1%
def standard_tax(amount):
    return (amount*0.081)


# Reduced tax rate is 2.5%
def reduced_tax(amount):
    return (amount*0.025)


# Accommodation tax rate is 3.7%
def accommodation_tax(amount):
    return (amount*0.037)


# Helper function to round the tax to the nearest 0.05 increment.
def round_tax(tax):
    return round((round(tax / 0.05) * 0.05), 2)


# Main function
def calculate_tax(amount, tax_type):
    if amount <= 0:
        amount = 0
    tax_raw = tax_type(amount)
    tax =  round_tax(tax_raw)
    return tax
    # Return the amount after you have calculated the tax.


# The following lines call the function and prints the return
# value to the Console. This way you can check what it does.
print(calculate_tax(101, standard_tax))
print(calculate_tax(101, reduced_tax))
print(calculate_tax(101, accommodation_tax))
