"""
random_algorithm.py

Programmeertheorie Rush Hour

Jesse Fontaine - 12693375
Annemarie Geertsema - 12365009
Laura Haverkorn - 12392707

- Contains class RandomAlg (Random Algorithm) inherits BaseAlg.
"""

from __future__ import annotations
from typing import Union

from random import choice

from code.classes import Board, Node
from code.algorithms.base_algorithms.base_algorithm import BaseAlg


class RandomAlg(BaseAlg):
    """
    The Random Algorithm class makes random moves untill the board is in a winning state.
    """

    def __init__(
        self,
        board: Board,
        depth: int = None,
        start_node: Union[Node, None] = None,
        end_node: Union[Node, None] = None,
    ):
        super().__init__(board, depth, start_node=start_node, end_node=end_node)

    def algorithm(self) -> Node:
        """
        Runs the random algoritm until the game is won.
        """

        current_state: Node = self.start_node

        while not self._check_finished(
            current_state, set_board_every_check=False
        ) and self._check_depth(current_state):
            # get the possible moves of current state and pick random
            moves = self.board.possible_moves
            move = choice(moves)

            # make the move
            self.board.make_move(*move)

            # create node
            new_node: Node = Node(
                repr(self.board), self.board.offset_from_start, move, current_state
            )

            # set current state to the new node
            current_state = new_node

        return current_state
