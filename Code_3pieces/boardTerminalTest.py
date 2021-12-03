from tools import GRID_SIZE, PIECES_NUMBER, EMPTY_POSITION
from player import Player 
from piece import Piece

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
        
    def _check_line_winning(self, piece1, piece2, piece3):
        if EMPTY_POSITION not in (piece1, piece2, piece3):
            piece_1 = Piece.get_piece_by_id(piece1)
            piece_2 = Piece.get_piece_by_id(piece2)
            piece_3 = Piece.get_piece_by_id(piece3)
            pieces = [piece_1, piece_2, piece_3]
            prop = [0, 0, 0] #round, big, light, hole
            

            for piece in pieces: 
                if piece.round_shape:
                    prop[0] += 1
                if piece.big_size:
                    prop[1] += 1
                if piece.light_color:
                    prop[2] += 1

            # either they all share the same property
            # or they dont share a single one 
            if GRID_SIZE in prop or 0 in prop: #max(prop) == GRID_SIZE or max(prop) == 0: 
                return True
            else: 
                return False

        return False
    
    def check_draw(self, board):
        grid = board.grid
        for row in grid:
            for elem in row:
                if elem == EMPTY_POSITION:
                    return False

        return True

    def check_rows_winning(self, board):
        grid = board.grid
        for row in grid:
            if self._check_line_winning(row[0], row[1], row[2]):
                return True

        return False

    def check_columns_winning(self, board):
        grid = board.grid
        for i in range(3):
            if self._check_line_winning(grid[0][i], grid[1][i], grid[2][i]):
                return True
        return False

    def check_diags_winning(self, board):
        grid = board.grid
        if self._check_line_winning(grid[0][0], grid[1][1], grid[2][2]) \
                or self._check_line_winning(grid[0][2], grid[1][1], grid[2][0]):
            return True

        return False

    