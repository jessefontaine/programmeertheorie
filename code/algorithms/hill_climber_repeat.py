from __future__ import annotations
from platform import node
from typing import Tuple, List, Set, Union
from xml.dom.minicompat import NodeList
from .hill_climber_alg import HCA
from code.classes import Node, Board


class HCR(HCA):

    def __init__(self, board: Board, iteration: int, min_interval: int, max_interval: int, start_mode: str, improve_mode: str):
        super().__init__(board, iteration, min_interval, max_interval, start_mode, improve_mode)
        self.start_node_list: List[Node] = self.start_solution(
            self.make_algorithm(self.start_mode)
        )
        # REMOVE LATER
        print(len(self.start_node_list))

        self.node_list: List[Node] = self.start_node_list

        # REMOVE LATER
        print('begin', len(self.node_list))
