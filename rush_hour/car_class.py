class Car():
    
    def __init__(self, name, orientation, col, row, length):
        self.name = name
        self.position = (int(row) - 1, int(col) - 1)
        self.orientation = orientation
        self.length = int(length)

