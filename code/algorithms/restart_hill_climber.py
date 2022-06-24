from __future__ import annotations
from typing import List
from code.algorithms.base_algorithms.base_hill_climber import BHC
from code.classes import Node, Board


class RHC(BHC):
    def __init__(
        self,
        board: Board,
        iteration: int,
        min_interval: int,
        max_interval: int,
        start_mode: str,
        improve_mode: str,
        plateau_iterations: int,
    ):
        super().__init__(
            board, iteration, min_interval, max_interval, start_mode, improve_mode
        )

        self.plateau_iterations: int = plateau_iterations

    def run_algorithm(self) -> None:
        self.iterations: int = 0
        self.moves_made_in_run: List[List[str, int]] = []

        for _ in range(self.iteration):
            print('s')
            # print("begin alg")
            self.node_list: List[Node] = self.start_solution(
                self.make_algorithm(self.start_mode)
            )

            # REMOVE LATER
            # print("begin", len(self.node_list))

            n: int = 0

            while n < self.plateau_iterations:
                print(self.iterations, n)
                # print("begin kleine loop")
                # print("s", len(self.node_list))
                if not self.step_algorithm():
                    # print("ja", n)
                    n += 1
                self.iterations += 1

            #     print("i", len(self.node_list))

            # print("uit while loop")
            # print("end", len(self.node_list))
        
        # print('iterations', self.iterations)

                self.create_moves_made(self.node_list[0], self.node_list[-1])
                self.list_moves_amount.append(self.moves_amount)
            self.moves_made_in_run.append(self.moves_made)
       
        # print("end", self.moves_amount)
