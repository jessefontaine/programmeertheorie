import matplotlib.pyplot as plt
import numpy as np

with open("batch_run_4_10000.txt", "r") as f:
    lines = f.readlines()

new_list = [int(i.split('\n', 1)[0]) for i in lines]
print(new_list)
print(max(new_list))

plt.hist(new_list, density=True, bins=50)
plt.savefig("plots/Rushour9x9_5_10000.png")

