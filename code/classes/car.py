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

    def test_move(self, direction: int) -> List[Tuple[int, int]]:
        """
        Method returns a position coordinate of the spot that is taken up when
        the car moves in the provided direction.

        Requires non-zero direction parameter.
        """

        # ensure proper usage
        if not isinstance(direction, int):
            raise TypeError("Direction must be of type 'int'.")
        if direction == 0:
            raise ValueError("Direction must be non-zero.")

        # derive index of self.positions list that is the in the movement direction
        if direction > 0:
            car_side: Tuple[int, int] = self.positions[-1]
        else:
            car_side = self.positions[0]

        # list to store all positions in the car will drive over
        test_pos_list: List[Tuple[int, int]] = []

        if direction < 0:
            check_list: Iterable[int] = range(direction, 0)
        else:
            check_list = range(1, direction + 1)

        for distance in check_list:

            # movement up/down or left/right depending on orientation
            if self.orientation == "H":
                test_pos: Tuple[int, int] = (car_side[0], car_side[1] + distance)
            else:
                test_pos = (car_side[0] + distance, car_side[1])

            # add pos to list
            test_pos_list.append(test_pos)

        return test_pos_list

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
