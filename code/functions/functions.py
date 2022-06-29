"""
functions.py

Programmeertheorie Rush Hour

Jesse Fontaine - 12693375
Annemarie Geertsema - 12365009
Laura Haverkorn - 12392707

- Contains functions used in multiple algorithms.
- Batch runner to run and save results for constructive algorithms.
- Function to run and save results for iterative algorithms.
- Functions to plot the results.
- Function to save the (moves of a) solution.
"""

from __future__ import annotations
from typing import List, Tuple, Union, Optional

from matplotlib import pyplot as plt
import os

from code.algorithms import RandomAlg, Bfs, Dfs, Bdfs, HC, RHC, SA


def batch_runner(
    algorithm: Union[RandomAlg, Bfs, Dfs, Bdfs], runs: int
) -> Tuple[List[int], List[Optional[Tuple[str, int]]]]:
    """
    Run the algorithm multiple times.
    Returns the number of moves and the solution.
    """

    amount_moves_per_runs: List[int] = []
    moves_made_in_runs: List[Optional[Tuple[str, int]]] = []

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


def hill_runner(algorithm: Union[HC, RHC, SA]) -> Tuple[List[int], List[Optional[Tuple[str, int]]], int]:
    """
    Runs the algorithm Hill Climber.
    Returns the number of moves, iterations and the solution.
    """

    algorithm.run_algorithm()

    list_moves_amount: List[int] = algorithm.list_moves_amount
    list_moves_made_in_run: List[List] = algorithm.moves_made_in_run

    return list_moves_amount, list_moves_made_in_run, algorithm.iterations


def plot_steps_to_file(amount_of_steps: List[int], path: str) -> None:
    """
    Plot a figure with the number of steps.
    Write the amount of steps to a csv file.
    Used for constructive algorithms.
    """

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
    """
    Plot a line figure with the number of steps.
    Write the amount of steps to a csv file.
    Used for iterative algorithms.
    """

    list_iteration: List[int] = list(range(0, iteration))

    # trim path if a filetype was specified
    path = path.split(".")[0]

    # plot all runs
    plt.plot(list_iteration, list_moves_amount)

    plt.title(
        f"Hill Climber {len(list_moves_amount) - 1} iterations: game board {path.split('/')[1].split('.')[0]}"
    )
    plt.xlabel("Iterations")
    plt.ylabel("Number of steps")
    plt.savefig(f"{path}.png")

    # convert to str and write to file
    amount_moves_str: List[str] = [str(x) for x in list_moves_amount]
    with open(f"{path}.txt", "w") as file:
        file.write("\n".join(amount_moves_str))


def write_moves_to_file(moves_made: List[Optional[Tuple[str, int]]], path: str) -> None:
    """
    Write the solution to a csv file.
    """

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
