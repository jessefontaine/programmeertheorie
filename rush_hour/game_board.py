from __future__ import annotations
from typing import Tuple
from loader import loader
import re

class Board():

    def __init__(self: Board, filepath: str) -> None:

        # parse board size from filename
        self.size = re.findall("[0-9]x[0-9]", filepath)[0].split('x')

        
        self.gridline = []
        for i in range(int(self.size[0])):
            self.gridline.append(" ")
        self.grid = []
        for i in range(int(self.size[1])):
            self.grid.append(list(self.gridline))

        self.car_list = loader(filepath)

        for car in self.car_list:
            for i in range(car.length):
                if car.orientation == "H":
                    self.grid[car.position[0]][car.position[1] + i] = car.name
                else:
                    self.grid[car.position[0] + i][car.position[1]] = car.name
        print(self.grid)

    def possible_moves(self):
        dict = {}
        for car in self.car_list:
            dict[car] = []

        for car in self.car_list:
            if car.orientation == "H":
                print(car.position, car.name)

                if self.within_range((car.position[0], car.position[1] - 1)):
                    if self.grid[car.position[0]][car.position[1] - 1] == " ":
                        dict[car].append("L")

                if self.within_range((car.position[0], car.position[1] + car.length)):
                    if self.grid[car.position[0]][car.position[1] + car.length] == " ":
                        dict[car].append("R")
            else:
                print(car.position, car.name)

                if self.within_range((car.position[0] - 1, car.position[1])):
                    if self.grid[car.position[0] - 1][car.position[1]] == " ":
                        dict[car].append("U")

                if self.within_range((car.position[0] + car.length, car.position[1])):
                    if self.grid[car.position[0] + car.length][car.position[1]] == " ":
                        dict[car].append("D")
        print(dict)
    
    def within_range(self: Board, position: Tuple[int, int]) -> bool:
        return 0 < position[0] < self.size[0] and 0 < position[1] < self.size[1]

if __name__ == "__main__":
    a = Board("game_boards/Rushhour6x6_3.csv")
    a.possible_moves()