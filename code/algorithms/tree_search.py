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

    def check_finished(self, state: Node) -> bool:
        self.board.set_board(state.board_rep)
        if self.find_win:
            return self.board.on_win_position()
        else:
            return state.board_rep == self.end_node.board_rep

    def create_run_data(self, final_node: Node):

        self.node_list: List[Node] = []
        self.moves_made: List[Optional[Tuple[str, int]]] = []

        current: Node = final_node
        self.moves_amount = 0
        while current is not self.start_node:
            self.node_list.append(current)
            self.moves_made.append(current.step_taken)
            self.moves_amount += 1
            current = current.parent
        
        self.node_list.append(self.start_node)
        self.node_list = self.node_list[::-1]
        self.moves_made = self.moves_made[::-1]

    def reset_algorithm(self):
        self.states = [self.start_node]
        self.unique_board_setups = set([self.start_node.board_rep])

    def run_algorithm(self):
        while self.states:
            current_state: Node = self.get_current_state()
            
            if self.check_finished(current_state):
                break

            self.build_children(current_state)

        self.create_run_data(current_state)
