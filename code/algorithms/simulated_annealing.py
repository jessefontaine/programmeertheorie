from __future__ import annotations

from random import uniform

from code.algorithms import HC


class SA(HC):
    def accept_insert(
        self, initial_size: int, insert_size: int, iteration: int
    ) -> bool:
        # acceptatiekans = 2( score_old – score_new ) / temperatuur
        # t = startT – (startT / aantal_iteraties) * i
        # t = startT * 0.997i

        start_temperature: int = 1000

        # temperature: float = (
        #     start_temperature - (start_temperature / self.iteration) * iteration
        # )
        temperature = start_temperature * pow(0.997, iteration)

        accept_chance: float = pow(2, ((initial_size - insert_size) / temperature))

        return uniform(0.0, 1.0) < accept_chance
