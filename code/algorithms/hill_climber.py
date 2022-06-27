from __future__ import annotations
from typing import List
from code.algorithms.base_algorithms.base_hill_climber import BHC
from code.classes import Node, Board


class HC(BHC):
    def __init__(
        self,
        board: Board,
        iteration: int,
        min_interval: int,
        max_interval: int,
        start_mode: str,
        improve_mode: str,
    ):
        super().__init__(
            board, iteration, min_interval, max_interval, start_mode, improve_mode
        )
        self.start_node_list: List[Node] = self._start_solution(
            self._make_algorithm(self.start_mode)
        )

        self.node_list: List[Node] = self.start_node_list

        self.list_moves_amount.append(len(self.node_list) - 1)
