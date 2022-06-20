from __future__ import annotations
from .dfs import Dfs


from typing import List, Dict, Tuple, Union
from queue import Queue

from code.classes import Board
from code.classes import Node
from code.functions.functions import merge_moves

class Bdfs(Dfs):
    def sort_children(self, children: List[Node]) -> List[Node]:
        """
        uses bubble sort
        """
        tmp_board: Board = self.board

        list_cars_in_front: List[int] = []
        list_distance: List[int] = []

        # for each node calculate cars in front of win car and distance of win car to exit
        for node in children:
            tmp_board.set_board(node.board_rep)
            list_cars_in_front.append(self.cars_in_front(tmp_board))

            list_distance.append(tmp_board.size[1] - tmp_board.win_car.position[1] - tmp_board.win_car.length)

        swapped = False
        # Looping from size of list from last index[-1] to index [0]
        for n in range(len(children)-1, 0, -1):
            for i in range(n):
                # swap nodes such that node with least cars in front goes to back of list
                if list_cars_in_front[i] < list_cars_in_front[i + 1]:
                    swapped = True

                    # swapping data of all lists
                    children[i], children[i + 1] = children[i + 1], children[i] 
                    list_cars_in_front[i], list_cars_in_front[i + 1] = list_cars_in_front[i + 1], list_cars_in_front[i]
                    list_distance[i], list_distance[i + 1] = list_distance[i + 1], list_distance[i]
                # swap nodes such that node with less distance of win car to exit goes to back of list
                if list_cars_in_front[i] == list_cars_in_front[i + 1]:
                    if list_distance[i] < list_distance[i + 1]:
                        swapped = True

                        # swapping data of all lists
                        children[i], children[i + 1] = children[i + 1], children[i] 
                        list_cars_in_front[i], list_cars_in_front[i + 1] = list_cars_in_front[i + 1], list_cars_in_front[i]
                        list_distance[i], list_distance[i + 1] = list_distance[i + 1], list_distance[i]

            if not swapped:
                # exiting the loop if we didn't make a single swap, so list is sorted
                pass

        return children

    def cars_in_front(self, board: Board) -> int:
        amount: int = 0

        # calculate how many cars are in front of win car
        for i in range(board.win_car.position[1] + 2, board.size[1]):
            if board.grid[board.win_car.position[0]][i] is not None:
                amount += 1

        return amount