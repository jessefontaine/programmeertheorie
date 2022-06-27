from __future__ import annotations

from code.algorithms.base_algorithms.tree_search import Treesearcher


class Dfs(Treesearcher):
    def get_current_state(self):
        """
        Gets last state from queue.
        """

        return self.states.pop()
