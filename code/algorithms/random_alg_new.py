from __future__ import annotations

import random
from typing import Tuple, List, Union

from code.classes import Board, Node
from code.algorithms.base_algorithm import BaseAlg


class RandomAlg(BaseAlg):

    def __init__(self, board: Board, start_node: Union[Node, None] = None, end_node: Union[Node, None] = None) -> None:
        super().__init__(board, start_node=start_node, end_node=end_node)

    def _move(self) -> Tuple[str, int]:
        """
        Returns a random move; a tuple with car object and the direction.
        """

        # chooses random move from dictionary
        # car_move: str = random.choice(list(self.board.moves_dict.keys()))
        ran_move = random.choice(self.board.possible_moves)

        return ran_move
    


    def algorithm(self) -> Node:
        """
        Runs the random algoritm until the game is won.
        """

        current_state: Node = self.start_node
        while not self.check_finished(current_state):
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


        # # clear the moves made list
        # self.moves_made = []

        # # make random steps in game untill red car is in win position
        # while not self.board.on_win_position():
        #     # make move
        #     move = self._move()
            
        #     # make and store the moves
        #     self.moves_made.append(self.board.make_move(*move))

        #     # add child node to list of states
        #     self.node_list.append(Node(str(self.board), move, self.node_list[-1]))

        # # make and store the final moves
        # # self.moves_made.extend(self.board.exit_moves())


        # # store amount of moves
        # self.moves_amount: int = len(self.moves_made)
