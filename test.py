from __future__ import annotations

from argparse import ArgumentParser, Namespace
import os
import random
from typing import Union, List, Tuple

from code.classes import Board
from code.algorithms import First_Alg, Random_Alg, Bfs, Depth_Alg, BDF_Alg, RandomAlgBO

a = Board("game_boards/Rushhour6x6_easywin.csv")

b = RandomAlgBO(a)

solution = b.run_algorithm()

print(solution)

print(len(solution))

interval = random.randint(7, 12)
start = random.randint(0, len(solution) - interval)
print(start, start + interval, interval)

a.set_board(solution[start].board_rep)
x = Bfs(a, 20, solution[start + interval].board_rep)

solution2 = x.run_algorithm()
print(solution2)
