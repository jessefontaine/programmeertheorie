from __future__ import annotations

from argparse import ArgumentParser, Namespace
import matplotlib.pyplot as plt
import os
import pandas
from typing import Union, List, Tuple

from code.classes import Board
from code.algorithms import First_Alg, Random_Alg, Breadth_Alg
from code.functions import batch_runner


def main(infile: str, outfolder: str, mode: str, runs: int):

    board: Board = Board(infile)

    if mode == 'random':
        algorithm: Union[Random_Alg, First_Alg, Breadth_Alg] = Random_Alg(board)
    elif mode == 'first':
        algorithm = First_Alg(board)

    elif mode == 'breadth':
        algorithm = Breadth_Alg(board)
    else:
        print("TODO")
    
    amount_moves: List[int]
    moves_made: List[List[Tuple[str, int]]]
    amount_moves, moves_made = batch_runner(algorithm, runs)

    try:
        os.makedirs(outfolder)
    except FileExistsError:
        pass

    # plot all runs
    plt.hist(amount_moves, density=True, bins=50)

    plt.savefig(
        f"{outfolder}/{infile.split('/')[-1].split('.')[0]}_{mode}_{runs}.png")

    # convert to str and write to file
    amount_moves_str: List[str] = [str(x) for x in amount_moves]
    with open(f"{outfolder}/{infile.split('/')[-1].split('.')[0]}_{mode}_{runs}.txt", 'w') as file:
        file.write('\n'.join(amount_moves_str))


if __name__ == "__main__":

    # setup cla parser
    parser: ArgumentParser = ArgumentParser(
        description="Run the rush-hour solver")

    # add cla's
    parser.add_argument('input_csv', help='gameboard csv file')
    parser.add_argument('output_folder', help='folder for output')
    parser.add_argument('mode', help='solver mode')
    parser.add_argument('runs', help='amount of runs')

    # read cla's
    args: Namespace = parser.parse_args()

    # call main with cla's
    main(args.input_csv, args.output_folder, args.mode, int(args.runs))
