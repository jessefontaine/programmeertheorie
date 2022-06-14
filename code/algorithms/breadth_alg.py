from __future__ import annotations
from typing import Tuple, List
from code.classes import Board
import queue
# import copy


class Breadth_Alg():

    def __init__(self: Breadth_Alg, board: Board) -> None:
        self.board: Board = board
        self.moves_made: List[Tuple[str, int]] = []
        self.moves_amount: int = 0

    def breadth(self):
        depth: int = 3
        layer: queue = queue.Queue()
        layer.put(str(self.board))

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
                    


    """
    def voorbeeld(self: Breadth_Alg):
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
    """

    def run_algorithm(self: Breadth_Alg) -> None:
        """
            Runs the random algoritm until the game is won.
        """

        # self.breadth()
        pass