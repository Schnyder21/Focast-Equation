from math import sin, cos, radians
import random
import sys
import os

print("Forcasting equation")


forcast_list = [3]
Actuall_list = [3, 4, 4.5, 3, 2, 2, 3, 3.5]

for x in range(1, 14):
    forcast_number= forcast_list[x-1] + ((.5)*(Actuall_list[x-1] - forcast_list[x-1]))
    forcast_list.append(forcast_number)
    
    if x >= len(Actuall_list) :
        Actuall_list.append( random.uniform(0, 10))
    
print('Forcast = ', forcast_list)
print('Actual = ', Actuall_list)
