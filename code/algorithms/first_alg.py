from __future__ import annotations

from typing import Tuple, List
import random

from ..classes import Board, Car
# from code import Board, Car


class First_Alg():

    def __init__(self: First_Alg, board: Board) -> None:
        self.board = board
        self.moves_made: List[Tuple[str, int]] = []

    def move_win_car(self: First_Alg) -> bool:
        dict = self.board.moves_dict

        if self.board.win_car in dict and 1 in list(dict[self.board.win_car]):
            self.moves_made.append(self.board.make_move(self.board.win_car, 1))

            return True

        return False

    def cars_to_left(self: First_Alg) -> bool:
        dict = self.board.moves_dict

        for car in dict:
            if car.orientation == "H" and -1 in list(dict[car]) and car.name != "X":
                self.moves_made.append(self.board.make_move(car, -1))

                return True

        return False

    def cars_vertical(self: First_Alg) -> bool:
        dict = self.board.moves_dict

        row_win_car = self.board.win_car.position[0]

        for car in dict:
            if car.orientation == "V" and car.length == 3 and 1 in list(dict[car]):
                self.moves_made.append(self.board.make_move(car, 1))
                
                return True
            elif car.orientation == "V" and (car.position[0] == row_win_car or\
                 car.position[0] + 1 == row_win_car and car.length == 2):
                random_move = random.choice(list(dict[car]))
                self.moves_made.append(self.board.make_move(car, random_move))
                
                return True

        return False

    def step(self):
        print(self.board)
        while not self.board.win():
            if self.move_win_car():
                pass
            elif self.cars_to_left():
                pass
            elif self.cars_vertical():
                pass
            print(self.board)

        # make and store the final moves
        self.moves_made.extend(self.board.exit_moves())

        print(self.moves_made)
        i = 0
        while i < len(self.moves_made) - 1:
            if self.moves_made[i][0] == self.moves_made[i + 1][0]:
                self.moves_made[i] = (self.moves_made[i][0], self.moves_made[i][1] + self.moves_made[i + 1][1])
                del self.moves_made[i + 1]
                i = i - 1

            i = i + 1
        print(self.moves_made)
        # for i in range(len(self.moves_made) - 1):
        #     print(i, len(self.moves_made) - 1)
        #     if self.moves_made[i][0] == self.moves_made[i + 1][0]:
        #         self.moves_made[i] = (self.moves_made[i][0], self.moves_made[i][1] + self.moves_made[i + 1][1])
        #         del self.moves_made[i + 1]
        #         i = i - 2
        # print(self.moves_made)

