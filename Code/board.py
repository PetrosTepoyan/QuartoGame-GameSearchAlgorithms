from tools import GRID_SIZE, PIECES_NUMBER, EMPTY_POSITION
from turn import Turn, TurnStage
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
        
        piece_to_place = self.game_turn.placingStage.piece
        current_player = self.get_player()
        next_player = current_player.toggle()
        all_pieces = set(range(1, 17))
        remaining_pieces = all_pieces - set(np.unique(self.grid)) - set([piece_to_place])

        # optimize with numpy as np.where
        if piece_to_place == 0:
            for remaining_piece in remaining_pieces:

                placingStage = None

                choosingStage = TurnStage(remaining_piece, None)

                turn = Turn(player = next_player, placingStage = placingStage, choosingStage = choosingStage)

                actions.add(turn)

        # optimize with numpy as np.where
        elif len(remaining_pieces) != 0:
            coords = np.where(self.grid == EMPTY_POSITION)
            for i in range(len(coords[0])):
                for remaining_piece in remaining_pieces:
                    piece_to_place_coord = (coords[1][i], coords[0][i])

                    placingStage = TurnStage(piece_to_place, piece_to_place_coord)

                    choosingStage = TurnStage(remaining_piece, None)

                    turn = Turn(player = next_player, placingStage = placingStage, choosingStage = choosingStage)

                    actions.add(turn)

        else:
            empty_pos_coord = np.where(self.grid == EMPTY_POSITION)

            row, col = empty_pos_coord[0][0], empty_pos_coord[1][0]

            piece_to_place_coord = (col, row)

            placingStage = TurnStage(piece_to_place, piece_to_place_coord)

            choosingStage = None

            turn = Turn(player = next_player, placingStage = placingStage, choosingStage = choosingStage)
            actions.add(turn)

        return actions

    def get_action_result(self, turn):

        new_grid = copy.deepcopy(self.grid)

        next_game_turn = Turn(player = turn.player, placingStage = turn.choosingStage, choosingStage = None)

        if turn.placingStage:
            piece_to_place = turn.placingStage.piece
            piece_to_place_coord = turn.placingStage.coord
            
            if piece_to_place_coord: ## not during the first iteration, when a player just gives a piece, without putting one
                col, row = piece_to_place_coord[0], piece_to_place_coord[1]
                new_grid[row, col] = piece_to_place
        
        new_board = Board(grid = new_grid, game_turn = next_game_turn)
        
        return new_board
        
    # Method that adds equatability
    def __eq__(self, other):
        return type(self) == type(other) and self.game_turn == other.game_turn and self.check_for_symmetry(withOther = other.grid)
    
    # Method that makes the object hashable
    # TODO: make hash faster 
    def __hash__(self):
        return sum([hash(j) for i in self.grid for j in i]) * hash(self.game_turn)

    def init_grid(self):
        return np.zeros((4,4)) + EMPTY_POSITION

    def check_position_availability(self, x, y):
        return self.grid[y, x] == EMPTY_POSITION

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
        legend_string = f"Piece to place {Piece.to_string(self.game_turn.placingStage.piece)}\n"  ##"Example, BS■ - Black Small Filled Square\n"
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

