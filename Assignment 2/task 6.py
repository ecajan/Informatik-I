#!/usr/bin/env python3
import math

def zoo(number):
    my_list = [
        (math.floor(number)), 
        (math.ceil(number)), 
        (math.atan(number)), 
        (tuple(math.modf(number))), 
        (math.nextafter(number, -math.inf, steps=1)), 
        (math.cbrt(number))]

    my_tuple = tuple(my_list)

    return(my_tuple)
