from __future__ import annotations
from typing import Tuple, List, Dict
from .car import Car
from csv import DictReader
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

    def __str__(self: Board) -> str:
        """
            return out current game board in readable format.
        """

        # make grid with car object names and dots for empty spaces
        rep = '\n'.join([''.join(['.' if cell is None else cell.name for cell in sublist]) for sublist in self.grid])
        return rep

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
        
        # calculate the possible moves with current board setup
        self.possible_moves()

    def possible_moves(self: Board) -> None:
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
                if self.within_range(test_pos) and self.grid[test_pos[0]][test_pos[1]] is None:
                    self.moves_dict[car].append(dir)

            # no possible moves deletes the key value pair
            if len(self.moves_dict[car]) == 0:
                del self.moves_dict[car]

    def make_move(self: Board, car: Car, move: int) -> None:
        """
            Make a move on the board.
        """

        # check if car parameter is of right type and value
        if not isinstance(car, Car):
            raise TypeError(f'Car argument must be Car object! Car is type {type(car)}')
        elif car not in list(self.cars.values()):
            raise ValueError(f'No car with name {car} exists!')
        
        # check if move parameter is of right type and value
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

    def win(self) -> bool:
        for i in range(self.win_car.position[1] + 2, self.size[1]):
            if self.grid[self.win_car.position[0]][i] is not None:
                return False

        return True

    def exit_moves(self):
        while self.win_car.position != self.win_postition:
            self.possible_moves()
            self.make_move(self.win_car, 1)
            self.update_grid()
