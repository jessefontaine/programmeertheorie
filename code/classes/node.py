from __future__ import annotations

from typing import Tuple


class Node:

    def __init__(self: Node, board_rep: str, step: Tuple[str, int] = None, parent: Node = None):
        
        self.board_rep: str = board_rep
        
        if parent is None:
            self.has_parent: bool = False
            self.step_taken: Tuple[str, int] = step
        
        else:

            self.has_parent = True
            self.parent: Node = parent
            self.step_taken = step        
