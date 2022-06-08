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

        # checks for each car what possible moves are
        for car in self.car_list:
            moves_dict[car] = []

            # checks for horizontal/vertical orientation if car can go left/right/up/down
            if car.orientation == "H":
                # can car to left and is the spot empty
                if self.within_range((car.position[0], car.position[1] - 1)):
                    if self.grid[car.position[0]][car.position[1] - 1] == None:
                        moves_dict[car].append(-1)

                # can car to left and is the spot empty
                if self.within_range((car.position[0], car.position[1] + car.length)):
                    if self.grid[car.position[0]][car.position[1] + car.length] == None:
                        moves_dict[car].append(1)
            else:
                # can car up and is the spot empty
                if self.within_range((car.position[0] - 1, car.position[1])):
                    if self.grid[car.position[0] - 1][car.position[1]] == None:
                        moves_dict[car].append(-1)

                # can car down and is the spot empty
                if self.within_range((car.position[0] + car.length, car.position[1])):
                    if self.grid[car.position[0] + car.length][car.position[1]] == None:
                        moves_dict[car].append(1)

            # removes cars that have no possible moves
            if len(moves_dict[car]) == 0:
                del moves_dict[car]

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
        print(self.win_car, moves_dict)
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
        self.grid: List[List[Optional[Car]]] = [[None for _ in range(self.size[1])] for _ in range(self.size[0])]

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
                    [cell.name if cell != None else '.' for cell in sublist]
                ) for sublist in self.grid]
            )
        )

    def step(self):
        while not self.win():
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
            print('no')
        print('yes')

    def step_random(self):
        while not self.win():
            pos_moves = self.possible_moves()
            self.random_final_move(pos_moves)
            self.update_grid()
        print('GEWONNEN')
        self.print()

            
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
        print(moves_dict)
        #for car in self.car_list:
        for car in moves_dict:
            if car.orientation == 'H' and -1 in list(moves_dict[car]):
                car.move(-1)
                return True, (car, [-1])

        return False, None
        

if __name__ == "__main__":
    a = Board("game_boards/Rushhour6x6_1.csv")
    a.step_random()

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

