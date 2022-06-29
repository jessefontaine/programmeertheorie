"""
settings.py

Programmeertheorie Rush Hour

Jesse Fontaine - 12693375
Annemarie Geertsema - 12365009
Laura Haverkorn - 12392707

- Parameters that are used in the algorithms
    can be changed as desired.


DEPTH: Maximum depth the breadth and depth search algorithms can go to.
    - Setting has a positive correlation to runtime and memory requirements

MIN_INTERVAL & MAX_INTERVAL: Minimum and maximum interval size the iterative 
algortihms can try to improve.
    - Max must be greater than min.
    - Min must be greater than zero.
    - Great intervals impact performance.

PLATEAU: Number of non improving iterations that run until the restart hillclimber 
terminates.
    - Must be higher than zero.
    - Smaller plateaus can hinder possible improvements that are eventually found.
    - Too great plateaus can unnessesarily increase runtime.

START_TEMPERATURE: Starting temperature for the simulated annealing. 
    - Effective starting temperature is very dependant on the game_board.
        - Shorter iterations experiments recommended before running longer sessions.
    - Too high starting temperatures allows the algorithm to worsen the solution to much
      before improving
    - Too low a value increases to odd of landing in a local minimum.

LINEAR_TEMP_PROCESS: Setting for the formula that plots temperature over iterations
to be linear (True) or exponential (False)
    - Either can be effective depending on the game board.

"""

DEPTH: int = 300
MIN_INTERVAL: int = 3
MAX_INTERVAL: int = 10
PLATEAU: int = 1000
START_TEMPERATURE: float = 30
LINEAR_TEMP_PROCESS: bool = True


# user setting checks
if DEPTH < 1:
    raise ValueError(f"DEPTH cannot be smaller than 1! Currently {DEPTH}")
if MIN_INTERVAL < 1:
    raise ValueError(f"MIN_INTERVAL must be greater than 0! Currently {MIN_INTERVAL}")
if MAX_INTERVAL < MIN_INTERVAL:
    raise ValueError(
        f"MAX_INTERVAL cannot be smaller than MIN_INTERVAL! {MAX_INTERVAL} < {MIN_INTERVAL}"
    )
if PLATEAU < 1:
    raise ValueError(f"PLATEAU must be greater than zero! Currently {PLATEAU}")
if START_TEMPERATURE < 0:
    raise ValueError(
        f"START_TEMPERATURE must be positive! Currently {START_TEMPERATURE}"
    )
