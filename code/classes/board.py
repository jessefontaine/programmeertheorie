from __future__ import annotations
from logging import exception
from typing import Tuple, List, Dict
from .car import Car
from csv import DictReader
import random
import re


class ImpossibleMoveError(Exception):
    pass

class Board():

    def __init__(self: Board, filepath: str) -> None:
        """
            Setup board: create car objects and full game-board-grid with objects.
            Requires filepath as argument. Filepath name should include the dimensions
            of the game-board, i.e. 6x6 or 12x12 (with no numbers adjacent to this part
            of the name!).
        """
        
        # parse board size from filename
        size = re.findall("[0-9]+x[0-9]+", filepath)[0].split('x')
        self.size: Tuple[int, int] = (int(size[0]), int(size[1]))

        # save board setup and place cars
        self.loader(filepath)

        # setup list to store all moves in
        self.moves_made: List[Tuple[str, int]] = []

        # save position when game should finished
        self.win_car: Car = self.cars['X']
        self.win_postition: Tuple[int, int] = (self.win_car.position[0], self.size[1] - 2)

        # setup first grid
        self.update_grid()

    def loader(self, filepath):
        """
            Using the path to a game_board csv-file, create and place Car objects
            into list, then return.

            Requires Car class.
        """

        # ensure argument contains board dimensions
        if not re.compile(r"[^0-9][0-9]+x[0-9]+[^0-9]").search(filepath):
            raise ValueError(
                'Given filepath argument does not contain board dimensions in proper format.'
            )

        # list for car objects
        self.cars: Dict[Car] = {}

        # go through lines in file
        with open(filepath, 'r') as file:

            # create car objects and place into list
            for row in DictReader(file):
                new_car = Car(*list(row.values()))
                self.cars[new_car.name] = new_car

    def update_grid(self: Board) -> None:
        """
            Creates/updates the current game board. The board consists of a nested list.
            Every occupied space holds the car object that occupies it. Unoccupied space is
            marked with `None`
        """

        # create empty nested list to store occupied spaces
        self.grid: List[List] = [[None for _ in range(self.size[1])] for _ in range(self.size[0])]

        # loop through every cars occupied positions and place car object on grid
        for car in list(self.cars.values()):
            for pos in car.positions:
                self.grid[pos[0]][pos[1]] = car

    def possible_moves(self: Board) -> dict[Car, List[int]]:
        """
            Returns a dictionary with all cars that can move in the current board setup
            and the directions they can move in.
        """

        # create dictionary to store possible moves in
        self.moves_dict: dict[Car, List[int]] = {}

        # loop through all cars to find their moves
        for car in list(self.cars.values()):

            # initialise key value par with empty list for storing moves
            self.moves_dict[car] = []

            # moves can be either forward or backward
            for dir in [-1, 1]:

                # Car returns the spot that would be taken up by the move. saved if valid
                test_pos: Tuple[int, int] = car.test_move(dir)
                if self.within_range(test_pos) and self.grid[test_pos[0]][test_pos[1]] == None:
                    self.moves_dict[car].append(dir)

            # no possible moves deletes the key value pair
            if len(self.moves_dict[car]) == 0:
                del self.moves_dict[car]

        return self.moves_dict

    def make_move(self: Board, car: Car, move: int) -> None:

        if not isinstance(car, Car):
            raise TypeError(f'Car argument must be Car object! Car is type {type(car)}')
        elif car not in list(self.cars.values()):
            raise ValueError(f'No car with name {car} exists!')
        
        if not isinstance(move, int):
            raise TypeError('Move argument must be integer!')
        elif move == 0:
            raise ValueError('Move cannot be 0!')

        if move not in self.moves_dict[car]:
            raise ImpossibleMoveError('Given move is not possible with current board setup!')
        
        car.move(move)
        self.update_grid()

    def within_range(self: Board, position: Tuple[int, int]) -> bool:
        """
            Returns bool, true if position is on the grid.
        """
        return 0 <= position[0] < self.size[0] and 0 <= position[1] < self.size[1]

    """
        def random_final_move(self: Board, dict: dict[Car, List[int]]):
            

         
            car_move = random.choice(list(dict.items()))
            ran_choice = random.choice(car_move[1])
            car_move[0].move(ran_choice)
            self.move_made_to_file((car_move[0].name, ran_choice))
    """

    def win(self) -> bool:
        for i in range(self.win_car.position[1] + 2, self.size[1]):
            if self.grid[self.win_car.position[0]][i] != None:
                return False

        return True

    def print(self: Board) -> None:
        """
            Print out current game board in readable format.
        """

        # print grid with car object names and dots for empty spaces
        print(
            '\n'.join(
                [''.join(
                    ['.' if cell == None else cell.name for cell in sublist]
                ) for sublist in self.grid]
            ), '\n' + self.size[0] * '#'
        )

    """
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
            elif car.orientation == 'V' and (car.position[0] == row_win_car or \
                 car.position[0] + 1 == row_win_car) and car.length == 2:
                 
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
        # print('GEWONNEN')

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

        while self.win_car.position != self.win_postition:
            pos_moves = self.possible_moves()
            self.win_car_move(pos_moves)
            
    """
