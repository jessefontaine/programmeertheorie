from game_board import *
import pandas
import matplotli as plt


def batch_run(filepath):
    list_amount_of_moves = []

    for i in range(10):
        game = Board(filepath)
        game.step_random()
        df = pandas.DataFrame(game.moves_made, columns=['car', 'move'])
        list_amount_of_moves.append(len(df.index))

    return list_amount_of_moves

print(batch_run("game_boards/Rushhour6x6_1.csv"))

plt.hist(batch_run("game_boards/Rushhour6x6_1.csv"))

plt.