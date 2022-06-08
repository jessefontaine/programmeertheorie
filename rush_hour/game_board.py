from __future__ import annotations
from typing import Tuple
from loader import loader
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

    def possible_moves(self):
        moves_dict = {}

        # checks for each car what possible moves are
        for car in self.car_list:
            moves_dict[car] = []

            # checks for horizontal/vertical orientation if car can go left/right/up/down
            if car.orientation == "H":
                # can car to left and is the spot empty
                if self.within_range((car.position[0], car.position[1] - 1)):
                    if self.grid[car.position[0]][car.position[1] - 1] == " ":
                        moves_dict[car].append(-1)

                # can car to left and is the spot empty
                if self.within_range((car.position[0], car.position[1] + car.length)):
                    if self.grid[car.position[0]][car.position[1] + car.length] == " ":
                        moves_dict[car].append(1)
            else:
                # can car up and is the spot empty
                if self.within_range((car.position[0] - 1, car.position[1])):
                    if self.grid[car.position[0] - 1][car.position[1]] == " ":
                        moves_dict[car].append(-1)

                # can car down and is the spot empty
                if self.within_range((car.position[0] + car.length, car.position[1])):
                    if self.grid[car.position[0] + car.length][car.position[1]] == " ":
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
    
    def update_grid(self):
        self.gridrow = []

        # create row of grid
        for i in range(int(self.size[0])):
            self.gridrow.append(" ")

        # create grid
        self.grid = []
        for i in range(int(self.size[1])):
            self.grid.append(list(self.gridrow))

        # fill grid with cars
        for car in self.car_list:
            for i in range(car.length):
                if car.orientation == "H":
                    self.grid[car.position[0]][car.position[1] + i] = car.name
                else:
                    self.grid[car.position[0] + i][car.position[1]] = car.name

        self.print()

    def win(self):
        if self.win_postition == self.win_car.position:
            return True

        return False
    
    def print(self: Board) -> None:
        """
            Print out current game board in readable format
        """
        print(
            '\n'.join(
                [''.join(
                    [char if char != ' ' else '.' for char in sublist]
                ) for sublist in self.grid]
            )
        )
       
        
    def step(self):
        while not self.win():
            random_move = self.random_final_move(self.possible_moves())
            self.print_move_made(random_move)
            self.update_grid()
            print('no')
        print('yes')
            
    def print_move_made(self, move):
        print(move[0].name)
        if move[0].orientation == 'H':
            if move[1][0] < 0:
                print(move[0].name, 'L')
            else:
                print(move[0].name, 'R')
        else:
            if move[1][0] < 0:
                print(move.name, 'U')
            else:
                print(move.name, 'D')
        

if __name__ == "__main__":
    a = Board("game_boards/Rushhour6x6_easywin.csv")
    a.step()
    # print(a.win())
    # a.random_final_move(a.possible_moves())
    # a.update_grid()
    # print(a.win())
    # a.random_final_move(a.possible_moves())
    # a.update_grid()

