from __future__ import annotations

from typing import List, Tuple, Union, Optional


class Node:

    def __init__(self: Node, board_rep: str, step: Tuple[str, int] = None, parent: Node = None):
        
        self.board_rep: str = board_rep
        
        if parent is None:
            self.has_parent: bool = False
            self.steps_taken: List[Optional[Tuple[str, int]]] = [None]
        
        else:

            self.has_parent = True
            self.parent: Node = parent
            self.parent.steps_taken.append(step)
        
