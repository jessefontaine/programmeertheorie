from __future__ import annotations

from typing import List, Union

from code.classes import Board, Node

from code.algorithms.random_algorithm import RandomAlg
from code.algorithms.bfs import Bfs
from code.algorithms.dfs import Dfs
from code.algorithms.bdfs import Bdfs
import random


class BHC:
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

        # self.node_list: List[Node] = self.begin_solution(self.make_algorithm(start_mode))
        # self.start_node_list: List[Node] = self.start_solution(
        #     self.make_algorithm(start_mode)
        # )
        # print(len(self.start_node_list))
        # self.node_list: List[Node] = self.start_node_list

        # # REMOVE LATER
        # print('begin', len(self.node_list))

    def make_algorithm(
        self,
        mode: str,
        start_node: Union[Node, None] = None,
        end_node: Union[Node, None] = None,
    ) -> Union[RandomAlg, Bfs, Dfs, Bdfs]:
        # RANDOM FIXEN DAT JE BEGIN EN START PUNT KAN DOEN
        if mode == "random":
            algorithm: Union[RandomAlg, Bfs, Dfs, Bdfs] = RandomAlg(
                self.board, start_node, end_node
            )
        elif mode == "breadth":
            algorithm = Bfs(self.board, 300, start_node, end_node)
        elif mode == "depth":
            algorithm = Dfs(self.board, 300, start_node, end_node)
        elif mode == "bestdepth":
            algorithm = Bdfs(self.board, 300, start_node, end_node)

        return algorithm

    # def reset_algorithm(self):
    #     # DOE HIER NOG WAT AAN
    #     self.node_list = self.start_node_list
    #     self.moves_made = []

    def start_solution(self, algorithm: Union[RandomAlg, Bfs, Dfs, Bdfs]) -> List[Node]:
        algorithm.run_algorithm()

        return algorithm.node_list

    # def new_solution(self, algorithm: Union[RandomAlg, Bfs, Dfs, Bdfs]) -> List[Node]:
    #     raise NotImplementedError

    def choose_interval(self) -> int:
        interval: int = len(self.node_list)

        # want interval that is not bigger then node list
        while interval >= len(self.node_list):
            interval = random.randint(self.min_interval, self.max_interval)

        return interval

    def create_moves_made(self, start_node: Node, final_node: Node) -> None:
        self.moves_made = []

        current: Node = final_node
        self.moves_amount = 0
        while current is not start_node:
            self.moves_made.append(current.step_taken)
            self.moves_amount += 1
            current = current.parent

        self.moves_made = self.moves_made[::-1]

    def accept_insert(
        self, initial_size: int, insert_size: int, iteration: int
    ) -> bool:
        return initial_size >= insert_size

    def step_algorithm(self, iteration) -> bool:
        interval: int = self.choose_interval()

        # choose ranodm start point in node list
        start = random.randint(0, len(self.node_list) - interval - 1)

        # do algoritme on small part to get it better
        alg = self.make_algorithm(
            self.improve_mode, self.node_list[start], self.node_list[start + interval]
        )
        alg.run_algorithm()

        if self.accept_insert(interval, len(alg.node_list), iteration):
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
        for i in range(self.iteration):

            print(i)
            self.step_algorithm()

            self.create_moves_made(self.node_list[0], self.node_list[-1])
            # print(self.moves_amount, self.moves_made)
            self.list_moves_amount.append(self.moves_amount)

        print(self.list_moves_amount)

        self.iterations: int = self.iteration
        self.moves_made_in_run: List[List[str, int]] = [self.moves_made]

        # print(self.list_moves_amount)

        # print(self.list_moves_amount)

        # print("end", self.moves_amount)

    # def run_algorithm(self) -> None:
    #     print('k', len(self.node_list))
    #     #MOET NOG EEN MAX OPKOMEN
    #     for _ in range(self.iteration):
    #         interval: int = self.choose_interval()

    #         # choose ranodm start point in node list
    #         start = random.randint(0, len(self.node_list) - interval - 1)

    #         # do algoritme on small part to get it better
    #         alg = self.make_algorithm(self.improve_mode, self.node_list[start], self.node_list[start + interval])
    #         alg.run_algorithm()

    #         if interval <= len(alg.node_list):
    #             continue

    #         # put the new improved part of node list into the node list, different when you improve the very last part
    #         if start + interval == len(self.node_list) - 1:
    #             self.node_list = self.node_list[:start] + alg.node_list
    #         else:
    #             self.node_list[start + interval + 1].new_parent(alg.node_list[-1])

    #             self.node_list = self.node_list[:start] + alg.node_list + self.node_list[start + interval + 1:]

    #     self.create_moves_made(self.node_list[0], self.node_list[-1])

    #     print('end', self.moves_amount)
