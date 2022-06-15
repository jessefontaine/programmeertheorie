from code.classes import Board

a = Board('game_boards/Rushhour6x6_1.csv')

print(a)

a.set_board('.FFBBB\n.CCEDD\nXXGE.I\nAAGHHI\nK.L.JJ\nK.L...')
print('-' * 30)

print(a)
