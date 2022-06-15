from code.algorithms import First_Alg, Random_Alg, Breadth_Alg, Depth_Alg
from code.classes import Board

a = Board("game_boards/Rushhour6x6_1.csv")

#print('AAAAAAAAAAAAAAAAAAAAAAAAAA\n',a, '\nAAAAAAAAAAAAAAAA')

b = Depth_Alg(a)

b.run_algorithm()


# setup_str: str = '.AABBB\n.CCEDD\nXXGE..\nFFGHHI\nK.LJJI\nK.L...'
# setup_str = setup_str.replace('\n', '')



# # get a list of all car names
# car_names_repeats = setup_str.replace('.', '')
# cars = list(set(car_names_repeats))



# print(cars)

