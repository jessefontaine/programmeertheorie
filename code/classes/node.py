from __future__ import annotations

from typing import Tuple, Optional


class Node:

    def __init__(self, board_rep: str, step: Tuple[str, int] = None, parent: Node = None):
        
        self.board_rep: str = board_rep
        self.step_taken: Optional[Tuple[str, int]] = step
        
        if parent is None:
            self.has_parent: bool = False            
        
        else:

            self.has_parent = True
            self.parent: Node = parent
