"""
car.py

Programmeertheorie Rush Hour

Jesse Fontaine - 12693375
Annemarie Geertsema - 12365009
Laura Haverkorn - 12392707

- Contains class Car.
- Functions to set, reset and update the positions.
- Functions to make and test moves.
"""

from __future__ import annotations
from typing import Iterable, Union, Tuple, List


class Car:
    def __init__(
        self,
        name: str,
        orientation: str,
        col: Union[int, str],
        row: Union[int, str],
        length: Union[int, str],
    ) -> None:
        """
        Instantiate car object with given parameters.
        Requires orientation the be either 'V' or 'H'.
        """

        # save object variables
        self.name: str = name
        self.start_position: Tuple[int, int] = (int(row) - 1, int(col) - 1)
        self.position: Tuple[int, int] = (int(row) - 1, int(col) - 1)
        self.orientation: str = orientation
        self.length: int = int(length)

        # create list of all positions on the grid the car takes up
        self._positions_update()

    def _positions_update(self) -> None:
        """
        Method updates the list of all positions the car object takes up on the game
        board.
        """

        # list comprehension method for updating all positions
        self.positions: List[Tuple[int, int]] = [
            (self.position[0], self.position[1] + i)
            if self.orientation == "H"
            else (self.position[0] + i, self.position[1])
            for i in range(self.length)
        ]

    def set_car(self, row: int, col: int) -> None:
        """
        Set the car to a specific positions. Indexing starts at 0.
        """

        self.position = (row, col)
        self._positions_update()

    def reset_car(self) -> None:
        """
        Resets the car to it's original position.
        """

        self.position = self.start_position
        self._positions_update()

    def set_offset(self, offset):
        self.position = self.start_position
        if not offset == 0:
            self.move(offset)
        else:
            self._positions_update()

    def test_moves(self, board_size):
        """
        Method returns a position coordinate of the spot that is taken up when
        the car moves in the provided direction.

        Requires non-zero direction parameter.
        """

        # forward
        max_moves = board_size - self.length

        if self.orientation == "V":
            positive_dir_list = [
                (self.positions[-1][0] + move, self.position[1])
                for move in range(1, max_moves + 1)
            ]
            negative_dir_list = [
                (self.positions[0][0] - move, self.position[1])
                for move in range(1, max_moves + 1)
            ]
        else:
            positive_dir_list = [
                (self.position[0], self.positions[-1][1] + move)
                for move in range(1, max_moves + 1)
            ]
            negative_dir_list = [
                (self.position[0], self.positions[0][1] - move)
                for move in range(1, max_moves + 1)
            ]

        return positive_dir_list, negative_dir_list

    def move(self, move: int) -> None:
        """
        Change car position on gameboard.

        Move can be a positive or negative integer. Positive values will move the car
        up or to the right, while negative integers will move down or to the left (all
        with respect to cars orientation).
        """

        # ensure proper usage
        if not isinstance(move, int):
            raise TypeError("Move must be of type 'int'.")
        if move == 0:
            raise ValueError("Value for move must be non-zero.")

        # change position depending on cars orientation
        if self.orientation == "H":
            self.position = (self.position[0], self.position[1] + move)
        else:
            self.position = (self.position[0] + move, self.position[1])

        # update the positions the car takes up
        self._positions_update()
