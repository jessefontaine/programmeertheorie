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
        """
            Returns a bool if a win car can go to right; if it does it makes the move and saves it.
        """

        dict = self.board.moves_dict

        # moves win car to right if possible and saves move
        if self.board.win_car in dict and 1 in list(dict[self.board.win_car]):
            self.moves_made.append(self.board.make_move(self.board.win_car, 1))

            return True

        return False

    def cars_to_left(self: First_Alg) -> bool:
        """
            Returns a bool if a horizontal car can go to left; if it does it makes the move and saves it.
        """

        dict = self.board.moves_dict

        # moves a car to the left if it is possible and saves move
        for car in dict:
            if car.orientation == "H" and -1 in list(dict[car]) and car.name != "X":
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
        for car in dict:
            # moves a car of length 3 down
            if car.orientation == "V" and car.length == 3 and 1 in list(dict[car]):
                self.moves_made.append(self.board.make_move(car, 1))
                
                return True
            # moves a car of length 2 down or up if it is in the way of win car
            elif car.orientation == "V" and (car.position[0] == row_win_car or\
                 car.position[0] + 1 == row_win_car and car.length == 2):
                random_move = random.choice(list(dict[car]))
                self.moves_made.append(self.board.make_move(car, random_move))
                
                return True

        return False

    def move_random(self: First_Alg) -> Tuple[Car, int]:
        """
            Returns a random move; a tuple with car object and the direction.
        """

        # chooses random move from dictionary
        car_move: Car = random.choice(list(self.board.moves_dict.keys()))
        ran_choice = random.choice(self.board.moves_dict[car_move])

        return (car_move, ran_choice)

    def step(self) -> None:
        """
            Runs the algoritm until the game is won.
            Makes use of moving win car to right, all horizontal cars to left, 
            all vertical cars up or down and then random until in win position.
        """

        # make steps in game until red car is in win position
        while not self.board.win():
            if self.move_win_car():
                pass
            elif self.cars_to_left():
                pass
            elif self.cars_vertical():
                pass
            else:
                # make random steps in game until red car is in win position
                while not self.board.win():
                    self.moves_made.append(self.board.make_move(*self.move_random()))

        # make and store the final moves
        self.moves_made.extend(self.board.exit_moves())

