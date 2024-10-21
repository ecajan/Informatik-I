#!/usr/bin/env python3


# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def hamming_dist(signal_1, signal_2):
    rtrnls =[]
    if len(signal_1["data"]) == len(signal_2) and len(signal_1["data"]) != 0:
        signal_1_data = signal_1["data"]
        for datai in range(len(signal_1_data)):
            tempcnt = 0
            if len(signal_1_data[datai]) != len(signal_2[datai]):
                #print(signal_1_data[datai])
                #print(signal_2[datai])
                return "Sensor defect detected"
            for i in range(len(signal_1_data[datai])):
                if signal_1_data[datai][i] != signal_2[datai][i]:
                    tempcnt += 1
            if tempcnt >= 1:
                rtrnls.append((signal_1_data[datai], signal_2[datai], tempcnt))
                
        return rtrnls
  



    else:
        return "Empty signal on at least one of the sensors"

# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001001", "11110011", "01111011", "11001101", "00011011"]}
signal_sensor_2 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")
print(hamming_dist(signal_sensor_1, signal_sensor_2))
