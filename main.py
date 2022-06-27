"""
main.py

Programmeertheorie Rush Hour

Jesse Fontaine - 12693375
Annemarie Geertsema - 12365009
Laura Haverkorn - 12392707

- Entry point of the code.
- Makes sure argument parser gets runned.
"""

from __future__ import annotations
from typing import Union, List

from argparse import ArgumentParser, Namespace
import os
import sys

from code.classes import Board
from code.algorithms import RandomAlg, Bfs, Dfs, Bdfs, HC, RHC, SA
from code.functions import (
    batch_runner,
    hill_runner,
    plot_steps_to_file,
    plot_line,
    write_moves_to_file,
)

MIN_INTERVAL = 4
MAX_INTERVAL = 15
PLATEAU = 150


class InvalidAlgorithmError(Exception):
    """
    Invalid algorithm exception.
    """

    pass


def main(infile: str, outfolder: str, mode: str, runs: int, output_moves: bool):
    """
    Makes and runs the given algorithm.
    Plots the output and saves the output when output_moves True.
    """

    board: Board = Board(infile)

    # make the given algorithm
    if mode == "random":
        algorithm: Union[RandomAlg, Bfs, Dfs, Bdfs, HC, RHC, SA] = RandomAlg(board)
    elif mode == "breadth":
        algorithm = Bfs(board, 300)
    elif mode == "depth":
        algorithm = Dfs(board, 300)
    elif mode == "bestdepth":
        algorithm = Bdfs(board, 300)
    elif "hill" in mode:
        mode, start_mode, improve_mode = (
            mode.split("/")[0],
            mode.split("/")[1],
            mode.split("/")[2],
        )

        if mode == "hill":
            algorithm = HC(board, runs, MIN_INTERVAL, MAX_INTERVAL, start_mode, improve_mode)
        elif mode == "restarthill":
            algorithm = RHC(
                board, runs, MIN_INTERVAL, MAX_INTERVAL, start_mode, improve_mode, PLATEAU
            )
        elif mode == "sahill":
            algorithm = SA(board, runs, MIN_INTERVAL, MAX_INTERVAL, start_mode, improve_mode)
    else:
        raise InvalidAlgorithmError("Given algorithm does not exist")

    try:
        os.makedirs(outfolder)
    except FileExistsError:
        pass

    # run the algorithm and output the result to a plot
    if "hill" in mode:
        filepath: str = f"{outfolder}/{infile.split('/')[-1].split('.')[0]}_{mode}_{start_mode}_{improve_mode}_{runs}"

        list_moves_amount, moves_made, iterations = hill_runner(algorithm)

        plot_line(iterations, list_moves_amount, filepath)
    else:
        filepath = (
            f"{outfolder}/{infile.split('/')[-1].split('.')[0]}_{mode}_{runs}"
        )

        # run the algorithm and collect the data
        amount_moves: List[int]

        amount_moves, moves_made = batch_runner(algorithm, runs)

        # plot steps for all runs
        plot_steps_to_file(amount_moves, filepath)

    # print the moves if user marked for it
    if output_moves:
        write_moves_to_file(moves_made, filepath)


if __name__ == "__main__":

    # setup cla parser
    parser: ArgumentParser = ArgumentParser(description="Run the Rush Hour solver")

    # add cla's
    parser.add_argument("input_csv", help="gameboard csv file")
    parser.add_argument("output_folder", help="folder for output")
    parser.add_argument("mode", help="solver mode")
    parser.add_argument("runs", help="amount of runs")

    # optional arguments
    parser.add_argument(
        "-m",
        "--output_moves",
        action="store_true",
        help="output moves made to csv file(s)",
    )

    # read cla's
    args: Namespace = parser.parse_args()

    # If the puzzle does not exist, exit
    if not os.path.exists(args.input_csv):
        print(f"The file {args.input_csv} does not exist")
        sys.exit(1)

    # call main with cla's
    main(
        args.input_csv, args.output_folder, args.mode, int(args.runs), args.output_moves
    )
