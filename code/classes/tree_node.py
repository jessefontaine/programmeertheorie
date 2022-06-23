from typing import Tuple

from .node import Node

class TreeNode(Node):

    def __init__(self, board_rep: str, step: Tuple[str, int] = None, parent: Node = None):
        super().__init__(board_rep, step, parent)
        
        if parent is None:
            self.depth: int = 0           
        
        else:
            self.depth = self.parent.depth + 1