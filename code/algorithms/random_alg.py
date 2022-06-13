from __future__ import annotations
from typing import Tuple, List
import random

class Random_Alg():

    def __init__(self: Random_Alg, board: Board) -> None:
        self.board = board


    def move(self: Random_Alg, dict: dict[Car, List[int]]):
        """
            Returns a random move; a tuple with car object and the direction.
            Requires a dictionary with all possible moves.
        """

        # chooses random move from dictionary
        car_move = random.choice(list(dict.items()))
        ran_choice = random.choice(car_move[1])

        return car_move[0], ran_choice

    def step_random(self, pos_moves=None):
        while not self.win():

            # if pos_moves == None:
            pos_moves = self.possible_moves()
            
            # if self.win_car_move(pos_moves):
            #     #self.update_grid()
            #     # self.print()
            # else: 
            self.random_final_move(pos_moves)
                #self.update_grid()
                # self.print()

            self.update_grid()
            # print(self.moves_made)

        while self.win_car.position != self.win_postition:
            pos_moves = self.possible_moves()
            self.win_car_move(pos_moves)
            
        # print('GEWONNEN')

    def step(self):

        while not self.board.win():
            pos_moves = self.board.possible_moves()

            move = self.move(pos_moves)

            self.board.make_move(*move)

            self.board.update_grid()

        self.board.exit_moves()