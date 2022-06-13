from __future__ import annotations

import random
from typing import Tuple, List

from ..classes import Board, Car


class Random_Alg():

    def __init__(self: Random_Alg, board: Board) -> None:
        self.board: Board = board
        self.moves_made: List[Tuple[str, int]] = []

    def _move(self: Random_Alg) -> Tuple[Car, int]:
        """
            Returns a random move; a tuple with car object and the direction.
        """

        # chooses random move from dictionary
        car_move: Car = random.choice(list(self.board.moves_dict.keys()))
        ran_choice = random.choice(self.board.moves_dict[car_move])

        return car_move, ran_choice

    def run_algorithm(self: Board) -> None:
        """
            Runs the random algoritm until the game is won.
        """

        # make random steps in game untill red car is in win position
        while not self.board.win():
            
            # make and store the moves
            self.moves_made.append(self.board.make_move(*self._move()))

        # make and store the final moves
        self.moves_made.extend(self.board.exit_moves())
