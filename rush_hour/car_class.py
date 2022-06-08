from __future__ import annotations
from typing import Union, Tuple, List

class Car():

    def __init__(
        self: Car, 
        name: str, 
        orientation: str, 
        col: Union[int, str], 
        row: Union[int, str], 
        length: Union[int, str]
        ) -> None:

        self.name: str = name
        self.position: Tuple[int, int] = (int(row) - 1, int(col) - 1)
        self.orientation: str = orientation
        self.length: int = int(length)

        self.positions_update()

    def positions_update(self: Car) -> None:
        """
            Method updates the list of all positions the car object takes up on the game
            board.
        """

        # list comprehension method for updating all positions
        self.positions: List[Tuple[int, int]] = [
            (self.position[0], self.position[1] + i) if self.orientation == 'H' else 
            (self.position[0] + i, self.position[1]) 
            for i in range(self.length)
        ]
    
    def test_move(self, direction):
        if self.orientation == 'H':
            if direction > 0:
                test_pos = (self.positions[-1][0], self.positions[-1][1] + direction)
            elif direction < 0:
                test_pos = (self.positions[0][0], self.positions[0][1] + direction)
        else:
            if direction > 0:
                test_pos = (self.positions[-1][0] + direction, self.positions[-1][1])
            elif direction < 0:
                test_pos = (self.positions[0][0] + direction, self.positions[0][1])

        return test_pos

    def move(self: Car, move: int) -> None:
        """
            Change car position on gameboard. 

            Move can be a positive or negative integer. Positive values will move the car
            up or to the right, while negative integers will move down or to the left (all
            with respect to cars orientation).
        """

        # change position depending on cars orientation
        if self.orientation == 'H':
            self.position = (self.position[0], self.position[1] + move)
        else:
            self.position = (self.position[0] + move, self.position[1])

        # update the positions the car takes up
        self.positions_update()
