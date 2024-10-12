#!/usr/bin/python3

def square_numbers(numbers):
    '''this one just serves as an example'''
    return [ number ** 2 for number in numbers ]

def even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]

def all_even(numbers):
    return [round(number) if round(number) % 2 == 0 else round(round(number) + 1) for number in numbers]

def only_integers(numbers):
    return [number for number in numbers if type(number) == int]

def only_positive(numbers):
    return [abs(number) for number in numbers]

def from_1_to_1000_containing_a(a):
    return [x for x in range(1, 1001) if str(a) in str(x)] # up to shut the fuck up

def multiple_of_a_and_greater_than_b(numbers, a, b):
    return [x for x in numbers if x % a == 0 and x > b]

#number_list = [-1, 0, 1, 1.5, 1.3, 2, 3, 4, 5, 6, 7, 8, 9]
#print(multiple_of_a_and_greater_than_b(number_list, 2, 4))