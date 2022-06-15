from __future__ import annotations
from typing import Tuple, List, Set
from code.classes import Board
from .node import Node
import queue
import copy


class Deep_Alg():

    def __init__(self: Deep_Alg, board: Board) -> None:
        self.board: Board = board
        self.moves_made: List[Tuple[str, int]] = []
        self.moves_amount: int = 0

    def deep_zonder_pruning(self):
        depth: int = 3
        stack = [self.board]

        for _ in range(depth):
            print('BEGIN')
            state = stack.pop()
            print(state)

            for car in state.moves_dict:
                child = copy.deepcopy(state)

                for direction in child.moves_dict[car]:
                    child.make_move(car, direction)
                    stack.append(child)
                    
            print(stack)
            for bla in stack:
                print("############")
                print(bla)

    def deep(self):
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
        print(" ")
        for bla in stack:
            print(bla.steps_taken)


    def run_algorithm(self: Deep_Alg) -> None:
        """
            
        """
        
        bla = self.deep()
        bla = bla[1:]
        
