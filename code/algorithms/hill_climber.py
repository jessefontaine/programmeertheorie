from __future__ import annotations
from typing import Tuple, List, Set, Union
from .random_alg_new import RandomAlg
from code.classes import Board
from code.functions.functions import write_moves_to_file
from code.classes import Node
import random


class HillClimber:

    def __init__(self, board: Board):
        self.board: Board = board

        a = RandomAlg(self.board)
        a.run_algorithm()
        self.states: List[Node] = a.states

    def run_algorithm(self) -> None:
        interval = 10
        start = random.randint(0, len(self.states) - interval)
        print(start)
        print('')

        self.moves_made = []

        # store amount of moves
        self.moves_amount: int = 0

"""
from __future__ import annotations

from argparse import ArgumentParser, Namespace
import os
import random
from typing import Union, List, Tuple

from code.classes import Board
from code.algorithms import First_Alg, Random_Alg, Bfs, BDFAlg, BestDepthFirst

a = Board("game_boards/Rushhour6x6_easywin.csv")

b = BestDepthFirst(a)

b.run_algorithm()

# solution = b.run_algorithm()

# print(solution)

# print(len(solution))

# interval = random.randint(7, 12)
# start = random.randint(0, len(solution) - interval)
# print(start, start + interval, interval)

# a.set_board(solution[start].board_rep)
# x = Bfs(a, 20, solution[start + interval].board_rep)

# solution2 = x.run_algorithm()
# print(solution2)
"""
