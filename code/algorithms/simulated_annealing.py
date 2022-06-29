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

from math import log
from random import uniform
from typing import Tuple

from code.algorithms import HC
from code.settings import START_TEMPERATURE, LINEAR_TEMP_PROCESS


class SA(HC):
    """
    The Simulated Annealing class runs a hill climber algorithm.
    Impoves solution by changing small parts of the solution, for given amount of iterations.
    Accepts changes with an acceptance chance.
    """

    # ensure proper usage
    if START_TEMPERATURE < 0:
        raise ValueError("Value for start temperature must be zero or positive.")

    def _choose_interval(
        self,
        iteration: int,
    ) -> Tuple[int, int]:
        """
        Returns interval within range that is smaller then length of solutions.
        Modified for simulated annealing.
        """

        # calculate the interval size to try and improve
        start_interval: int
        start_interval, _ = super()._choose_interval(iteration)

        # switch to choose the temperature formula and calculate
        linear: bool = LINEAR_TEMP_PROCESS
        start_temp: int = START_TEMPERATURE

        if linear:
            temperature: float = start_temp - (start_temp / self.iteration) * iteration
        else:
            temperature = start_temp * pow(0.997, iteration)

        # calculate probavility and new interval size
        probability: float = uniform(0.0, 1.0)
        new_interval: float = -temperature * log(probability, 2) + start_interval

        return start_interval, int(new_interval)
