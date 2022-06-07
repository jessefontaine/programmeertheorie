from __future__ import annotations
from typing import Union, Tuple

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

    def move(self: Car, move: int) -> None:
        """
            Change car position on gameboard. 

            Move can be a positive or negative integer. Positive values will move the car
            up or to the right, while negative integers will move down or to the left (all
            with respect to cars orientation).
        """

        # change position depending on cars orientation
        if self.orientation == 'H':
            self.position = (self.position[0] + move, self.position[1])
        else:
            self.position = (self.position[0], self.position[1] + move)
