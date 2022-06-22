from __future__ import annotations

from code.algorithms.tree_search import Treesearcher


class Dfs(Treesearcher):

    def get_current_state(self):
        return self.states.pop()