from __future__ import annotations

import random
from typing import Tuple, List

from code.classes import Board, Car


class Random_Alg():

    def __init__(self, board: Board) -> None:
        self.board: Board = board

    def _move(self) -> Tuple[str, int]:
        """
        Returns a random move; a tuple with car object and the direction.
        """

        # chooses random move from dictionary
        # car_move: str = random.choice(list(self.board.moves_dict.keys()))
        ran_move = random.choice(self.board.possible_moves)

        return ran_move
    
    def reset_algorithm(self):
        self.states = [self.start_node]
        self.unique_board_setups = set([self.start_node.board_rep])

    def run_algorithm(self) -> None:
        """
        Runs the random algoritm until the game is won.
        """

        # clear the moves made list
        self.moves_made: List[Tuple[str, int]] = []

        # make random steps in game untill red car is in win position
        while not self.board.win():
            
            # make and store the moves
            self.moves_made.append(self.board.make_move(*self._move()))

        # make and store the final moves
        self.moves_made.extend(self.board.exit_moves())

        # store amount of moves
        self.moves_amount: int = len(self.moves_made)
