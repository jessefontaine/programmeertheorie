class Car():
    
    def __init__(self, name, orientation, col, row, length):
        self.name = name
        self.position = (int(row), int(col))
        self.orientation = orientation
        self.length = length

