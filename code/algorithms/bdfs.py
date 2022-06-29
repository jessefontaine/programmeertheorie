"""
bdfs.py

Programmeertheorie Rush Hour

Jesse Fontaine - 12693375
Annemarie Geertsema - 12365009
Laura Haverkorn - 12392707

- Contains class Bdfs (Best Depth First Search) inherits Dfs (Depth First Search).
- Contains heuristics to improve Dfs.
- Uses a bubble sort algorithm.
"""

from __future__ import annotations
from typing import List

from code.algorithms.dfs import Dfs
from code.classes import Board, Node


class Bdfs(Dfs):
    """
    The Best Depth First Search class that runs a Depth First Search algorithm.
    Uses heuristics in choosing branches by:
    - number of cars in front of the win car,
    - distance of win car to the exit.
    """

    def swap(self, not_sorted_list: List, index1: int, index2: int) -> None:
        """
        Swaps elements in a list.
        """

        not_sorted_list[index1], not_sorted_list[index2] = not_sorted_list[index1], not_sorted_list[index2]

    def _sort_children(self, children: List[Node]) -> List[Node]:
        """
        Uses bubble sort.
        """

        tmp_board: Board = self.board
        list_cars_in_front: List[int] = []
        list_distance: List[int] = []

        # for each node calculate cars in front of win car and distance to exit
        for node in children:
            tmp_board.set_board(node.board_offsets)
            list_cars_in_front.append(self._cars_in_front(tmp_board))

            list_distance.append(
                tmp_board.size[1]
                - tmp_board.win_car.position[1]
                - tmp_board.win_car.length
            )

        swapped = False

        # looping from size of list from last index to first
        for max_index in range(len(children) - 1, 0, -1):
            for i in range(max_index):
                # sort nodes according to number of cars in front high to low
                if list_cars_in_front[i] < list_cars_in_front[i + 1]:
                    swapped = True

                    # swapping data of all lists
                    self.swap(children, i, i + 1)
                    self.swap(list_cars_in_front, i, i + 1)
                    self.swap(list_distance, i, i + 1)

                # sort nodes according to distance of win car to exit high to low
                if list_cars_in_front[i] == list_cars_in_front[i + 1]:
                    if list_distance[i] < list_distance[i + 1]:
                        swapped = True

                        self.swap(children, i, i + 1)
                        self.swap(list_cars_in_front, i, i + 1)
                        self.swap(list_distance, i, i + 1)

            if not swapped:
                # exit the loop if we didn't make a swap, list is sorted
                pass

        return children

    def _cars_in_front(self, board: Board) -> int:
        """
        Counts the number of cars in front of the win car.
        """

        amount: int = 0

        # calculate how many cars are in front of win car
        for i in range(board.win_car.position[1] + 2, board.size[1]):
            if board.grid[board.win_car.position[0]][i] is not None:
                amount += 1

        return amount
