from __future__ import annotations

from csv import DictReader
import re
from typing import Tuple, List, Dict

from .car import Car


class InvalidMoveError(Exception):
    pass


class Board():

    def __init__(self: Board, filepath: str) -> None:
        """
            Setup board: create car objects and full game-board-grid with objects.
            Requires filepath as argument. Filepath name should include the dimensions
            of the game-board (row x col), i.e. 6x6 or 12x12 (with no numbers adjacent 
            to this part of the name!).
        """

        # parse board size from filename
        size = re.findall("[0-9]+x[0-9]+", filepath)[0].split('x')
        self.size: Tuple[int, int] = (int(size[0]), int(size[1]))

        # save board setup and place cars
        self._loader(filepath)

        # setup list to store all moves in
        self.moves_made: List[Tuple[str, int]] = []

        # save position when game should finished
        self.win_car: Car = self.cars['X']
        self.win_postition: Tuple[int, int] = (self.win_car.position[0], self.size[1] - 2)

        # setup first grid
        self._update_grid()

    def __str__(self: Board) -> str:
        """
            Return current game board in readable format.
        """

        # make grid with car object names and dots for empty spaces
        rep = '\n'.join([''.join(['.' if cell is None else cell.name for cell in sublist]) for sublist in self.grid])
        return rep

    def _loader(self, filepath):
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
        self.cars: Dict[str, Car] = {}

        # go through lines in file
        with open(filepath, 'r') as file:

            # create car objects and place into list
            for row in DictReader(file):
                new_car = Car(*list(row.values()))
                self.cars[new_car.name] = new_car

    def _update_grid(self: Board) -> None:
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
        self._possible_moves()
    
    def _free_spot(self, position: Tuple[int, int]) -> bool:
        return self._within_range(position) and self.grid[position[0]][position[1]] == None

    def _possible_moves(self) -> None:
        """
            Returns a dictionary with all cars that can move in the current board setup
            and the directions they can move in.
        """
        
        self.possible_moves: List[Tuple[str, int]] = []

        check_distances: List[int] = list(range(-1 * max(self.size) + 2, 0)) + list(range(1, max(self.size) - 1))

        for car in list(self.cars.values()):

            for distance in check_distances:

                check_positions: List[Tuple[int, int]] = car.test_move(distance)

                if all([self._free_spot(pos) for pos in check_positions]):

                    self.possible_moves.append((car.name, distance))

    def _within_range(self: Board, position: Tuple[int, int]) -> bool:
        """
            Returns bool, true if position is on the grid.
        """
        
        return 0 <= position[0] < self.size[0] and 0 <= position[1] < self.size[1]

    def set_board(self: Board, setup: str):
        """
            Setup the board accoring to a setup string. Setup string should be similar to
            the board representation this class creates and include all car names, orientations and
            lengths as the original board setup.
        """

        # TODO: input checks; 1) all cars present. 2) all orientations correct. 3) all lenghts correct

        # remove unnessessairy \n
        setup_str = setup.replace('\n', '')

        # get a list of all car names
        cars_repeats: str = setup_str.replace('.', '')
        cars: List[str] = list(set(cars_repeats))

        # find first occurence for eacht car and set it to that place
        for car in cars:

            # calculate the rows and colums
            str_place: int = setup_str.find(car)
            row: int = str_place // self.size[0]
            col: int = str_place % self.size[1]

            # set the car to that row and column
            self.cars[car].set_car(row, col)
        
        # update the board
        self._update_grid()

    def reset_board(self: Board) -> None:
        """
            Resets the board to it's original setup. Also clears all moves made.
        """

        # set all cars back to start position
        for car in list(self.cars.values()):
            car.reset_car()

        # clear moves made and reset grid
        self.moves_made = []
        self._update_grid()

    def make_move(self: Board, car: str, move: int) -> Tuple[str, int]:
        """
            Make a move on the board and return the move as a tuple.
        """

        # check if car parameter is of right type and value
        if not isinstance(car, str):
            raise TypeError(f'Car argument must be a string! Car is type {type(car)}')
        elif car not in list(self.cars.keys()):
            raise ValueError(f'No car with name {car} exists!')
        
        # check if move parameter is of right type and value
        if not isinstance(move, int):
            raise TypeError('Move argument must be integer!')
        elif move == 0:
            raise ValueError('Move cannot be 0!')

        # make sure move is valid
        if (car, move) not in self.possible_moves:
            raise InvalidMoveError('Given move is not possible with current board setup!')

        # move the car and update the grid
        self.cars[car].move(move)
        self._update_grid()

        # return the move as a tuple
        return (car, move)

    def win(self) -> bool:
        for i in range(self.win_car.position[1] + 2, self.size[1]):
            if self.grid[self.win_car.position[0]][i] is not None:
                return False

        return True
    
    def on_win_position(self: Board) -> bool:
        return self.win_car.position == self.win_postition

    def exit_moves(self):
        last_moves: List[Tuple[Car, int]] = []

        while self.win_car.position != self.win_postition:
            # self._possible_moves()
            last_moves.append(self.make_move(self.win_car.name, 1))
            self._update_grid()
        
        return last_moves
