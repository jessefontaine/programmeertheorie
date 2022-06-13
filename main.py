from code import Board
import pandas
import matplotlib.pyplot as plt
from argparse import ArgumentParser, Namespace
import os

def main(infile: str, outfolder: str, mode: str, runs: int):



    # batch run
    amt_list = batch_run(infile, runs)

    # plot all runs
    plt.hist(amt_list, density=True)

    try:
        os.makedirs(outfolder)
    except FileExistsError:
        pass

    plt.savefig(f"{outfolder}/{infile.split('/')[-1].split('.')[0]}_{mode}_{runs}.png")

    # convert to str and write to file
    amt_list = [str(x) for x in amt_list]
    with open(f"{outfolder}/{infile.split('/')[-1].split('.')[0]}_{mode}_{runs}.txt", 'w') as file:
        file.write('\n'.join(amt_list))


def batch_run(filepath, runs):
    list_amount_of_moves = []

    for i in range(runs):
        game = Board(filepath)
        game.step_random()
        df = pandas.DataFrame(game.moves_made, columns=['car', 'move'])
        list_amount_of_moves.append(len(df.index))
        print(f"run {i}/{runs}", end='\r')
    
    print('\n')

    return list_amount_of_moves

#print(batch_run("game_boards/Rushhour6x6_1.csv"))

if __name__ == "__main__":

    # setup cla parser
    parser: ArgumentParser = ArgumentParser(description="Run the rush-hour solver")

    # add cla's
    parser.add_argument('input_csv', help='gameboard csv file')
    parser.add_argument('output_folder', help='folder for output')
    parser.add_argument('mode', help='solver mode')
    parser.add_argument('runs', help='amount of runs')

    # read cla's
    args: Namespace = parser.parse_args()

    # call main with cla's
    main(args.input_csv, args.output_folder, args.mode, int(args.runs))
