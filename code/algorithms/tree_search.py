from __future__ import annotations
from typing import Tuple, List, Set, Union
from code.classes import Board
from code.functions.functions import write_moves_to_file
from code.classes import Node


class Treesearcher:
  
    def __init__(self, board: Board, depth: int, start_node: Union[Node, None] = None, end_node: Union[Node, None] = None):
        self.board: Board = board
        self.depth: int = depth
        
        if start_node is not None:
            self.start_node: Node = start_node
        else:
            self.start_node = Node(str(board))
        if end_node is not None:
            self.end_node: Node = end_node
        
        self.states: List[Node] = [self.start_node]
    
    
    def get_current_state(self):
        raise NotImplementedError

    def build_children(self, parent: Node):
        self.board.set_board(parent.board_rep)
    
     
    def run_algorithm(self):
        while self.states:
            current_state: Node = self.get_current_state()
            self.build_children(current_state)

        # """
        # Runs the algorithm untill all possible states are visited.
        # """
        # while self.states:
        #     new_graph = self.get_next_state()

        #     # Retrieve the next empty node.
        #     node = new_graph.get_empty_node()

        #     if node is not None:
        #         self.build_children(new_graph, node)
        #     else:
        #         # Stop if we find a solution
        #         # break

        #         # or ontinue looking for better graph
        #         self.check_solution(new_graph)

        # # Update the input graph with the best result found.
        # self.graph = self.best_solution
        
        
    
    
