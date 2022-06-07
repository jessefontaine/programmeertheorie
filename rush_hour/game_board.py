from loader import loader
import re

class Board():

    def __init__(self):
        pass

    def load_board(self, filepath):
        grid_digits = re.findall("[0-9]x[0-9]", filepath)
        grid_digits = grid_digits[0].split('x')

        gridline = []
        for i in range(int(grid_digits[0])):
            gridline.append(" ")
        grid = []
        for i in range(int(grid_digits[1])):
            grid.append(list(gridline))

        car_list = loader("game_boards/Rushhour6x6_1.csv")

        for car in car_list:
            for i in range(car.length):
                if car.orientation == "H":
                    grid[car.position[0] - 1][car.position[1] + i - 1] = car.name
                else:
                    grid[car.position[0] + i - 1][car.position[1] - 1] = car.name

        print(grid)

if __name__ == "__main__":
    a = Board()
    a.load_board("game_boards/Rushhour6x6_1.csv")