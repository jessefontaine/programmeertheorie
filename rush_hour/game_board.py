from __future__ import annotations
from typing import Tuple, Union, Optional, List
from loader import loader
from car_class import Car
import random
import re

class Board():

    def __init__(self: Board, filepath: str) -> None:

        # parse board size from filename
        size = re.findall("[0-9]x[0-9]", filepath)[0].split('x')
        self.size: Tuple[int, int] = (int(size[0]), int(size[1]))

        self.car_list = loader(filepath)

        # save position when game should finished
        for car in self.car_list:
            if car.name == "X":
                self.win_postition = (car.position[0], self.size[1] - 2)
                self.win_car = car

        self.update_grid()
        self.print()

    def possible_moves(self):
        moves_dict = {}

        for car in self.car_list:
            moves_dict[car] = []
            for dir in [-1, 1]:
                test_pos = car.test_move(dir)
                if self.within_range(test_pos) and self.grid[test_pos[0]][test_pos[1]] == None:
                    moves_dict[car].append(dir)

        return moves_dict
    
    def within_range(self: Board, position: Tuple[int, int]) -> bool:
        """
            Returns bool, true if position is on the grid.
        """
        return 0 <= position[0] < self.size[0] and 0 <= position[1] < self.size[1]

    def random_final_move(self, dict):
        # random choice from the dictionary
        car_move = random.choice(list(dict.items()))
        car_move[0].move(car_move[1][0])
        return car_move
    
    def win_car_move(self, moves_dict):

        if self.win_car in moves_dict and 1 in list(moves_dict[self.win_car]):
            self.win_car.move(1)
            return True

        return False

    def update_grid(self: Board) -> None:
        """
            Creates/updates the current game board. The board consists of a nested list.
            Every occupied space holds the car object that occupies it. Unoccupied space is
            marked with `None`
        """

        # create empty nested list to store occupied spaces
        self.grid: List[List] = [[None for _ in range(self.size[1])] for _ in range(self.size[0])]

        # loop through every cars occupied positions and place car object on grid
        for car in self.car_list:
            for pos in car.positions:
                self.grid[pos[0]][pos[1]] = car

    def win(self):
        if self.win_postition == self.win_car.position:
            return True

        return False

    def print(self: Board) -> None:
        """
            Print out current game board in readable format.
        """
        print(
            '\n'.join(
                [''.join(
                    ['.' if cell == None else cell.name for cell in sublist]
                ) for sublist in self.grid]
            )
        )

    def step(self):
        # while not self.win():
        for _ in range(10):
            print('Step:')
            pos_moves = self.possible_moves()
            if self.win_car_move(pos_moves):
                self.print_move_made((self.win_car, [1]))
            else:
                left_move = self.cars_to_left(pos_moves)
                if left_move[0]:
                    self.print_move_made(left_move[1])
                else:
                    random_move = self.random_final_move(self.possible_moves())
                    self.print_move_made(random_move)
            self.update_grid()
            self.print()
            print('no\n\n\n')
        print('yes')
            
    def print_move_made(self, move):
        if move[0].orientation == 'H':
            if move[1][0] < 0:
                print(move[0].name, 'L')
            else:
                print(move[0].name, 'R')
        else:
            if move[1][0] < 0:
                print(move[0].name, 'U')
            else:
                print(move[0].name, 'D')

    def cars_to_left(self, moves_dict):
        #for car in self.car_list:
        for car in moves_dict:
            if car.orientation == 'H' and -1 in list(moves_dict[car]):
                car.move(-1)
                return True, (car, [-1])

        return False, None
        

if __name__ == "__main__":
    a = Board("game_boards/Rushhour6x6_easywin.csv")
    # a.win_car_move(a.possible_moves())
    # a.random_final_move(a.possible_moves())
    # a.update_grid()
    a.step()

    # print(' ')
    # a.print()
    # a.cars_to_left(a.possible_moves())
    # a.update_grid()


    # print(a.win())
    # a.random_final_move(a.possible_moves())
    # a.update_grid()
    # print(a.win())
    # a.random_final_move(a.possible_moves())
    # a.update_grid()

