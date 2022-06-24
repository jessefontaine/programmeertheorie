from __future__ import annotations

from matplotlib import pyplot as plt
from typing import List, Tuple, Union
import os

from code import algorithms


def batch_runner(algorithm: Union["Random_Alg", "Bfs", "Dfs"], runs: int):

    amount_moves_per_runs: List[int] = []
    moves_made_in_runs: List[List[Tuple[str, int]]] = []

    for run in range(runs):

        # print status
        print(f"run {run + 1}/{runs}", end="\r")

        # run algorithm on clean board
        algorithm.board.reset_board()
        algorithm.reset_algorithm()
        algorithm.run_algorithm()

        # save data
        amount_moves_per_runs.append(algorithm.moves_amount)
        moves_made_in_runs.append(algorithm.moves_made)

    return amount_moves_per_runs, moves_made_in_runs


def bla(algorithm):
    algorithm.run_algorithm()

    list_moves_amount: List[int] = algorithm.list_moves_amount
    list_moves_made_in_run: List[List[str, int]] = algorithm.moves_made_in_run
    print('j', list_moves_amount)
    
    print('moves', len(algorithm.moves_made))

    return list_moves_amount, list_moves_made_in_run, algorithm.iterations


def plot_steps_to_file(amount_of_steps: List[int], path: str) -> None:

    # trim path if a filetype was specified
    path = path.split(".")[0]

    # plot all runs
    plt.hist(amount_of_steps, density=True, bins=50)

    plt.title(
        f"Density plot {len(amount_of_steps)} runs: game board {path.split('/')[1].split('.')[0]}"
    )
    plt.xlabel("Number of steps")
    plt.ylabel("Density")
    plt.savefig(f"{path}.png")

    # convert to str and write to file
    amount_moves_str: List[str] = [str(x) for x in amount_of_steps]
    with open(f"{path}.txt", "w") as file:
        file.write("\n".join(amount_moves_str))


def plot_line(iteration: int, list_moves_amount: List[int], path: str) -> None:
    print('help', iteration, list_moves_amount)
    list_iteration: List[int] = list(range(1, iteration + 1))
    print(list_iteration)

    # trim path if a filetype was specified
    path = path.split(".")[0]

    # plot all runs
    plt.plot(list_iteration, list_moves_amount)

    plt.title(
        f"Hill Climber {len(list_moves_amount)} iterations: game board {path.split('/')[1].split('.')[0]}"
    )
    plt.xlabel("Iterations")
    plt.ylabel("Number of steps")
    plt.savefig(f"{path}.png")

    # convert to str and write to file
    amount_moves_str: List[str] = [str(x) for x in list_moves_amount]
    with open(f"{path}.txt", "w") as file:
        file.write("\n".join(amount_moves_str))


def steps_amount_to_file(amount_of_steps: List[int], path: str) -> None:

    # trim path if a filetype was specified
    path = path.split(".")[0]

    # convert to str and write to file
    amount_moves_str: List[str] = [str(x) for x in amount_of_steps]
    with open(f"{path}.txt", "w") as file:
        file.write("\n".join(amount_moves_str))


def write_moves_to_file(moves_made: List[List[Tuple[str, int]]], path: str) -> None:
    print(moves_made)

    # trim path if a filetype was specified
    path = path.split(".")[0]

    # make the path to the files
    name: str = path.split("/")[-1]
    folder: str = "/".join(path.split("/")[:-1]) + "/runs"

    # make a subfolder
    try:
        os.makedirs(folder)
    except FileExistsError:
        pass

    # save all the files
    run_moves: List[Tuple[str, int]]
    for run, run_moves in enumerate(moves_made):
        with open(f"{folder}/{name}_run_{run}.csv", "w") as file:
            file.write("car,move\n")
            file.write("\n".join([f"{move[0]},{move[1]}" for move in run_moves]))
