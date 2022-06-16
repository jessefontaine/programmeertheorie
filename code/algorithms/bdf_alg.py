from __future__ import annotations
from typing import Tuple, List, Set
from code.classes import Board
from code.functions.functions import write_moves_to_file
from .node import Node
from code.functions import merge_moves

import random

class BDF_Alg():

    def __init__(self: BDF_Alg, board: Board) -> None:
        self.board: Board = board
        self.moves_made: List[Tuple[str, int]] = []

    def best_depth(self: BDF_Alg) -> Tuple[Board, List[Tuple[str, int]]]:
        board_set_ups: Set = set()
        head_board: Board = self.board

        # make begin node and add it in stack and save as a board set up
        begin_node = Node(str(head_board))
        stack = [begin_node]
        board_set_ups.add(begin_node.board_rep)

        # loop though all possible bord until win board is found
        #while True:
        for _ in range(3):
            print("BEGIN")
            print(stack)

            if len(stack) > 1:
                parent = self.best_rep(stack)
            else:
                parent = stack.pop()

            print('parent', parent)
            
            stack.clear()
            print(stack)

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

    def best_rep(self, stack):
        print("BESTREP")
        tmp_board = self.board

        distance = tmp_board.size[1] - 2
        best_choice = stack[0]
        print(distance, best_choice)

        for node in stack:
            print('rep', node)
            tmp_board.set_board(node.board_rep)
            print(tmp_board)

            tmp_distance = tmp_board.size[1] - tmp_board.win_car.position[1] - 2
            if tmp_distance < distance:
                print(tmp_board.size[1] - tmp_board.win_car.position[1] - 2)
                distance = tmp_distance
                best_choice = node

        return best_choice

    def run_algorithm(self: BDF_Alg) -> None:
        """
            Runs the depth first algorithm until a solution is found.
            Merges all moves of the same car and saves how many moves necessary.
        """

        # store end board and the moves made to work towards this board
        tmp = self.best_depth()

        self.board = tmp[0]
        self.moves_made = tmp[1]

        # make and store the final moves
        self.moves_made.extend(self.board.exit_moves())

        # merge moves of same car together
        self.moves_made = merge_moves(self.moves_made)

        # store amount of moves
        self.moves_amount: int = len(self.moves_made)