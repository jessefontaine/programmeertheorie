from __future__ import annotations

from matplotlib import pyplot as plt
from typing import List, Tuple, Union

# from code.algorithms import Random_Alg, First_Alg, Bfs, Depth_Alg
# from code.classes import Board, Car

def batch_runner(algorithm: Union["Random_Alg", "First_Alg", "Bfs", "Depth_Alg"], runs: int):
    
    amount_moves_per_runs: List[int] = []
    moves_made_in_runs: List[List[Tuple[str, int]]] = []

    for run in range(runs):

        # print status
        # print(f'run {run + 1}/{runs}', end='\r')

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

def plot_steps_to_file(amount_of_steps: List[int], path: str) -> None:

    # trim path if a filetype was specified
    path = path.split('.')[0]

    # plot all runs
    plt.hist(amount_of_steps, density=True, bins=50)

    plt.title(f"Density plot {len(amount_of_steps)} runs: game board {path.split('/')[1].split('.')[0]}")
    plt.xlabel("Number of steps")
    plt.ylabel("Density")
    plt.savefig(f"{path}.png")

    # convert to str and write to file
    amount_moves_str: List[str] = [str(x) for x in amount_of_steps]
    with open(f"{path}.txt", 'w') as file:
        file.write('\n'.join(amount_moves_str))


def steps_amount_to_file(amount_of_steps: List[int], path: str) -> None:

    # trim path if a filetype was specified
    path = path.split('.')[0]

    # convert to str and write to file
    amount_moves_str: List[str] = [str(x) for x in amount_of_steps]
    with open(f"{path}.txt", 'w') as file:
        file.write('\n'.join(amount_moves_str))


def write_moves_to_file(moves_made: List[List[Tuple[str, int]]], path: str) -> None:
    
    # trim path if a filetype was specified
    path = path.split('.')[0]

    run_moves: List[Tuple[str, int]]
    for run_moves in moves_made:
        with open(f'{path}.csv', 'w') as file:
            file.write('car,move\n')
            file.write('\n'.join([f'{move[0]},{move[1]}' for move in run_moves]))
