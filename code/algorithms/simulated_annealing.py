from __future__ import annotations

from random import uniform

from code.algorithms import HC


class SA(HC):
    def accept_insert(
        self, initial_size: int, insert_size: int, iteration: int
    ) -> bool:
        """
        Defines different accept rate for the Hill Climber algorithm.
        Returns if new solutions is accepted.
        """

        start_temperature: int = 5

        linear: bool = True

        if linear:
            temperature: float = (
                start_temperature - (start_temperature / self.iteration) * iteration
            )
        else:
            temperature = start_temperature * pow(0.997, iteration)

        accept_chance: float = pow(2, ((initial_size - insert_size) / temperature))

        print(
            f"initial: {initial_size}   insert: {insert_size}   ratio: {insert_size/initial_size}    accept: {accept_chance}"
        )

        return uniform(0.0, 1.0) <= accept_chance
