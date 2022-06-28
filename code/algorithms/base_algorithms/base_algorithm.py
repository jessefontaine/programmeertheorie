"""
base_algorithm.py

Programmeertheorie Rush Hour

Jesse Fontaine - 12693375
Annemarie Geertsema - 12365009
Laura Haverkorn - 12392707

- Contains class BaseAlg (Base Algorithm).
- Is being used in all the different constructive algorithms.
- Contains functions to reset and correctly run the algorithm.
- Function to save data from run.
"""

from __future__ import annotations
from typing import Tuple, List, Union, Optional

from code.classes import Board, Node


class BaseAlg:
    """
    The Base Algorithm class that can be used for all the algorithms as a basic.
    Contains methods that all algoritms need.
    """

    def __init__(
        self,
        board: Board,
        depth: int = None,
        start_node: Union[Node, None] = None,
        end_node: Union[Node, None] = None,
    ):

        # save the gameboard and maximum depth constructive algorithms can go
        self.board: Board = board
        self.depth: Optional[int] = depth
        self.node_list: List[Node] = []
        self.moves_made: List[Optional[Tuple[str, int]]] = []
        self.moves_amount: int = 0

        # starting without a start node means the current gameboard setup is the start
        if start_node is None:
            self.start_node: Node = Node(repr(self.board), self.board.offset_from_start)
        else:
            self.start_node = start_node
            self.board.set_board(self.start_node.board_offsets)

        self.start_node.start_depth()

        # starting without an end node means the algorithm will try to find a winning setup
        if end_node is None:
            self.find_win: bool = True
        else:
            self.find_win = False
            self.end_node: Node = end_node

        # ensure proper usage
        if depth is not None and depth < 1:
            raise ValueError("Value for depth must be positive.")

    def _check_depth(self, current_state) -> bool:
        """
        Checks whether a given state has an acceptable depth.
        """

        if current_state.depth == self.depth:
            return False

        return True

    def _check_finished(self, state: Node, set_board_every_check: bool = True) -> bool:
        """
        Checks whether a given state satisfies the constraints.
        """

        if set_board_every_check:
            # setup the board according to the given state
            self.board.set_board(state.board_offsets)

        # return whether contraints are satisfied
        if self.find_win:
            return self.board.on_win_position()

        return state.board_rep == self.end_node.board_rep

    def _create_run_data(self, final_node: Node) -> None:
        """
        After a run, calculate the data for the found solution.
        """

        # moving backwards from the winning node, construct the entire node list
        current: Node = final_node

        while current is not self.start_node:
            # save the data
            self.node_list.append(current)
            self.moves_made.append(current.step_taken)
            self.moves_amount += 1

            # switch to the parent
            current = current.parent

        # append the first node
        self.node_list.append(self.start_node)

        # invert all lists, since they are built from children to parents
        self.node_list = self.node_list[::-1]
        self.moves_made = self.moves_made[::-1]

    def reset_algorithm(self) -> None:
        """
        Resets everything to the initial state.
        """

        self.node_list = [Node(repr(self.board), self.board.offset_from_start)]
        self.moves_made = []

    def algorithm(self) -> Node:
        """
        To implement the algorithm.
        """

        raise NotImplementedError

    def run_algorithm(self) -> Tuple[Node, Node]:
        """
        Runs the algorithm.
        Returns the start and end state.
        """

        end_state: Node = self.algorithm()
        self._create_run_data(end_state)

        return self.start_node, end_state
