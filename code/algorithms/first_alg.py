from __future__ import annotations

import random
from typing import Tuple, List, Dict

from code.classes import Board, Car
from code.functions import merge_moves


class First_Alg():

    def __init__(self: First_Alg, board: Board) -> None:
        self.board: Board = board
        self.cars: Dict[str, Car] = self.board.cars

    def move_win_car(self: First_Alg) -> bool:
        """
            Returns a bool if a win car can go to right; if it does it makes the move and saves it.
        """

        dict: Dict[str, List[int]] = self.board.moves_dict

        # moves win car to right if possible and saves move
        if self.board.win_car.name in list(dict.keys()) and 1 in list(dict[self.board.win_car.name]):
            self.moves_made.append(self.board.make_move(self.board.win_car.name, 1))

            return True

        return False

    def cars_to_left(self: First_Alg) -> bool:
        """
            Returns a bool if a horizontal car can go to left; if it does it makes the move and saves it.
        """

        dict = self.board.moves_dict


        # moves a car to the left if it is possible and saves move
        for car in list(dict.keys()):
            if self.cars[car].orientation == "H" and -1 in list(dict[car]) and car != "X":
                self.moves_made.append(self.board.make_move(car, -1))

                return True

        return False

    def cars_vertical(self: First_Alg) -> bool:
        """
            Returns a bool if a vertical car can go up or down; if it does it makes the move and saves it.
        """

        dict = self.board.moves_dict

        row_win_car = self.board.win_car.position[0]

        # moves a car up or down if possible and saves the move
        for car in list(dict.keys()):
            # moves a car of length 3 down
            if self.cars[car].orientation == "V" and self.cars[car].length == 3 and 1 in list(dict[car]):
                self.moves_made.append(self.board.make_move(car, 1))

                return True
            # moves a car of length 2 down or up if it is in the way of win car
            elif self.cars[car].orientation == "V" and (self.cars[car].position[0] == row_win_car or\
                 self.cars[car].position[0] + 1 == row_win_car and self.cars[car].length == 2):
                random_move = random.choice(list(dict[car]))
                self.moves_made.append(self.board.make_move(car, random_move))

                return True

        return False

    def move_random(self: First_Alg) -> Tuple[str, int]:
        """
            Returns a random move; a tuple with car object and the direction.
        """

        # chooses random move from dictionary
        car_move: str = random.choice(list(self.board.moves_dict.keys()))
        ran_choice = random.choice(self.board.moves_dict[car_move])

        return car_move, ran_choice

    def run_algorithm(self: First_Alg) -> None:
        """
            Runs the algoritm until the game is won.
            Makes use of moving win car to right, all horizontal cars to left,
            all vertical cars up or down and then random until in win position.
        """

        self.moves_made: List[Tuple[str, int]] = []
        
        # make steps in game until red car is in win position
        # print('-' * 80)
        while not self.board.win():
            # print('checking moves.......')
            if self.move_win_car():
                # print('found move!')
                continue
            elif self.cars_to_left():
                # print('found move!')
                continue
            elif self.cars_vertical():
                # print('found move!')
                continue
            else:
                # make random steps in game until red car is in win position
                rand_moves = 0
                while not self.board.win():
                    # print('random move: ', rand_moves)
                    if rand_moves == 20:
                        break
                    self.moves_made.append(self.board.make_move(*self.move_random()))
                    rand_moves += 1

        # make and store the final moves
        self.moves_made.extend(self.board.exit_moves())
        self.moves_made = merge_moves(self.moves_made)

        self.moves_amount: int = len(self.moves_made)