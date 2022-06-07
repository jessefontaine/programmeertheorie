from typing import Union, Tuple
from __future__ import annotations

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

