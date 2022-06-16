from __future__ import annotations
from typing import Tuple, List, Set
from code.classes import Board
from code.functions.functions import write_moves_to_file
from .node import Node
from code.functions import merge_moves

import random

class Depth_Alg():

    def __init__(self, board: Board) -> None:
        self.board: Board = board
        self.moves_made: List[Tuple[str, int]] = []

    def depth(self) -> Tuple[Board, List[Tuple[str, int]]]:
        board_set_ups: Set = set()
        head_board: Board = self.board

        # make begin node and add it in stack and save as a board set up
        begin_node = Node(str(head_board))
        stack = [begin_node]
        board_set_ups.add(begin_node.board_rep)

        # loop though all possible bord until win board is found
        while True:
            parent = stack.pop()
            head_board.set_board(parent.board_rep)

            moves_list = list(head_board.moves_dict.items())
            random.shuffle(moves_list)

            # for each possible moveable car save the board representation
            for car in moves_list:
                # update the board with right car representation
                head_board.set_board(parent.board_rep)

                random.shuffle(car[1])

                # for each move save the board representation
                for direction in car[1]:
                    # update board with right car representation
                    head_board.set_board(parent.board_rep)

                    # make new board representation and save as new node
                    head_board.make_move(car[0], direction)
                    child = Node(str(head_board))

                    # do not save board representation when we already have/had it in stack
                    if child.board_rep in board_set_ups:
                        pass
                    else:
                        # save all the steps taken to the node
                        tmp: List[Tuple[str, int]] = parent.steps_taken[:]
                        tmp.append((car[0], direction))
                        child.steps_taken = tmp

                        # save board representation in stack and our set
                        stack.append(child)
                        board_set_ups.add(child.board_rep)

                        if head_board.win():
                            return head_board, child.steps_taken

    def run_algorithm(self) -> None:
        """
        Runs the depth first algorithm until a solution is found.
        Merges all moves of the same car and saves how many moves necessary.
        """

        # store end board and the moves made to work towards this board
        tmp = self.depth()

        self.board = tmp[0]
        self.moves_made = tmp[1]

        # make and store the final moves
        self.moves_made.extend(self.board.exit_moves())

        # merge moves of same car together
        self.moves_made = merge_moves(self.moves_made)

        # store amount of moves
        self.moves_amount: int = len(self.moves_made)