"""
dfs.py

Programmeertheorie Rush Hour

Jesse Fontaine - 12693375
Annemarie Geertsema - 12365009
Laura Haverkorn - 12392707

- Contains class Dfs (Depth First Search) inherits Treesearcher.
"""

from __future__ import annotations

from code.algorithms.base_algorithms.tree_search import Treesearcher


class Dfs(Treesearcher):
    """
    The Depth First Search class that runs a search algorithm.
    Searches a branch untill a winning state, if a branch is pruned go back to parent and choose a new branch.
    """

    def _get_current_state(self):
        """
        Gets last state from queue.
        """

        return self.states.pop()
