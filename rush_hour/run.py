from game_board import *
import pandas
import matplotlib.pyplot as plt


def batch_run(filepath, runs):
    list_amount_of_moves = []

    for i in range(runs):
        game = Board(filepath)
        game.step_random()
        df = pandas.DataFrame(game.moves_made, columns=['car', 'move'])
        list_amount_of_moves.append(len(df.index))

    return list_amount_of_moves

#print(batch_run("game_boards/Rushhour6x6_1.csv"))

# batch run
amt_list = batch_run("game_boards/Rushhour6x6_1.csv", 10000)

# plot all runs
plt.hist(amt_list, density=True)
plt.savefig("plots/Rushour6x6_1_10000.png")

# convert to str and write to file
amt_list = [str(x) for x in amt_list]
with open('batch_run_1_10000.txt', 'w') as file:
    file.write('\n'.join(amt_list))
