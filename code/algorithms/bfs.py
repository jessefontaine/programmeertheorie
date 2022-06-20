from __future__ import annotations
from .tree_search import Treesearcher


from typing import List, Dict, Tuple, Union
from queue import Queue

from code.classes import Board
from code.functions.functions import merge_moves

class Bfs(Treesearcher):

    def get_current_state(self):
        return self.states.pop(0)