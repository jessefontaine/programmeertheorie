from __future__ import annotations
from typing import Tuple, List
from ..classes import Board, Car
import queue
import copy


class Breadth_Alg():

    def __init__(self: Breadth_Alg, board: Board) -> None:
        self.board = board
        self.moves_made: List[Tuple[str, int]] = []

    def breadth(self):
        depth = 3
        layer = queue.Queue()
        layer.put(self.board)

        while not layer.empty():
            state = layer.get()
            print(state)

            for i in range(1):
                print(i)
                for car in state.moves_dict:
                    print(car)
                    child = copy.deepcopy(state)
                    print(type(child))
            #         print(self.board.moves_dict[car])
                    print(child.moves_dict)
                    for direction in child.moves_dict[car]:
                        child.make_move(car, direction)
                        print(child)
            #             print(str(child))
                    



    def voorbeeld(self):
        depth = 3
        layer = queue.Queue()
        layer.put("")

        while not layer.empty():
            state = layer.get()
            print(state)

            if len(state) < depth:
                for i in ['L', 'R']:
                    child = copy.deepcopy(state)
                    child += i
                    layer.put(child)
                    print(list(layer.queue))


    def run_algorithm(self: Board) -> None:
        """
            Runs the random algoritm until the game is won.
        """

        self.breadth()