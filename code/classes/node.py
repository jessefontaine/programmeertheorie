from __future__ import annotations

from typing import Tuple, Optional


class Node:
    def __init__(
        self, board_rep: str, step: Tuple[str, int] = None, parent: Node = None
    ):

        self.board_rep: str = board_rep
        self.step_taken: Optional[Tuple[str, int]] = step

        if parent is None:
            self.has_parent: bool = False

        else:
            self.has_parent = True
            self.parent: Node = parent

    def new_parent(self, parent: Node) -> None:
        """
        Gives node a parent.
        """

        self.has_parent = True
        self.parent = parent

    def __len__(self):
        """
        Returns if node has parents.
        """

        if self.has_parent:
            return len(self.parent) + 1
        else:
            return 0
