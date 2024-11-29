#!/usr/bin/env python3

# Count the number of recursive calls.
# Not relevant to solve the exercise but just to show the performance improvement.
count = 0


# Change the functions below to calculate the knapsack value.
# Use the variable lookup_table to store intermediate results to improve performance.
# Don't forget to pass it as an argument to the recursive calls.
def knapsack(capacity, weights, values, lookup_table=None):
    # Only for performance measurement. You can ignore this line or event remove it.
    global count
    count += 1

    if lookup_table is None:                                    #Not used
        lookup_table = {}

    if len(weights) > 1:
        vvalues, vweights = zip(*sorted(zip(values, weights)))  #Sort both values and weights list to feature most "V"aluble at the end
        wweights, wvalues = zip(*sorted(zip(weights, values)))  #Sort both values and weights list to feature most "W"eighted at the end
    else:                                                       #Incase of only one remaining item in list, just copy the list
        vvalues, vweights = values, weights
        wweights, wvalues = weights, values
    if len(weights) == 0:
        return 0
    if wweights[0] > capacity:                                                                              #If least weighted item does not fit remaining capacity:
        return 0                                                                                            #return 0
    elif wweights[0] == capacity:                                                                           #If least weighted item does just fit remaining capacity:
        return wvalues[0]                                                                                   #return value of that                                                               
    elif vweights[-1] <= capacity:                                                                          #If weight of most valuable object fits:
        return vvalues[-1] + knapsack(capacity - vweights[-1], vweights[:-1], vvalues[:-1], lookup_table)   #Return value of that combined with recursive call of function with remaining objects
    elif vweights[-1] > capacity:                                                                           #If weight of most valuable object does not fit capacity:
        return knapsack(capacity, vweights[:-1], vvalues[:-1], lookup_table)                                #Return recursive call of function without that object


if __name__ == "__main__":
    # The following lines call the function and prints the return
    # value to the Console. This way you can check what it does.
    print("The maximum value in the knapsack is:", knapsack(50, [10, 20, 30], [60, 100, 120]))
    print("Number of function calls:", count)
