import random
import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt

list_of_random = [0]*22

copy = list_of_random

# print(len(list_of_random))
for i in range(0,3):
    for x in range(0, 3): # this line will ensure 4 element insertion
        list_of_random.insert(random.randrange(0, len(list_of_random)-1), 1)
        copy.append(list_of_random)


print(copy)
