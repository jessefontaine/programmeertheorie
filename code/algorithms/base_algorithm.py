from __future__ import annotations
from typing import Tuple, List, Set, Union, Optional
from code.classes import Board, Node

class BaseAlg:

    def __init__(self, board: Board, depth: int = None, start_node: Union[Node, None] = None, end_node: Union[Node, None] = None):
        self.board: Board = board
        self.depth: Optional[int] = depth
        
        if start_node is None:
            self.start_node: Node = Node(str(self.board))
        else:
            self.start_node = start_node

        if end_node is None:
            self.find_win: bool = True
        else:
            self.find_win = False
            self.end_node: Node = end_node
        
