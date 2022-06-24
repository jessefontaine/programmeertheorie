from __future__ import annotations

from typing import Tuple, List

from numpy import infty
from code.algorithms.base_algorithms.hill_climber_alg import HCA
from code.classes import Node, Board


class SHC(HCA):
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

        self.best_solution: Tuple[float, List[Node]] = (infty, [])

    # GEEN BATCHRUN VOOR DEZE DUS RESET NIET NODIG
    def reset_algorithm(self) -> None:
        pass

    # BATCHRUNNER MOET ANDERS!!!!!!!!!!!!!!!!!!!!!!
    def run_algorithm(self) -> None:
        for _ in range(self.iteration):
            print("begin alg")
            self.node_list: List[Node] = self.start_solution(
                self.make_algorithm(self.start_mode)
            )

            # REMOVE LATER
            print("begin", len(self.node_list))

            n: int = 0

            while n < 2:
                print("begin kleine loop")
                print("s", len(self.node_list))
                if not self.step_algorithm():
                    print("ja", n)
                    n += 1
                print("i", len(self.node_list))

            print("uit while loop")
            print("end", len(self.node_list))

            if len(self.node_list) < self.best_solution[0]:
                print("ja")
                self.best_solution = (len(self.node_list), self.node_list)

        print("best", self.best_solution[0])
        self.create_moves_made(self.node_list[0], self.node_list[-1])

        print("end", self.moves_amount)
