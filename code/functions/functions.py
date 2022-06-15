from __future__ import annotations

from typing import List, Tuple, Union

from code.algorithms import Random_Alg, First_Alg, Breadth_Alg
# from code.classes import Board, Car

def batch_runner(algorithm: Union[Random_Alg, First_Alg, Breadth_Alg], runs: int):
    
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

def merge_moves(moves: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
        """
            Merges moves together.
            Deletes the move if direction is 0.
        """
        i = 0

        # loop over moves made
        while i < len(moves) - 1:
            # check if next move is done with the same car
            if moves[i][0] == moves[i + 1][0]:
                moves[i] = (moves[i][0], moves[i][1] + moves[i + 1][1])
                # delete the move which is added
                del moves[i + 1]
                
                # if the move is undone, delete move
                if moves[i][1] == 0:
                    del moves[i]
                    i -= 1
                i -= 1
            i += 1

        return moves
