from tools import GRID_SIZE, PIECES_NUMBER, EMPTY_POSITION
from player import Player 
from piece import Piece
import numpy as np

class TerminalTest:
    def __init__(self):
        self._utilities = {}

    def utility(self, state):
        return self._utilities[state]

    def is_terminal(self, state):
        pass

class BoardTerminalTest(TerminalTest):
    def is_terminal(self, board):
        
        player = board.game_turn.player
        
        if self.check_rows_winning(board) or self.check_columns_winning(board) or self.check_diags_winning(board):
            self._utilities[board] = 1 if player == Player.MAX else -1
            return True

        if self.check_draw(board):
            self._utilities[board] = 0
            return True
        
        return False
        
    def _check_line_winning(self, line):
        if EMPTY_POSITION not in line:
            
            pieces = np.array([Piece.get_piece_by_id(p) for p in line]) #[piece_1, piece_2, piece_3, piece_4]
            prop = np.array([0, 0, 0, 0]) #round, big, light, hole
            
            

            for piece in pieces: 
                if piece.round_shape:
                    prop[0] += 1
                if piece.big_size:
                    prop[1] += 1
                if piece.light_color:
                    prop[2] += 1
                if piece.top_hole:
                    prop[3] += 1

            # either they all share the same property
            # or they dont share a single one 
            if 4 in prop or 0 in prop: #max(prop) == GRID_SIZE or max(prop) == 0: 
                return True
            else: 
                return False

        return False
    
    def check_draw(self, board):
        return not (board.grid == EMPTY_POSITION).any()

    def check_rows_winning(self, board):
        grid = board.grid
        for row in range(GRID_SIZE):
            if self._check_line_winning(grid[row]):
                return True

        return False

    def check_columns_winning(self, board):
        grid = board.grid
        for col in range(GRID_SIZE):
            if self._check_line_winning(grid[:,col]):
                return True

        return False

    def check_diags_winning(self, board):
        grid = board.grid
        if self._check_line_winning(grid.diagonal()) \
                or self._check_line_winning(np.fliplr(grid).diagonal()):
            return True

        return False

    