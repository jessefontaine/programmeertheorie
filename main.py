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
from typing import Union, List, Tuple, Optional

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
from code.settings import DEPTH, MAX_INTERVAL, MIN_INTERVAL, PLATEAU


class InvalidAlgorithmError(Exception):
    """
    Invalid algorithm exception.
    """


def main(infile: str, outfolder: str, mode: str, runs: int, output_moves: bool):
    """
    Makes and runs the given algorithm.
    Plots the output and saves the output when output_moves True.
    """

    board: Board = Board(infile)

    # make the given algorithm
    if mode == "random":
        constructive_algorithm: Union[RandomAlg, Bfs, Dfs, Bdfs] = RandomAlg(board)
    elif mode == "breadth":
        constructive_algorithm = Bfs(board, DEPTH)
    elif mode == "depth":
        constructive_algorithm = Dfs(board, DEPTH)
    elif mode == "bestdepth":
        constructive_algorithm = Bdfs(board, DEPTH)
    elif "hill" in mode:
        mode, start_mode, improve_mode = (
            mode.split("/")[0],
            mode.split("/")[1],
            mode.split("/")[2],
        )

        if mode not in ["hill", "restarthill", "sahill"]:
            raise InvalidAlgorithmError("Given algorithm does not exist.")
        elif start_mode not in ["random", "breadth", "depth", "bestdepth"]:
            raise InvalidAlgorithmError("Given algorithm does not exist or can not be used to find a starting solution.")
        elif improve_mode not in ["random", "breadth", "depth", "bestdepth"]:
            raise InvalidAlgorithmError("Given algorithm does not exist or can not be used to improve.")

        if mode == "hill":
            iterative_algorithm: Union[HC, RHC, SA] = HC(
                board, runs, MIN_INTERVAL, MAX_INTERVAL, start_mode, improve_mode
            )
        elif mode == "restarthill":
            iterative_algorithm = RHC(
                board,
                runs,
                MIN_INTERVAL,
                MAX_INTERVAL,
                start_mode,
                improve_mode,
                PLATEAU,
            )
        elif mode == "sahill":
            iterative_algorithm = SA(
                board, runs, MIN_INTERVAL, MAX_INTERVAL, start_mode, improve_mode
            )
    else:
        raise InvalidAlgorithmError("Given algorithm does not exist.")

    try:
        os.makedirs(outfolder)
    except FileExistsError:
        pass

    # run the algorithm and output the result to a plot
    if "hill" in mode:
        filepath: str = f"{outfolder}/{infile.split('/')[-1].split('.')[0]}_{mode}_{start_mode}_{improve_mode}_{runs}"

        list_moves_amount: List[int]
        moves_made: List[Optional[Tuple[str, int]]]
        iterations: int

        list_moves_amount, moves_made, iterations = hill_runner(iterative_algorithm)

        plot_line(iterations, list_moves_amount, filepath)
    else:
        filepath = f"{outfolder}/{infile.split('/')[-1].split('.')[0]}_{mode}_{runs}"

        # run the algorithm and collect the data
        amount_moves: List[int]

        amount_moves, moves_made = batch_runner(constructive_algorithm, runs)

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

    # if the puzzle does not exist, exit
    if not os.path.exists(args.input_csv):
        print(f"The file {args.input_csv} does not exist")
        sys.exit(1)

    if int(args.runs) <= 0:
        print(
            f"The runs {args.runs} is a negative or zero number, use a positive integer."
        )
        sys.exit(2)

    # call main with cla's
    main(
        args.input_csv, args.output_folder, args.mode, int(args.runs), args.output_moves
    )
