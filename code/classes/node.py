"""
node.py

Programmeertheorie Rush Hour

Jesse Fontaine - 12693375
Annemarie Geertsema - 12365009
Laura Haverkorn - 12392707

- Contains class Node.
- Function define parents in a search tree.
"""

from __future__ import annotations
from typing import Tuple, Optional, Dict
from copy import copy


class Node:
    def __init__(
        self,
        board_str: str,
        board_offsets: Dict[str, int],
        step: Tuple[str, int] = None,
        parent: Node = None,
    ):

        self.board_rep: str = board_str
        self.board_offsets: Dict[str, int] = copy(board_offsets)
        self.step_taken: Optional[Tuple[str, int]] = step

        if parent is None:
            self.has_parent: bool = False
        else:
            self.has_parent = True
            self.parent: Node = parent
            self.depth: int = self.parent.depth + 1

    def start_depth(self) -> None:
        self.depth = 0

    def new_parent(self, parent: Node) -> None:
        """
        Gives node a parent.
        """

        self.has_parent = True
        self.parent = parent
