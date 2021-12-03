from tools import GRID_SIZE, PIECES_NUMBER, EMPTY_POSITION
from turn import Turn
from player import Player
from piece import Piece
import copy
from boardTerminalTest import BoardTerminalTest
import numpy as np

class State:
    def get_player(self):
        pass

    def get_applicable_actions(self):
        pass

    def get_action_result(self, action):
        pass
    
    # Method that adds equatability
    def __eq__(self, other):
        pass
    
    # Method that makes the object hashable
    def __hash__(self):
        pass

class Board(State):
    """Definition of all data of the game at an instant:
    - grid [2 dimension list]
    - game_turn [GameTurn]"""

    def __init__(self, grid = None, game_turn = None):
        self.boardTerminalTest = BoardTerminalTest()
        if grid is not None:
            self.grid = grid
        else:
            self.grid = self.init_grid()
            
        if game_turn:
            self.game_turn = game_turn
        else:
            self.game_turn = Turn(player = Player.MAX, piece_to_place = 0) ## choosing randomly for a player
        
        
    ## Implementation of State methods
    def get_player(self):
        return self.game_turn.player
    
    def get_applicable_actions(self):
        actions = set()
        
        piece_to_place = self.game_turn.piece_to_place
        current_player = self.get_player()
        next_player = current_player.toggle()
        all_pieces = set(range(1, 17))
        remaining_pieces = all_pieces - {elem for row in self.grid for elem in row} - set([piece_to_place])

        if piece_to_place == 0:
            for remaining_piece in remaining_pieces:
                turn = Turn(player = next_player,
                            piece_to_place = remaining_piece,
                            piece_coord = None,
                            prev_turn = self.game_turn)

                actions.add(turn)
                
        else :
            for row in range(GRID_SIZE):
                for col in range(GRID_SIZE):
                    if self.check_position_availability(col, row):
                        for remaining_piece in remaining_pieces:
                            piece_to_place_coord = (col, row)
                            turn = Turn(player = next_player,
                                        piece_to_place = remaining_piece,
                                        piece_coord = None,
                                        prev_turn = self.game_turn.with_piece_coord_set(piece_to_place_coord))

                            actions.add(turn)
                            
        return actions

    def get_action_result(self, turn):
        prev_turn = turn.prev_turn
        piece_coord = prev_turn.piece_coord
        
        new_game_turn = Turn(player = turn.player,
                             piece_to_place = turn.piece_to_place,
                             piece_coord = None,
                             prev_turn = turn)

        new_grid = copy.deepcopy(self.grid)
        
        if piece_coord: ## not during the first iteration, when a player just gives a piece, without putting one
            col, row = piece_coord[0], piece_coord[1]
            new_grid[row, col] = prev_turn.piece_to_place

        new_board = Board(grid = new_grid, game_turn = new_game_turn)
        
        return new_board
        
    # Method that adds equatability
    def __eq__(self, other):
        return type(self) == type(other) and self.game_turn == other.game_turn and self.check_for_symmetry(withOther = other.grid)
    
    # Method that makes the object hashable
    def __hash__(self):
        return sum([hash(j) for i in self.grid for j in i]) * hash(self.game_turn)

    def init_grid(self):
        return np.zeros((4,4)) + EMPTY_POSITION

    def check_position_availability(self, x, y):
        return self.grid[y, x] == EMPTY_POSITION

    def select_piece_for_opponent(self, piece_id):
        if not self.check_piece_availability(piece_id):
            return False
        self.game_turn.piece_to_place = piece_id
        return True

    def switch_player(self):
        self.game_turn.player_one_active = not self.game_turn.player_one_active
        if self.game_turn.player == Player.MAX:
            self.game_turn.player = Player.MIN
        else:
            self.game_turn.player = Player.MAX

    def check_winner(self):
        if self.check_raws_winning() or self.check_columns_winning() or self.check_diags_winning():
            if self.game_turn.player_one_active:
                player_name = "Player 1"
            else:
                player_name = "Player 2"
            self.message = player_name + " WINNNNS !!!!!!\n"
            return True
        return False

    def check_for_symmetry(self, withOther):
        for k in range(0, 4):
            rotated = np.rot90(self.grid, k = k)
            all_same_transposed = (withOther == rotated.T).all()
            all_same_rotated = (withOther == rotated).all()
            
            if all_same_transposed or all_same_rotated:
                return True
        
        return False

    def has_selected_piece(self):
        return self.game_turn.selected_piece > 0

    def __repr__(self):
        legend_string = f"Piece to place {Piece.to_string(self.game_turn.piece_to_place)}\n"  ##"Example, BS■ - Black Small Filled Square\n"
        display_string = '    A    B    C    D\n'
        for i, row in enumerate(self.grid, start = 1):
            display_string += ' '
            display_string += str(i)
            display_string += ' '
            for position in row:
                display_string += Piece.to_string(position)
                display_string += '  '
            display_string += '\n'
        return legend_string + display_string + '\n\n'

