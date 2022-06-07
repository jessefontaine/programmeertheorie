# import pandas as pd

# # saves data from input file to dataframe
# data_df = pd.read_csv("game_boards/Rushhour6x6_1.csv")

# print(data_df)

def loader(filepath):
    
    with open(filepath) as file:

        line = file.readline()
