"""
simulated_annealing.py

Programmeertheorie Rush Hour

Jesse Fontaine - 12693375
Annemarie Geertsema - 12365009
Laura Haverkorn - 12392707

- Contains class SA (Simulated Annealing) inherits HC (Hill Climber).
- Contains an different accept insert function then normal Hill Climber.
"""

from __future__ import annotations
from typing import Tuple

from random import uniform
from math import log

from code.algorithms import HC


class SA(HC):
    """
    The Simulated Annealing class runs a hill climber algorithm.
    Impoves solution by changing small parts of the solution, for given amount of iterations.
    Accepts changes with an acceptance chance.
    """

    def _choose_interval(
        self,
        iteration: int,
    ) -> Tuple[int, int]:
        """
        Returns interval within range that is smaller then length of solutions.
        Modified for simulated annealing.
        """

        start_interval, _ = super()._choose_interval(iteration)

        linear: bool = True

        probability: float = uniform(0.0, 1.0)

        if linear:
            start_temp: int = 15
            temperature: float = start_temp - (start_temp / self.iteration) * iteration
        else:
            start_temp = 80
            temperature = start_temp * pow(0.997, iteration)

        new_interval: float = -temperature * log(probability, 2) + start_interval

        return start_interval, int(new_interval)
