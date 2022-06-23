from __future__ import annotations
from platform import node
from typing import Tuple, List, Set, Union
from xml.dom.minicompat import NodeList
from .random_algorithm import RandomAlg
from .bfs import Bfs
from .dfs import Dfs
from .bdfs import Bdfs
from code.classes import Board
from code.functions.functions import write_moves_to_file
from code.classes import Node
import random


class HillClimberNew:

    def __init__(self, board: Board, iteration: int, start_mode: str, improve_mode: str):
        self.board: Board = board
        self.iteration: int = iteration
        self.improve_mode: str = improve_mode
        self.node_list: List[Node] = self.begin_solution(self.make_algorithm(start_mode))

        # REMOVE LATER
        print(len(self.node_list))

    def make_algorithm(self, mode: str, start_node: Union[Node, None] = None, end_node: Union[Node, None] = None) -> Union[RandomAlg, Bfs, Dfs, Bdfs]:
        # RANDOM FIXEN DAT JE BEGIN EN START PUNT KAN DOEN
        if mode == 'random':
            algorithm: Union[RandomAlg, Bfs] = RandomAlg(self.board)
        elif mode == 'breadth':
            algorithm = Bfs(self.board, 300, start_node, end_node)
        elif mode == "depth":
            algorithm = Dfs(self.board, 300, start_node, end_node)
        elif mode == "bestdepth":
            algorithm = Bdfs(self.board, 300, start_node, end_node)

        return algorithm

    def begin_solution(self, algorithm: Union[RandomAlg, Bfs, Dfs, Bdfs]) -> List[Node]:
        algorithm.run_algorithm()

        return algorithm.node_list

    def reset_algorithm(self):
        pass

    def choose_interval(self) -> int:
        interval: int = len(self.node_list)

        # want interval that is not bigger then node list
        while interval >= len(self.node_list):
            interval = random.randint(5, 20)    #DEZE OOK NOG VARIABLE MAKEN!!!!!!!!

        return interval

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
        #MOET NOG EEN MAX OPKOMEN
        for _ in range(self.iteration):
            interval: int = self.choose_interval()

            # choose ranodm start point in node list
            start = random.randint(0, len(self.node_list) - interval - 1)

            # do algoritme on small part to get it better
            alg = self.make_algorithm(self.improve_mode, self.node_list[start], self.node_list[start + interval])
            alg.run_algorithm()
            # print(interval)
            # print('g', len(alg.node_list))

            if interval <= len(alg.node_list):
                continue

            # put the new improved part of node list into the node list, different when you improve the very last part
            if start + interval == len(self.node_list) - 1:
                self.node_list = self.node_list[:start] + alg.node_list
            else:
                self.node_list[start + interval + 1].new_parent(alg.node_list[-1])
        
                self.node_list = self.node_list[:start] + alg.node_list + self.node_list[start + interval + 1:]
        
        self.create_moves_made(self.node_list[0], self.node_list[-1])

        print(self.moves_amount, "  ")
