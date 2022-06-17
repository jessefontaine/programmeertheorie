from __future__ import annotations

import random
from typing import Tuple, List

from code.classes import Board, Car
from .node import Node


class RandomAlgBO:

    def __init__(self, board: Board) -> None:
        self.board: Board = board
        self.boards: List = [Node(str(self.board))]

    def _move(self) -> Tuple[str, int]:
        """
        Returns a random move; a tuple with car object and the direction.
        """

        # chooses random move from dictionary
        car_move: str = random.choice(list(self.board.moves_dict.keys()))
        ran_choice = random.choice(self.board.moves_dict[car_move])

        return car_move, ran_choice

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
            self.boards.append(Node(str(self.board)))


        # make and store the final boards
        for i in range(self.board.size[1] - self.board.win_car.position[1] - 2):
            self.boards.append(Node(str(self.board.exit_boards())))


        # for i in range(len(self.boards)):
        #     print(self.boards[i].board_rep)
        #     print(10 * "#")

        # store amount of moves
        self.moves_amount: int = len(self.moves_made)

        return self.boards
