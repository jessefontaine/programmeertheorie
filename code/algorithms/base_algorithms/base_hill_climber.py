"""
base_hill_climber.py

Programmeertheorie Rush Hour

Jesse Fontaine - 12693375
Annemarie Geertsema - 12365009
Laura Haverkorn - 12392707

- Contains class BHC (Base Hill Climber).
- Is being used in all the different iterative algorithms.
- Contains functions to reset and correctly run the algorithm.
- Function to save data from run.
"""

from __future__ import annotations
from typing import List, Union

from code.classes import Board, Node
from code.algorithms.random_algorithm import RandomAlg
from code.algorithms.bfs import Bfs
from code.algorithms.dfs import Dfs
from code.algorithms.bdfs import Bdfs
import random


class BHC:
    """
    The Base Hill Climber class that can be used too run a basic hill climber algorithm.
    Impoves solution by improving small parts of the solution.
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
        self.board: Board = board
        self.iteration: int = iteration
        self.min_interval: int = min_interval
        self.max_interval: int = max_interval
        self.start_mode: str = start_mode
        self.improve_mode: str = improve_mode

        self.list_moves_amount: List[int] = []
        self.node_list: List[Node]

    def _make_algorithm(
        self,
        mode: str,
        depth: int = None,
        start_node: Union[Node, None] = None,
        end_node: Union[Node, None] = None,
    ) -> Union[RandomAlg, Bfs, Dfs, Bdfs]:
        """
        Returns algorithm specified by user.
        """

        if mode == "random":
            algorithm: Union[RandomAlg, Bfs, Dfs, Bdfs] = RandomAlg(
                self.board, depth, start_node, end_node
            )
        elif mode == "breadth":
            algorithm = Bfs(self.board, depth, start_node, end_node)
        elif mode == "depth":
            algorithm = Dfs(self.board, depth, start_node, end_node)
        elif mode == "bestdepth":
            algorithm = Bdfs(self.board, depth, start_node, end_node)

        return algorithm

    def _reset_board(self) -> None:
        """
        Resets everything to the initial state.
        """

        self.board.set_board(self.node_list[0].board_rep)

    def _start_solution(
        self, algorithm: Union[RandomAlg, Bfs, Dfs, Bdfs]
    ) -> List[Node]:
        """
        Run the algorithm.
        Returns the steps of the solutions as nodes.
        """
        algorithm.run_algorithm()

        return algorithm.node_list

    def _choose_interval(self) -> int:
        """
        Returns interval within range that is smaller then length of solutions.
        """

        interval: int = random.randint(
            self.min_interval, min(self.max_interval, len(self.node_list) - 1)
        )

        return interval

    def _create_moves_made(self, start_node: Node, final_node: Node) -> None:
        """
        Creates list of all the moves made from given start to final node.
        Counts the number of moves.
        """

        self.moves_made = []

        current: Node = final_node
        self.moves_amount = 0

        # iterate over all nodes untill start node
        while current is not start_node:
            self.moves_made.append(current.step_taken)
            self.moves_amount += 1
            current = current.parent

        self.moves_made = self.moves_made[::-1]

    # def _accept_insert(
    #     self, initial_size: int, insert_size: int, iteration: int
    # ) -> bool:
    #     """
    #     Checks if the new solution is not bigger then the initial solution.
    #     """

    #     return initial_size >= insert_size

    def _accept_insert(
        self, alg: Union[RandomAlg, Bfs, Dfs, Bdfs], start: int, interval: int) -> bool:
        """
        Checks if the new solution is not bigger then the initial solution.
        """

        if alg.node_list[-1].board_rep == self.node_list[start + interval].board_rep:
            return True

        return False

    def _step_algorithm(self, iteration) -> bool:
        """
        Runs the algorithm on a given interval.
        Returns true if inital solution is changed.
        """

        interval: int = self._choose_interval()

        # choose random start point in node list
        start = random.randint(0, len(self.node_list) - interval - 1)

        # do algoritme on small part to get it better
        alg = self._make_algorithm(
            self.improve_mode, interval, self.node_list[start], self.node_list[start + interval]
        )
        alg.run_algorithm()

        # if self._accept_insert(interval, len(alg.node_list), iteration):
        if self._accept_insert(alg, start, interval):
            # put the new improved part of node list into the node list, different when you improve the very last part
            if start + interval == len(self.node_list) - 1:
                self.node_list = self.node_list[:start] + alg.node_list
            else:
                self.node_list[start + interval + 1].new_parent(alg.node_list[-1])

                self.node_list = (
                    self.node_list[:start]
                    + alg.node_list
                    + self.node_list[start + interval + 1 :]
                )

            return True

        return False

    def run_algorithm(self) -> None:
        """
        Runs the algorithm, for given amount of iterations.
        Counts the number of iterations and saves the moves made of the last found solution.
        """

        for i in range(self.iteration):
            # print iteration
            print(f"iteration {i + 1}/{self.iteration}", end="\r")

            self._step_algorithm(i)

            # update data of moves made and add to amount of moves made to list
            self._create_moves_made(self.node_list[0], self.node_list[-1])
            self.list_moves_amount.append(self.moves_amount)

        self.iterations: int = self.iteration + 1
        self.moves_made_in_run: List[List] = [self.moves_made]
