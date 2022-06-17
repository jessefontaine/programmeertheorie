from __future__ import annotations

from typing import List, Dict, Tuple, Union
from queue import Queue


from .node import Node
from code.classes import Board
from code.functions.functions import merge_moves


class Bfs():

    def __init__(self: Bfs, board: Board, depth: int, endboard: str = None):
        self.board: Board = board
        self.depth: int = depth
        self.endboard: Union[str, None] = endboard        
    
    def run_algorithm(self: Bfs):

        # save begin state from the board        
        begin_state: Node = Node(str(self.board))

        # list to store all useful nodes in
        unique_nodes: List[Node] = [begin_state]

        # set for storing unique boards
        unique_boards: set[str] = set([begin_state.board_rep])

        # create queue
        layer: Queue = Queue()

        # add begin state to queue
        layer.put(begin_state)

        # win condition
        win_found = False

        while not layer.empty() and not win_found:

            # get the top of the queue
            state: Node = layer.get()
            self.board.set_board(state.board_rep)
            # print(f'Moves: {state.steps_taken}\n{state.board_rep}\n' + '-' * 80)
            print(f'depth: {len(state.steps_taken)}/{self.depth}', end='\r')

            # go no deeper than depth
            if len(state.steps_taken) < self.depth:

                # get all possible actions
                actions: List[Tuple[str, int]] = self.board.possible_moves

                # loop through all actions
                for move in actions:
                    # set the board to the mother state and make the move
                    self.board.set_board(state.board_rep)
                    self.board.make_move(*move)

                    board_rep = str(self.board)

                    if board_rep not in unique_boards:
                        
                        # make new node
                        child: Node = Node(board_rep)
                        steps = state.steps_taken[:]
                        steps.append(move)
                        child.steps_taken = steps

                        # add the node to the list of nodes
                        unique_nodes.append(child)

                        # add that nodes board representation to the set
                        unique_boards.add(board_rep)

                        # add node to queue
                        layer.put(child)

                    if self.endboard == None:
                        win_found = self.board.on_win_position()
                    else:
                        win_found = self.endboard == str(self.board)

                    if win_found:
                        break

        self.moves_made: List[Tuple[str, int]] = unique_nodes[-1].steps_taken
        # self.moves_made = merge_moves(self.moves_made)
        self.moves_amount: int = len(unique_nodes[-1].steps_taken)

