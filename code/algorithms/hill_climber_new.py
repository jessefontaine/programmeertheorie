from __future__ import annotations
from platform import node
from typing import Tuple, List, Set, Union
from xml.dom.minicompat import NodeList
from .random_alg_new import RandomAlg
from .bfs import Bfs
from code.classes import Board
from code.functions.functions import write_moves_to_file
from code.classes import Node
import random


class HillClimberNew:

    def __init__(self, board: Board, iteration: int, mode: str):
        self.board: Board = board
        self.iteration: int = iteration
        self.node_list: List[Node] = self.node_list(mode)
        # a = RandomAlg(self.board)
        
        # a.run_algorithm()
        # print(a.moves_amount)
        # self.node_list: List[Node] = a.node_list

    def begin_solution(self, mode: str):
        if mode == 'random':
            algorithm: Union[RandomAlg, Bfs] = RandomAlg(self.board)
        elif mode == 'breadth':
            algorithm = Bfs(self.board, 300)
        # elif mode == "depth":
        #     algorithm = Dfs(board, 300)
        # elif mode == "bestdepth":
        #     algorithm = Bdfs(board, 300)
        return algorithm.node_list

    def reset_algorithm(self):
        pass

    def create_moves_made(self, start_node: Node, final_node: Node) -> None:
        self.moves_made: List[Tuple[str, int]] = []

        current: Node = final_node
        self.moves_amount = 0
        while current is not start_node:
            self.moves_made.append(current.step_taken)
            self.moves_amount += 1
            current = current.parent
        
        self.moves_made = self.moves_made[::-1]

    def run_algorithm(self) -> None:
        for _ in range(100):
            interval: int = len(self.node_list)

            # want interval that is not bigger then node list
            while interval >= len(self.node_list):
                interval = random.randint(5, 20)

            # choose ranodm start point in node list
            start = random.randint(0, len(self.node_list) - interval - 1)

            # do algoritme on small part to get it better
            b = Bfs(self.board, 300, self.node_list[start], self.node_list[start + interval])
            b.run_algorithm()

            # put the new improved part of node list into the node list, different when you improve the very last part
            if start + interval == len(self.node_list) - 1:
                self.node_list = self.node_list[:start] + b.node_list
            else:
                self.node_list[start + interval + 1].new_parent(b.node_list[-1])
        
                self.node_list = self.node_list[:start] + b.node_list + self.node_list[start + interval + 1:]
        
        self.create_moves_made(self.node_list[0], self.node_list[-1])

        print(self.moves_amount, " ")
