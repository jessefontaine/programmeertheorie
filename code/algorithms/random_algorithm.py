from __future__ import annotations

import random
from typing import Union

from code.classes import Board, Node
from code.algorithms.base_algorithms.base_algorithm import BaseAlg


class RandomAlg(BaseAlg):
    def __init__(
        self,
        board: Board,
        start_node: Union[Node, None] = None,
        end_node: Union[Node, None] = None,
    ) -> None:
        super().__init__(board, start_node=start_node, end_node=end_node)

    def algorithm(self) -> Node:
        """
        Runs the random algoritm until the game is won.
        """

        current_state: Node = self.start_node

        while not self.check_finished(current_state, set_board_every_check=False):
            # get the possible moves of current state
            moves = self.board.possible_moves

            # pick one random move
            move = random.choice(moves)

            # make the move
            self.board.make_move(*move)

            # create node
            new_node: Node = Node(str(self.board), move, current_state)

            # set current state to the new node
            current_state = new_node

        # return the ending node
        return current_state
