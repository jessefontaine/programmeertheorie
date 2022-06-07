from csv import reader
from car_class import Car

def loader(filepath):

    cars = []
    
    with open(filepath, 'r') as file:
        
        csv_reader = reader(file)

        for row in csv_reader:
            cars.append(Car(*row))
    
    return cars
