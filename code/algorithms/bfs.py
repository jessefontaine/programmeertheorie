"""
bfs.py

Programmeertheorie Rush Hour

Jesse Fontaine - 12693375
Annemarie Geertsema - 12365009
Laura Haverkorn - 12392707

- Contains class Bfs (Breadth First Search) inherits Treesearcher.
"""

from __future__ import annotations

from code.algorithms.base_algorithms.tree_search import Treesearcher
from code.classes.node import Node


class Bfs(Treesearcher):
    """
    The Breadth First Search class that runs a search algorithm.
    Searches a winning state for every layer of the tree.
    """

    def _get_current_state(self) -> Node:
        """
        Gets first state from queue.
        """

        return self.states.pop(0)
