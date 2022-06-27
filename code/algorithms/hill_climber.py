"""
hill_climber.py

Programmeertheorie Rush Hour

Jesse Fontaine - 12693375
Annemarie Geertsema - 12365009
Laura Haverkorn - 12392707

- Contains class HC (Hill Climber).
- Uses the class BHC (Base Hill Climber).
"""

from __future__ import annotations
from typing import List

from code.algorithms.base_algorithms.base_hill_climber import BHC
from code.classes import Node, Board


class HC(BHC):
    """
    The Hill Climber class that runs a hill climber algorithm.
    Impoves solution by improving small parts of the solution, for given amount of iterations.
    """

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

        # make start solution and save node list
        self.node_list: List[Node] = self._start_solution(
            self._make_algorithm(self.start_mode)
        )

        self.list_moves_amount.append(len(self.node_list) - 1)
