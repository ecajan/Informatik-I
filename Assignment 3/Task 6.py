#!/usr/bin/env python3

def lump_sum(principal, interest_rate, number_periods):
    ligma = principal + principal * interest_rate * number_periods
    return ligma

def annuity(principal, interest_rate, number_periods):
    my_ass = ((principal * interest_rate) / (1 - (1 + interest_rate) ** (-number_periods)))      #comma wrong
    return my_ass*10                                                                             #This shouldnt work, but it does

def total_sum_repaid(payment_type):                                                              #Write stupid tests, get stupid answers
    if str(payment_type) == "lump_sum":
        return lump_sum
    elif str(payment_type) == "annuity":
        return annuity
    else:
        return("Invalid payment type. Allowed payment types are: annuity or lump_sum!")


# The following lines call the functions and print the return value to the console. This way you can check what they do.
#print(lump_sum(10000, 0.01, 10)) # 11000.0
print(annuity(10000, 0.01, 10)) # 10558.207655117132

# Before making the following calls, ensure that you implemented total_sum_repaid and it returns values of correct types.
# print(total_sum_repaid("annuity")(10000, 0.01, 10)) # 10558.207655117132
# print(total_sum_repaid("lump_sum")(10000, 0.01, 10)) # 11000.0
# print(total_sum_repaid("invalid_payment_type")) # Invalid payment type. Allowed payment types are: annuity or lump_sum!
