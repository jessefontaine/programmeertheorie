from __future__ import annotations

import random
from typing import Tuple, List
import time

from code.algorithms.random_algorithm import RandomAlg
from code.algorithms.bfs import Bfs
from code.algorithms.base_algorithm import BaseAlg
from code.classes import Board, Node


class HillClimber(BaseAlg):

    def __init__(self, board: Board):
        super().__init__(board=board)

    def algorithm(self) -> Node:

        # generate a solution
        start_alg = RandomAlg(self.board)
        start_node, end_node = start_alg.run_algorithm()
        node_list = start_alg.node_list
        moves_amount = start_alg.moves_amount

        # end_time = time.time() + 10

        # while time.time() < end_time:

        

        # pick two random nodes
        node_1, node_2, route_length = self.pick_nodes(node_list, moves_amount)

        # run algorithm between two nodes
        iter_alg = RandomAlg(self.board, node_1, node_2)
        iter_start_node, iter_end_node = iter_alg.run_algorithm

        # check if new route is same or better
        if iter_alg.moves_amount <= route_length:
            
            # if so implant the new route
            
        pass
