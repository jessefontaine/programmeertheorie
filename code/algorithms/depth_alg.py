from __future__ import annotations
from typing import Tuple, List, Set
from code.classes import Board
from .node import Node
from ..functions import merge_moves


class Depth_Alg():

    def __init__(self: Depth_Alg, board: Board) -> None:
        self.board: Board = board
        self.moves_made: List[Tuple[str, int]] = []
        self.moves_amount: int = 0

    def depth(self: Depth_Alg) -> Tuple(Board, List[Tuple[str, int]]):
        board_set_ups: Set = set()
        head_board: Board = self.board
        #depth: int = 2

        # make begin node and add it in stack and save as a board set up
        begin_node = Node(str(head_board))
        stack = [begin_node]
        board_set_ups.add(begin_node.board_rep)

        #for _ in range(depth):
        while True:
            parent = stack.pop()
            head_board.set_board(parent.board_rep)

            # for each possible moveable car save the board representation
            for car in head_board.moves_dict:
                # update the board with right car representation
                head_board.set_board(parent.board_rep)

                # for each move save the board representation
                for direction in head_board.moves_dict[car]:
                    # update board with right car representation
                    head_board.set_board(parent.board_rep)

                    # make new board representation and save as new node
                    head_board.make_move(car, direction)
                    child = Node(str(head_board))

                    # do not save board representation when we already have/had it in stack
                    if child.board_rep in board_set_ups:
                        pass
                    else:
                        # save all the steps taken to the node
                        tmp = parent.steps_taken[:]
                        tmp.append((car, direction))
                        child.steps_taken = tmp

                        # save board representation in stack and our set
                        stack.append(child)
                        board_set_ups.add(child.board_rep)

                        if head_board.win():
                            return head_board, child.steps_taken

    def merge_moves(self: Depth_Alg) -> None:
        """
            Merges moves together.
            Deletes the move if direction is 0.
        """
        i = 0

        # loop over moves made
        while i < len(self.moves_made) - 1:
            # check if next move is done with the same car
            if self.moves_made[i][0] == self.moves_made[i + 1][0]:
                self.moves_made[i] = (self.moves_made[i][0], self.moves_made[i][1] + self.moves_made[i + 1][1])
                # delete the move which is added
                del self.moves_made[i + 1]
                
                # if the move is undone, delete move
                if self.moves_made[i][1] == 0:
                    del self.moves_made[i]
                    i -= 1
                i -= 1
            i += 1

    def run_algorithm(self: Depth_Alg) -> None:
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