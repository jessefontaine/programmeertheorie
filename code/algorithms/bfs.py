from __future__ import annotations

from code.algorithms.base_algorithms.tree_search import Treesearcher


class Bfs(Treesearcher):
    def get_current_state(self):
        """
        Gets first state from queue.
        """

        return self.states.pop(0)
