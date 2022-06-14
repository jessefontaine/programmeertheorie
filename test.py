from code.algorithms import First_Alg, Random_Alg, Breadth_Alg, Deep_Alg
from code.classes import Board

a = Board("game_boards/Rushhour6x6_1.csv")

b = Deep_Alg(a)

b.run_algorithm()