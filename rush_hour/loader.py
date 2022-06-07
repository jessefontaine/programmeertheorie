# import pandas as pd

# # saves data from input file to dataframe
# data_df = pd.read_csv("game_boards/Rushhour6x6_1.csv")

# print(data_df)
import csv

def loader(filepath):
    
    with open(filepath) as file:
        file_reader = csv.DictReader(file)

        line = file_reader.fieldnames

        print(line)

if __name__ == "__main__":
    loader("game_boards/Rushhour6x6_1.csv")