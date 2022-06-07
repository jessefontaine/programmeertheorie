from loader import loader
import re

class Board():

    def __init__(self, filepath):

        # parse board size from filename
        self.grid_digits = re.findall("[0-9]x[0-9]", filepath)[0].split('x')

        
        self.gridline = []
        for i in range(int(self.grid_digits[0])):
            self.gridline.append(" ")
        self.grid = []
        for i in range(int(self.grid_digits[1])):
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

                if self.out_of_bounds((car.position[0], car.position[1] - 1)):
                    if self.grid[car.position[0]][car.position[1] - 1] == " ":
                        dict[car].append("L")

                if self.out_of_bounds((car.position[0], car.position[1] + car.length)):
                    if self.grid[car.position[0]][car.position[1] + car.length] == " ":
                        dict[car].append("R")
            else:
                print(car.position, car.name)

                if self.out_of_bounds((car.position[0] - 1, car.position[1])):
                    if self.grid[car.position[0] - 1][car.position[1]] == " ":
                        dict[car].append("U")

                if self.out_of_bounds((car.position[0] + car.length, car.position[1])):
                    if self.grid[car.position[0] + car.length][car.position[1]] == " ":
                        dict[car].append("D")
        print(dict)
    
    def out_of_bounds(self, position):
        if position[0] < 0 or position[0] >= len(self.grid):
            return False

        if position[1] < 0 or position[1] >= len(self.grid[0]):
            return False

        return True

if __name__ == "__main__":
    a = Board("game_boards/Rushhour6x6_3.csv")
    a.possible_moves()