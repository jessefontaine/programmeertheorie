import matplotlib.pyplot as plt
import numpy as np

with open("output/12x12_7_random/Rushhour12x12_7_random_1000.txt", "r") as f:
    lines = f.readlines()

new_list = [int(i.split('\n', 1)[0]) for i in lines]
print(new_list)
print(max(new_list))

plt.hist(new_list, density=True, bins=50)
plt.savefig("output/12x12_7_random/Rushhour12x12_7_random_1000.png")

