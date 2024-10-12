#!/usr/bin/python3

# Implement the following three functions according to the specification.

def add_stock(warehouse, product):
    if product in warehouse and warehouse[product] > 0:
        warehouse[product] = (warehouse[product] + 1)
    else:
        warehouse[product] = 1

def remove_stock(warehouse, product):
    if product in warehouse and warehouse[product] > 0:
        warehouse[product] = (warehouse[product] - 1)
    else:
        print(product + " not in stock")
    if product in warehouse and warehouse[product] == 0:
        del warehouse[product]

def get_stock(warehouse, product):
    if product in warehouse:
        return(warehouse[product])
    else:
        return 0

# The following code is just here as an example for you to try your
# implementation. Uncomment it and run it if you want. Feel free to modify it.
# However, make sure it doesn't break your solution when submitting.

#warehouse = {}
#add_stock(warehouse, "C")    # stock for A should now be 11
#remove_stock(warehouse, "D") # stock for D should now be 1
#remove_stock(warehouse, "C") # The key/value pair for key "C" should be removed
#remove_stock(warehouse, "X") # should print: X not in stock
#get_stock(warehouse, "B")    # should return 15
#get_stock(warehouse, "C")    # should return 0
#print(warehouse)             # to see if it worked

