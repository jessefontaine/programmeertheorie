from __future__ import annotations

from typing import List, Tuple, Union

from ..algorithms import Random_Alg, First_Alg
from ..classes import Board, Car

def batch_runner(algorithm: Union[Random_Alg, First_Alg], runs: int):
    
    amount_moves_per_runs: List[int] = []
    moves_made_in_runs: List[List[Tuple[str, int]]] = []

    for run in range(runs):

        # print status
        print(f'run {run + 1}/{runs}', end='\r')

        # run algorithm on clean board
        algorithm.board.reset_board()
        algorithm.run_algorithm()

        # save data
        amount_moves_per_runs.append(algorithm.moves_amount)
        moves_made_in_runs.append(algorithm.moves_made)

    return amount_moves_per_runs, moves_made_in_runs