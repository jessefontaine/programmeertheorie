from csv import reader
from car_class import Car
from typing import List

def loader(filepath: str) -> List[Car]:
    """
        Using the path to a game_board csv-file, create and place Car objects
        into list, then return.

        Requires Car class.
    """

    # list for car objects
    cars: List[Car] = []
    
    # go through lines in file
    with open(filepath, 'r') as file:
        
        # create car objects and place into list
        for row in reader(file):
            cars.append(Car(*row))
    
    return cars
