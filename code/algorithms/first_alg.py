from __future__ import annotations

from typing import Tuple, List
import random

from ..classes import Board, Car
# from code import Board, Car


class Random_Alg():

    def __init__(self: Random_Alg, board: Board) -> None:
        self.board = board



    def win_car_move(self, moves_dict):
        if self.win_car in moves_dict and 1 in list(moves_dict[self.win_car]):
            self.win_car.move(1)
            #self.print_move_made((self.win_car, 1))
            self.move_made_to_file((self.win_car.name, 1))
            return True

        return False

    def cars_to_left(self, moves_dict):
        #for car in self.car_list:
        for car in moves_dict:
            if car.orientation == 'H' and -1 in list(moves_dict[car]) and car.name != "X":
                car.move(-1)
                # self.print_move_made((car, -1))
                return True

        return False

    def cars_move_vertical(self, moves_dict):
        row_win_car = self.win_car.position[0]
        #for car in self.car_list:
        for car in moves_dict:
            if car.orientation == 'V' and car.length == 3 and 1 in list(moves_dict[car]):
                car.move(1)
                # self.print_move_made((car, 1))
                return True
            elif car.orientation == 'V' and (car.position[0] == row_win_car or car.position[0] + 1 == row_win_car) and car.length == 2:
                random_move = random.choice(list(moves_dict[car]))
                car.move(random_move)
                # self.print_move_made((car, random_move))

                return True

                # if 1 in list(moves_dict[car]):
                #     car.move(1)
                #     self.print_move_made((car, 1))
                #     return True
                # else:
                #     car.move(-1)
                #     self.print_move_made((car, -1))
                #     return True

        return False