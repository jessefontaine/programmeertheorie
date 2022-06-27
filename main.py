from __future__ import annotations

from argparse import ArgumentParser, Namespace
import os
import sys
from typing import Union, List

from code.classes import Board
from code.algorithms import RandomAlg, Bfs, Dfs, Bdfs, HC, RHC, SA
from code.functions import (
    batch_runner,
    hill_runner,
    plot_steps_to_file,
    plot_line,
    write_moves_to_file,
)


class InvalidAlgorithmError(Exception):
    pass


def main(infile: str, outfolder: str, mode: str, runs: int, output_moves: bool):

    board: Board = Board(infile)

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
            algorithm = HC(board, runs, 4, 10, start_mode, improve_mode)
        elif mode == "restarthill":
            plateau_iteration = 20
            algorithm = RHC(
                board, runs, 4, 10, start_mode, improve_mode, plateau_iteration
            )
        elif mode == "sahill":
            algorithm = SA(board, runs, 4, 10, start_mode, improve_mode)
    else:
        raise InvalidAlgorithmError("Given algorithm does not exist")

    try:
        os.makedirs(outfolder)
    except FileExistsError:
        pass

    if "hill" in mode:
        filepath: str = f"{outfolder}/{infile.split('/')[-1].split('.')[0]}_{mode}_{start_mode}_{improve_mode}_{runs}"

        list_moves_amount, moves_made, iterations = hill_runner(algorithm)

        plot_line(iterations, list_moves_amount, filepath)    
    else:
        filepath: str = (
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
