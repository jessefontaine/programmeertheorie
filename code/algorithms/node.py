from __future__ import annotations

from typing import List, Tuple


class Node():

    def __init__(self: Node, board_rep: str, steps: List[Tuple[str, int]] = []):
        
        self.board_rep: str = board_rep
        self.steps_taken: List[Tuple[str, int]] = steps
        self.possible_moves: List[Tuple[str, int]] = []
