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

    def _positions_update(self: Car) -> None:
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
    
    def set_car(self: Car, row: int, col: int) -> None:
        """
            Set the car to a specific positions. Indexing starts at 0.
        """

        self.position = (row, col)
        self._positions_update()

    def reset_car(self: Car) -> None:
        """
            Resets the car to it's original position.
        """
        self.position = self.start_position
        self._positions_update()

    def test_move(self: Car, direction: int) -> Tuple[int, int]:
        """
            Method returns a position coordinate of the spot that is taken up when
            the car moves in the provided direction.

            Requires non-zero direction parameter.
        """

        # ensure proper usage
        if not isinstance(direction, int):
            raise TypeError('Direction must be of type \'int\'.')
        if direction == 0:
            raise ValueError('Direction must be non-zero.')

        # derive index of self.positions list that is the in the movement direction
        if direction > 0:
            list_index: int = -1
        else:
            list_index = 0

        # movement up/down or left/right depending on orientation
        if self.orientation == 'H':
            test_pos: Tuple[int, int] = (self.position[0], self.positions[list_index][1] + direction)
        else:
            test_pos = (self.positions[list_index][0] + direction, self.position[1])

        return test_pos

    def move(self: Car, move: int) -> None:
        """
            Change car position on gameboard.

            Move can be a positive or negative integer. Positive values will move the car
            up or to the right, while negative integers will move down or to the left (all
            with respect to cars orientation).
        """

        # ensure proper usage
        if not isinstance(move, int):
            raise TypeError('Move must be of type \'int\'.')
        if move == 0:
            raise ValueError('Value for move must be non-zero.')

        # change position depending on cars orientation
        if self.orientation == 'H':
            self.position = (self.position[0], self.position[1] + move)
        else:
            self.position = (self.position[0] + move, self.position[1])

        # update the positions the car takes up
        self._positions_update()
