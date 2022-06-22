from __future__ import annotations
from lib2to3.pytree import Base
from typing import Tuple, List, Set, Union, Optional
from code.functions.functions import write_moves_to_file
from code.classes import Board, Node
from code.algorithms.base_algorithm import BaseAlg
import random


class Treesearcher(BaseAlg):
  
    def __init__(self, board: Board, depth: int = None, start_node: Union[Node, None] = None, end_node: Union[Node, None] = None):
        super().__init__(board, depth, start_node, end_node)
        
        self.states: List[Node] = [self.start_node]
        self.unique_board_setups: Set = set([self.start_node.board_rep])

    def get_current_state(self):
        raise NotImplementedError

    def sort_children(self, children):
        return children

    def build_children(self, parent: Node):

        self.board.set_board(parent.board_rep)

        children = []

        random.shuffle(self.board.possible_moves)
        for move in self.board.possible_moves:

            self.board.set_board(parent.board_rep)
            self.board.make_move(*move)

            if str(self.board) not in self.unique_board_setups:
                child = Node(str(self.board), move, parent)
                children.append(child)
                self.unique_board_setups.add(child.board_rep)
        
        children = self.sort_children(children)

        self.states.extend(children)

    def reset_algorithm(self):
        self.states = [self.start_node]
        self.unique_board_setups = set([self.start_node.board_rep])

    def run_algorithm(self):
        states = 0
        while self.states:
            current_state: Node = self.get_current_state()
            states += 1
            
            if self.check_finished(current_state):
                break

            self.build_children(current_state)

        self.create_run_data(current_state)
        # print(f'amount of states: {states}')
