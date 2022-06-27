from __future__ import annotations

from code.algorithms.base_algorithms.tree_search import Treesearcher


class Bfs(Treesearcher):
    """
    The Breadth First Search class that runs a search algorithm.
    Searches a winning state for every layer of the tree.
    """

    def get_current_state(self):
        """
        Gets first state from queue.
        """

        return self.states.pop(0)
