"""
tree_search.py

Programmeertheorie Rush Hour

Jesse Fontaine - 12693375
Annemarie Geertsema - 12365009
Laura Haverkorn - 12392707

- Contains class Treesearch inherits BaseAlg (Base Algorithm).
- Contains functions to build tree and sort children.
- Contains functions to reset and run the algorithm.
"""

from __future__ import annotations

from random import shuffle
from typing import List, Set, Union

from code.classes import Board
from code.classes import Node
from code.algorithms.base_algorithms.base_algorithm import BaseAlg


class Treesearcher(BaseAlg):
    """
    The Tree Searcher class that can be used for all the constructive algorithms.
    Contains methods that all constructive algoritms need.
    """

    def __init__(
        self,
        board: Board,
        depth: int = None,
        start_node: Union[Node, None] = None,
        end_node: Union[Node, None] = None,
    ):
        super().__init__(board, depth, start_node, end_node)

        # states list to function as stack or queue
        self.states: List[Node] = [self.start_node]

        # set of previous found states for pruning
        self.unique_board_setups: Set[str] = set([self.start_node.board_rep])

    def reset_algorithm(self) -> None:
        """
        Reset the algorithm to it's beginning state
        """

        super().reset_algorithm()

        # reset the additional instance variables
        self.states = [self.start_node]
        self.unique_board_setups = set([self.start_node.board_rep])

    def _get_current_state(self) -> Node:
        """
        Method to get the next state from stack or queue.
        """

        raise NotImplementedError

    def _sort_children(self, children) -> List[Node]:
        """
        Method to sort the list of children before they are added to the
        stack or queue.
        """

        return children

    def _build_children(self, parent: Node) -> None:
        """
        Create children node of the given parent.
        States that have previously been found in the current run will be pruned.
        """

        # set the board to the parents state and shuffle order of moves
        self.board.set_board(parent.board_offsets)
        shuffle(self.board.possible_moves)

        children = []

        # create children for all moves that don't result in states already seen
        for move in self.board.possible_moves:

            # set board back to parent state and make the move
            self.board.set_board(parent.board_offsets)
            self.board.make_move(*move)

            # pruning step
            if repr(self.board) not in self.unique_board_setups:

                # create child and add state to set of seen states
                child = Node(
                    repr(self.board), self.board.offset_from_start, move, parent
                )
                children.append(child)
                self.unique_board_setups.add(child.board_rep)

        children = self._sort_children(children)

        # add children nodes to stack or queue
        self.states.extend(children)

    def algorithm(self) -> Node:
        """
        Basic tree searcher algorithm.
        """

        # run the tree searcher over all states in stack or queue
        current_state: Node = self.start_node

        while self.states and self._check_depth(current_state):
            # get the state to work with
            current_state = self._get_current_state()

            # check if its the final one
            if self._check_finished(current_state):
                break

            # add child states to stack or queue
            self._build_children(current_state)

        return current_state
