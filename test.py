from code import Board, Random_Alg

from code.algorithms.first_alg import First_Alg

# b = Board("game_boards/Rushhour6x6_3.csv")

# alg = Random_Alg(b)

# print(alg)

# alg.step()

# print(alg.board)

c = Board("game_boards/Rushhour6x6_1.csv")

first_alg = First_Alg(c)

first_alg.step()
