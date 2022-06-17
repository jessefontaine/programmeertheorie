from __future__ import annotations

from typing import List, Tuple, Union


class Node():

    def __init__(self, board_rep: str, parent: Union[Node, None]):
        
        self.board_rep: str = board_rep
        self.steps_taken: List[Tuple[str, int]] = []
        # self.possible_moves: List[Tuple[str, int]] = []
        self.parent: Union[Node, None] = parent
