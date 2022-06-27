from __future__ import annotations

from code.algorithms.base_algorithms.tree_search import Treesearcher


class Dfs(Treesearcher):
    """
    The Depth First Search class that runs a search algorithm.
    Searches a branch untill a winning state, if a branch is pruned go back to parent and choose a new branch.
    """

    def get_current_state(self):
        """
        Gets last state from queue.
        """

        return self.states.pop()
