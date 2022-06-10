import matplotlib.pyplot as plt


plt.hist(batch_run("game_boards/Rushhour6x6_1.csv"), density=True)

plt.savefig("plots/Rushour6x6_1_10.png")