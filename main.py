from __future__ import annotations

from argparse import ArgumentParser, Namespace
import os
import sys
from typing import Union, List, Tuple
# from code.algorithms.hill_climber_repeat import HCR

from code.classes import Board
from code.algorithms import RandomAlg, Bfs, Dfs, Bdfs, HC, RHC, SHC  # , HillClimberNew
from code.functions import (
    batch_runner,
    bla,
    plot_steps_to_file,
    plot_line,
    steps_amount_to_file,
    write_moves_to_file,
)


class InvalidAlgorithmError(Exception):
    pass


def main(infile: str, outfolder: str, mode: str, runs: int, output_moves: bool):

    board: Board = Board(infile)

    if mode == "random":
        algorithm: Union[RandomAlg, Bfs, Dfs, Bdfs, HC, RHC, SHC] = RandomAlg(board)
    elif mode == "breadth":
        algorithm = Bfs(board, 300)
    elif mode == "depth":
        algorithm = Dfs(board, 300)
    elif mode == "bestdepth":
        algorithm = Bdfs(board, 300)
    elif mode == "hill":
        iteration = 1000
        algorithm = HC(board, iteration, 4, 20, "random", "breadth")
    elif mode == "restarthill":
        algorithm = RHC(board, 5, 4, 40, "random", "depth")
    elif mode == "steephill":
        algorithm = SHC(board, 5, 4, 40, "random", "depth")
    else:
        raise InvalidAlgorithmError("Given algorithm does not exist")

    try:
        os.makedirs(outfolder)
    except FileExistsError:
        pass

    filepath: str = f"{outfolder}/{infile.split('/')[-1].split('.')[0]}_{mode}_{runs}"

    if mode == "hill":
        list_moves_amount, moves_made = bla(algorithm)
        moves_made = [moves_made]

        plot_line(iteration, list_moves_amount, filepath)
    else:
        # run the algorithm and collect the data
        amount_moves: List[int]

        amount_moves, moves_made = batch_runner(algorithm, runs)
        plot_steps_to_file(amount_moves, filepath)
        steps_amount_to_file(amount_moves, filepath)

        # plot steps for all runs
        plot_steps_to_file(amount_moves, filepath)
        steps_amount_to_file(amount_moves, filepath)

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
        "-m", "--output_moves", action="store_true", help="Output moves made to file(s)"
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
