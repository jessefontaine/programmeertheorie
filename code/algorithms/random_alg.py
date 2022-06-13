from __future__ import annotations
from ..classes import Board, Car
from typing import Tuple, List
import random


class Random_Alg():

    def __init__(self: Random_Alg, board: Board) -> None:
        self.board = board

    def move(self: Random_Alg, dict: dict[Car, List[int]]) -> Tuple[Car, int]:
        """
            Returns a random move; a tuple with car object and the direction.
            Requires a dictionary with all possible moves.
        """

        # chooses random move from dictionary
        car_move = random.choice(list(dict.items()))
        ran_choice = random.choice(car_move[1])

        return car_move[0], ran_choice

    def step(self) -> None:
        """
            Runs the random algoritm until the game is won.
        """

        # make random steps in game untill red car is in win position
        while not self.board.win():
            pos_moves = self.board.possible_moves()

            move = self.move(pos_moves)

            self.board.make_move(*move)

            self.board.update_grid()

        self.board.exit_moves()
