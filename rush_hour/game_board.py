from __future__ import annotations
from typing import Tuple
from loader import loader
import random
import re

class Board():

    def __init__(self: Board, filepath: str) -> None:

        # parse board size from filename
        size = re.findall("[0-9]x[0-9]", filepath)[0].split('x')
        self.size = (int(size[0]), int(size[1]))

        
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
        moves_dict = {}

        for car in self.car_list:
            moves_dict[car] = []

            if car.orientation == "H":
                if self.within_range((car.position[0], car.position[1] - 1)):
                    if self.grid[car.position[0]][car.position[1] - 1] == " ":
                        moves_dict[car].append("L")

                if self.within_range((car.position[0], car.position[1] + car.length)):
                    if self.grid[car.position[0]][car.position[1] + car.length] == " ":
                        moves_dict[car].append("R")
            else:
                if self.within_range((car.position[0] - 1, car.position[1])):
                    if self.grid[car.position[0] - 1][car.position[1]] == " ":
                        moves_dict[car].append("U")

                if self.within_range((car.position[0] + car.length, car.position[1])):
                    if self.grid[car.position[0] + car.length][car.position[1]] == " ":
                        moves_dict[car].append("D")

            if len(moves_dict[car]) == 0:
                del moves_dict[car]

        return moves_dict
    
    def within_range(self: Board, position: Tuple[int, int]) -> bool:
        return 0 <= position[0] < self.size[0] and 0 <= position[1] < self.size[1]

    def random_final_move(self, dict):
        return random.choice(list(dict.items()))

if __name__ == "__main__":
    a = Board("game_boards/Rushhour6x6_1.csv")
    b = a.possible_moves()
    print(b)
    c = a.random_final_move(b)
    print(c)
