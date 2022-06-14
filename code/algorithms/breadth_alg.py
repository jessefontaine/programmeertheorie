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
        layer.put(str(self.board))

        while not layer.empty():
            state = layer.get()
            print(state)

            for i in range(1):
                print(i)
                for car in self.board.moves_dict:
                    print(car)
                    print(str(self.board))


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