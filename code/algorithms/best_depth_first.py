from __future__ import annotations
from typing import Tuple, List, Set
from code.classes import Board
from .node import Node
from .depth_first import DepthFirst
import random


class BestDepthFirst(DepthFirst):
    """"
    A Best Depth First algorithm that builds a queue of graphs with a unique assignment of nodes for each instance.
    Has the almost the same methods as DepthFirst class, the depth method is different.
    """

    def depth(self) -> Tuple[Board, List[Tuple[str, int]]]:
        board_set_ups: Set = set()
        head_board: Board = self.board

        # make begin node and add it in stack and save as a board set up
        begin_node: Node = Node(str(head_board), None)
        stack: List[Node] = [begin_node]
        board_set_ups.add(begin_node.board_rep)

        # loop though all possible bord until win board is found
        while True:
            parent = stack.pop()

            child_list: List[Node] = []
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
                    child = Node(str(head_board), parent)

                    # do not save board representation when we already have/had it in stack
                    if child.board_rep in board_set_ups:
                        pass
                    else:
                        # save all the steps taken to the node
                        tmp: List[Tuple[str, int]] = parent.steps_taken[:]
                        tmp.append((car[0], direction))
                        child.steps_taken = tmp

                        # save board representation in stack and our set
                        child_list.append(child)
                        board_set_ups.add(child.board_rep)

                        # when board in win position return the board and all the steps taken
                        if head_board.win():
                            return head_board, child.steps_taken

            stack = stack + self.bubble_sort(child_list)

    def bubble_sort(self, child_list: List[Node]) -> List[Node]:
        tmp_board: Board = self.board

        list_cars_in_front: List[int] = []
        list_distance: List[int] = []

        # for each node calculate cars in front of win car and distance of win car to exit
        for node in child_list:
            tmp_board.set_board(node.board_rep)
            list_cars_in_front.append(self.cars_in_front(tmp_board))

            list_distance.append(tmp_board.size[1] - tmp_board.win_car.position[1] - tmp_board.win_car.length)

        swapped = False
        # Looping from size of list from last index[-1] to index [0]
        for n in range(len(child_list)-1, 0, -1):
            for i in range(n):
                # swap nodes such that node with least cars in front goes to back of list
                if list_cars_in_front[i] < list_cars_in_front[i + 1]:
                    swapped = True

                    # swapping data of all lists
                    child_list[i], child_list[i + 1] = child_list[i + 1], child_list[i] 
                    list_cars_in_front[i], list_cars_in_front[i + 1] = list_cars_in_front[i + 1], list_cars_in_front[i]
                    list_distance[i], list_distance[i + 1] = list_distance[i + 1], list_distance[i]
                # swap nodes such that node with less distance of win car to exit goes to back of list
                if list_cars_in_front[i] == list_cars_in_front[i + 1]:
                    if list_distance[i] < list_distance[i + 1]:
                        swapped = True

                        # swapping data of all lists
                        child_list[i], child_list[i + 1] = child_list[i + 1], child_list[i] 
                        list_cars_in_front[i], list_cars_in_front[i + 1] = list_cars_in_front[i + 1], list_cars_in_front[i]
                        list_distance[i], list_distance[i + 1] = list_distance[i + 1], list_distance[i]

            if not swapped:
                # exiting the loop if we didn't make a single swap, so list is sorted
                pass

        return child_list

    def cars_in_front(self, board: Board) -> int:
        amount: int = 0

        # calculate how many cars are in front of win car
        for i in range(board.win_car.position[1] + 2, board.size[1]):
            if board.grid[board.win_car.position[0]][i] is not None:
                amount += 1

        return amount
