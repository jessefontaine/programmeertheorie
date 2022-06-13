import matplotlib.pyplot as plt
import numpy as np

with open("output/6x6_1_random/Rushhour6x6_1_random_10000.txt", "r") as f:
    lines = f.readlines()

new_list = [int(i.split('\n', 1)[0]) for i in lines]
print(new_list)
print(max(new_list))

plt.hist(new_list, density=True, bins=50)
plt.title("Density plot 10000 runs: game board 1")
plt.xlabel("Number of steps")
plt.ylabel("Density")
plt.savefig("output/6x6_1_random/Rushhour6x6_1_random_10000.png")

import statistics
print(statistics.mean(new_list), "mean")
