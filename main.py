from __future__ import annotations

from argparse import ArgumentParser, Namespace
import os
# import pandas
from typing import Union, List, Tuple

from code.classes import Board
from code.algorithms import Random_Alg, Bfs, Dfs
from code.functions import batch_runner, plot_steps_to_file, steps_amount_to_file, write_moves_to_file


def main(infile: str, outfolder: str, mode: str, runs: int, output_moves: bool):

    board: Board = Board(infile)

    if mode == 'random':
        algorithm: Union[Random_Alg, Bfs, Dfs] = Random_Alg(board)
    elif mode == 'first':
        # algorithm = First_Alg(board)
        pass

    elif mode == 'breadth':
        algorithm = Bfs(board, 50)
    elif mode == "depth":
        algorithm = Dfs(board, 50)
    else:
        print("TODO")
    
    # run the algorithm and collect the data
    amount_moves: List[int]
    moves_made: List[List[Tuple[str, int]]]
    amount_moves, moves_made = batch_runner(algorithm, runs)

    try:
        os.makedirs(outfolder)
    except FileExistsError:
        pass

    # plot steps for all runs
    plot_steps_to_file(amount_moves, f"{outfolder}/{infile.split('/')[-1].split('.')[0]}_{mode}_{runs}")
    steps_amount_to_file(amount_moves, f"{outfolder}/{infile.split('/')[-1].split('.')[0]}_{mode}_{runs}")

    # print the moves if user marked for it
    if output_moves:
        write_moves_to_file(moves_made, f"{outfolder}/{infile.split('/')[-1].split('.')[0]}_{mode}_{runs}")


if __name__ == "__main__":

    # setup cla parser
    parser: ArgumentParser = ArgumentParser(
        description="Run the rush-hour solver")

    # add cla's
    parser.add_argument('input_csv', help='gameboard csv file')
    parser.add_argument('output_folder', help='folder for output')
    parser.add_argument('mode', help='solver mode')
    parser.add_argument('runs', help='amount of runs')

    # optional arguments
    parser.add_argument("-m", "--output_moves", action='store_true', help="Output moves made to file(s)")

    # read cla's
    args: Namespace = parser.parse_args()

    # call main with cla's
    main(args.input_csv, args.output_folder, args.mode, int(args.runs), args.output_moves)
