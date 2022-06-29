"""
dfs.py

Programmeertheorie Rush Hour

Jesse Fontaine - 12693375
Annemarie Geertsema - 12365009
Laura Haverkorn - 12392707

- Contains class Dfs (Depth First Search) inherits Treesearcher.
"""

from __future__ import annotations
from typing import Union

from code.algorithms.base_algorithms.tree_search import Treesearcher
from code.classes import Board, Node


class Dfs(Treesearcher):
    """
    The Depth First Search class that runs a search algorithm.
    Searches a branch until a winning state, if a branch is pruned
    goes back to parent and chooses a new branch.
    """

    def __init__(
        self,
        board: Board,
        depth: int = None,
        start_node: Union[Node, None] = None,
        end_node: Union[Node, None] = None
    ):
        super().__init__(board, depth, start_node, end_node)

    def _get_current_state(self) -> Node:
        """
        Gets last state from queue.
        """

        return self.states.pop()
