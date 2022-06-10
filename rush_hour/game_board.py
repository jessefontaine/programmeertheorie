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

        self.car_list: List[Car] = loader(filepath)
        self.moves_made: List[Tuple[str, int]] = []

        # save position when game should finished
        for car in self.car_list:
            if car.name == "X":
                self.win_postition: Tuple[int, int] = (car.position[0], self.size[1] - 2)
                self.win_car: Car = car

        # setup first grid and print
        self.update_grid()
        self.print()

    def possible_moves(self: Board) -> dict[Car, List[int]]:
        """
            Returns a dictionary with all cars that can move in the current board setup
            and the directions they can move in.
        """

        # create dictionary to store possible moves in
        moves_dict: dict[Car, List[int]] = {}

        # loop through all cars to find their moves
        for car in self.car_list:

            # initialise key value par with empty list for storing moves
            moves_dict[car] = []

            # moves can be either forward or backward
            for dir in [-1, 1]:

                # Car returns the spot that would be taken up by the move. saved if valid
                test_pos: Tuple[int, int] = car.test_move(dir)
                if self.within_range(test_pos) and self.grid[test_pos[0]][test_pos[1]] == None:
                    moves_dict[car].append(dir)

            # no possible moves deletes the key value pair
            if len(moves_dict[car]) == 0:
                del moves_dict[car]

        return moves_dict
    
    def within_range(self: Board, position: Tuple[int, int]) -> bool:
        """
            Returns bool, true if position is on the grid.
        """
        return 0 <= position[0] < self.size[0] and 0 <= position[1] < self.size[1]

    def random_final_move(self, dict):
        # for car in dict:
        #     print(car.name, dict[car])
        # random choice from the dictionary
        car_move = random.choice(list(dict.items()))
        ran_choice = random.choice(car_move[1])
        car_move[0].move(ran_choice)
        self.print_move_made((car_move[0], ran_choice))
        self.move_made_to_file((car_move[0].name, ran_choice))

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
        for i in range(self.win_car.position[1] + 2, self.size[1]):
            if self.grid[self.win_car.position[0]][i] != None:
                return False

        return True

    def print(self: Board) -> None:
        """
            Print out current game board in readable format.
        """
        print(
            '\n'.join(
                [''.join(
                    ['.' if cell == None else cell.name for cell in sublist]
                ) for sublist in self.grid]
            ), '\n' + self.size[0] * '#'
        )

    def print_move_made(self, move):
        if move[0].orientation == 'H':
            if move[1] < 0:
                print(move[0].name, 'L')
            else:
                print(move[0].name, 'R')
        else:
            if move[1] < 0:
                print(move[0].name, 'U')
            else:
                print(move[0].name, 'D')

    def move_made_to_file(self, move):
        self.moves_made.append(move)

    def win_car_move(self, moves_dict):
        if self.win_car in moves_dict and 1 in list(moves_dict[self.win_car]):
            self.win_car.move(1)
            self.print_move_made((self.win_car, 1))
            return True

        return False

    def cars_to_left(self, moves_dict):
        #for car in self.car_list:
        for car in moves_dict:
            if car.orientation == 'H' and -1 in list(moves_dict[car]) and car.name != "X":
                car.move(-1)
                self.print_move_made((car, -1))
                return True

        return False

    def cars_move_vertical(self, moves_dict):
        row_win_car = self.win_car.position[0]
        #for car in self.car_list:
        for car in moves_dict:
            if car.orientation == 'V' and car.length == 3 and 1 in list(moves_dict[car]):
                car.move(1)
                self.print_move_made((car, 1))
                return True
            elif car.orientation == 'V' and (car.position[0] == row_win_car or car.position[0] + 1 == row_win_car) and car.length == 2:
                random_move = random.choice(list(moves_dict[car]))
                car.move(random_move)
                self.print_move_made((car, random_move))

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

    def step(self):
        while not self.win():
            pos_moves = self.possible_moves()
            if self.win_car_move(pos_moves):
                pass
            elif self.cars_to_left(pos_moves):
                pass
            elif self.cars_move_vertical(pos_moves):
                pass
            else:
                self.step_random(pos_moves)
                break
            self.update_grid()
            # self.print()
        print('GEWONNEN')

    def step_random(self, pos_moves=None):
        while not self.win():

            # if pos_moves == None:
            pos_moves = self.possible_moves()
            
            # if self.win_car_move(pos_moves):
            #     #self.update_grid()
            #     # self.print()
            # else: 
            self.random_final_move(pos_moves)
                #self.update_grid()
                # self.print()

            self.update_grid()
            # print(self.moves_made)
            
        print('GEWONNEN')
        

if __name__ == "__main__":
    a = Board("game_boards/Rushhour6x6_easywin.csv")

    a.step_random()

    import pandas

    pandas.DataFrame(a.moves_made, columns=['car', 'move']).to_csv('output.csv', index=False)
    # print(moves)
