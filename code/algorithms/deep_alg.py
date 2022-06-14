from __future__ import annotations
from typing import Tuple, List
from code.classes import Board
import queue
import copy


class Deep_Alg():

    def __init__(self: Deep_Alg, board: Board) -> None:
        self.board: Board = board
        self.moves_made: List[Tuple[str, int]] = []
        self.moves_amount: int = 0

    def deep(self):
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


    def run_algorithm(self: Deep_Alg) -> None:
        """
            
        """

        self.deep()