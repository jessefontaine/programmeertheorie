from __future__ import annotations
from typing import Tuple, List, Set, Union, Optional
from code.classes import Board, Node

class BaseAlg:

    def __init__(
        self, 
        board: Board, 
        depth: int = None, 
        start_node: Union[Node, None] = None, 
        end_node: Union[Node, None] = None
        ) -> None:

        # save the gameboard and maximum depth constructive algorithms can go
        self.board: Board = board
        self.depth: Optional[int] = depth
        
        # starting without a start node means the current gameboard setup is the start
        if start_node is None:
            self.start_node: Node = Node(str(self.board))
        else:
            self.start_node = start_node

        # starting without an end node means the algorithm will try to find a winning setup
        if end_node is None:
            self.find_win: bool = True
        else:
            self.find_win = False
            self.end_node: Node = end_node
        
    def check_finished(self, state: Node) -> bool:
        """
        Checks whether a given state satisfies the constraints.
        """

        # setup the board according to the given state
        self.board.set_board(state.board_rep)

        # return whether contraints are satisfied
        if self.find_win:
            return self.board.on_win_position()
        else:
            return state.board_rep == self.end_node.board_rep
        
    def create_run_data(self, final_node: Node) -> None:
        """
        After a run, calculate the data for the found solution
        """

        # lists to store the data in
        self.node_list = []
        self.moves_made = []

        # moves counter
        self.moves_amount = 0

        # moving backwards from the winning node, construct the entire node list
        current: Node = final_node
        while current is not self.start_node:

            # save the data
            self.node_list.append(current)
            self.moves_made.append(current.step_taken)
            self.moves_amount += 1

            # switch to the parent
            current = current.parent
        
        # append the first node
        self.node_list.append(self.start_node)

        # invert all lists, since they are built from children to parents
        self.node_list = self.node_list[::-1]
        self.moves_made = self.moves_made[::-1]

    def reset_algorithm(self):
        self.node_list: List[Node] = [Node(str(self.board))]
        self.moves_made: List[Optional[Tuple[str, int]]] = []

    def algorithm(self) -> Node:
        raise NotImplementedError
    
    def run_algorithm(self) -> Tuple[Node, Node]:
        end_state: Node = self.algorithm()
        self.create_run_data(end_state)

        return self.start_node, end_state