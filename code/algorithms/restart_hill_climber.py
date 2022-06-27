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
        self.node_list: List[Node] = [Node(str(self.board))]

    def run_algorithm(self) -> None:
        self.iterations: int = 0
        self.moves_made_in_run: List[List] = []

        for i in range(self.iteration):
            # print board
            print(f"board {i + 1}/{self.iteration}", end="\r")

            self.reset_board()

            self.node_list = self.start_solution(
                self.make_algorithm(self.start_mode)
            )

            self.list_moves_amount.append(len(self.node_list) - 1)
            self.iterations += 1

            iteration: int = 0
            n: int = 0

            while n < self.plateau_iterations:
                # print iteration
                print(f"board {i + 1}/{self.iteration}, iteration {iteration + 1}", end="\r")

                if not self.step_algorithm(iteration):
                    n += 1
                else:
                    n = 0

                self.iterations += 1
                iteration += 1

                self.create_moves_made(self.node_list[0], self.node_list[-1])
                self.list_moves_amount.append(self.moves_amount)
            
            self.moves_made_in_run.append(self.moves_made)
