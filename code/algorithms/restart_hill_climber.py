from __future__ import annotations
from typing import List

from code.algorithms.base_algorithms.base_hill_climber import BHC
from code.classes import Node, Board


class RHC(BHC):
    """
    The Restart Hill Climber class that runs a given amount of times the hill climber algorithm.
    Impoves solution by improving small parts of the solution, untill a plateau in improvement is reached.
    """

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
        """
        Runs the algorithm, for given amount of times untill for each solution we reach a plateau.
        Counts the number of total iterations and saves the moves made for each end solution.
        """

        self.iterations: int = 0
        self.moves_made_in_run: List[List] = []

        # run for given amount of begin times
        for i in range(self.iteration):
            # print board
            print(f"board {i + 1}/{self.iteration}", end="\r")

            self._reset_board()

            # make start solution and save node list
            self.node_list = self._start_solution(self._make_algorithm(self.start_mode))

            # make start solution and save node list
            self.list_moves_amount.append(len(self.node_list) - 1)

            self.iterations += 1
            iteration: int = 0
            no_improvement: int = 0

            while no_improvement < self.plateau_iterations:
                # print iteration
                print(
                    f"board {i + 1}/{self.iteration}, iteration {iteration + 1}",
                    end="\r",
                )

                # update no_improvement count
                if not self._step_algorithm(iteration):
                    no_improvement += 1
                else:
                    no_improvement = 0

                self.iterations += 1
                iteration += 1

                # update data of moves made and add to amount of moves made to list
                self._create_moves_made(self.node_list[0], self.node_list[-1])
                self.list_moves_amount.append(self.moves_amount)

            self.moves_made_in_run.append(self.moves_made)
