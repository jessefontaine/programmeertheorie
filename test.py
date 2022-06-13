from code import Board, Random_Alg


b = Board("game_boards/Rushhour6x6_3.csv")

alg = Random_Alg(b)

print(alg)

alg.step()

print(alg.board)

