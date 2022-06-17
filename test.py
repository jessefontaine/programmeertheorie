from __future__ import annotations

from argparse import ArgumentParser, Namespace
import os
# import pandas
from typing import Union, List, Tuple

from code.classes import Board
from code.algorithms import First_Alg, Random_Alg, Bfs, Depth_Alg, BDFAlg

a = Board("game_boards/Rushhour6x6_easywin.csv")

b = BDFAlg(a)

b.run_algorithm()