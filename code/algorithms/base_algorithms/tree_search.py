from __future__ import annotations

import random
from typing import List, Set, Union

from code.classes import Board
from code.classes import Node
from code.algorithms.base_algorithms.base_algorithm import BaseAlg


class Treesearcher(BaseAlg):
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
        self.unique_board_setups: Set = set([self.start_node.board_rep])

    def reset_algorithm(self):
        """
        Reset the algorithm to it's beginning state
        """

        super().reset_algorithm()

        # reset the additional instance variables
        self.states = [self.start_node]
        self.unique_board_setups = set([self.start_node.board_rep])

    def _get_current_state(self):
        """
        Method to get the next state from stack or queue.
        """

        raise NotImplementedError

    def _sort_children(self, children):
        """
        Method to sort the list of children before they are added to the
        stack or queue.
        """

        return children

    def _build_children(self, parent: Node):
        """
        Create children node of the given parent. States that have previously been
        found in the current run will be pruned.
        """

        # set the board to the parents state and shuffle order of moves
        self.board.set_board(parent.board_rep)
        random.shuffle(self.board.possible_moves)

        # list for storing children
        children = []

        # create children for all moves that don't result in states already seen
        for move in self.board.possible_moves:

            # set board back to parent state and make the move
            self.board.set_board(parent.board_rep)
            self.board.make_move(*move)

            # pruning step
            if str(self.board) not in self.unique_board_setups:

                # create child and add state to set of seen states
                child = Node(str(self.board), move, parent)
                children.append(child)
                self.unique_board_setups.add(child.board_rep)

        # sort children based on sorting method
        children = self._sort_children(children)

        # add children nodes to stack or queue
        self.states.extend(children)

    def _algorithm(self):
        """
        Basic tree searcher algorithm.
        """

        # run the tree searcher over all states in stack or queue
        current_state: Node = self.start_node

        while self.states:  # and current_state.depth < self.depth:
            # get the state to work with
            current_state = self._get_current_state()

            # check if its the final one
            if self._check_finished(current_state):
                break

            # add child states to stack or queue
            self._build_children(current_state)

        return current_state
