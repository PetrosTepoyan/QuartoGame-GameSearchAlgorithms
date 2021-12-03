from player import Player
from piece import Piece
import copy

class Action:
    pass

class TurnStage:
    def __init__(self, piece, coord):
        self.piece = piece
        self.coord = coord

    def __hash__(self):
        return hash(self.piece + 1) + hash(self.coord)

    def __eq__(self, other):
        return type(self) == type(other) and self.piece == other.piece and self.coord == other.coord

class Turn(Action):
    """
    One turn is to put a piece on the board and pick a new one
    """

    def __init__(self, player = Player.MAX, placingStage = None, choosingStage = None):
        self.player = player
        if placingStage:
            self.placingStage = placingStage
        else:
            self.placingStage = TurnStage(0, None)

        if choosingStage:
            self.choosingStage = choosingStage
        else:
            self.choosingStage = TurnStage(0, None)
        
    def __hash__(self):
        return hash(self.player) + hash(self.placingStage) + hash(self.choosingStage)

    def __eq__(self, other):
        return (self.player == other.player and self.placingStage == other.placingStage and self.choosingStage == other.choosingStage)

    def __repr__(self):
        return f"Place {Piece.to_string(self.placingStage.piece)} to {self.placingStage.coord} and choose {Piece.to_string(self.choosingStage.piece)}"

# class Turn(Action):
#     """
#     One turn is to put a piece on the board and pick a new one
#     """

#     def __init__(self, player = Player.MAX, piece_to_place = 0, piece_coord = None, prev_turn = None):
#         self.player = player
#         self.piece_to_place = piece_to_place
#         self.piece_coord = piece_coord
#         self.prev_turn = prev_turn

#     def with_piece_coord_set(self, coord):
#         piece_copy = copy.deepcopy(self)
#         piece_copy.piece_coord = coord
#         return piece_copy

#     def set_coord(self, coord):
#         self.piece_coord = coord
        
#     def __hash__(self):
#         if self.prev_turn:
#             return hash(self.player) + (self.piece_to_place + 1) + hash(self.prev_turn.piece_coord)
#         else:
#             return hash(self.player) * (self.piece_to_place + 1) * hash(self.piece_coord)
        

#     def __eq__(self, other):
#         return (self.player == other.player and 
#         self.piece_to_place == other.piece_to_place and 
#         self.piece_coord == other.piece_coord and 
#         self.prev_turn.piece_coord == other.prev_turn.piece_coord)

#     def __repr__(self):
        
#         if self.prev_turn:
#             return f"Place {Piece.to_string(self.prev_turn.piece_to_place)} to {self.prev_turn.piece_coord} and choose {Piece.to_string(self.piece_to_place)}"
#         else:
#             # return f"Place {Piece.to_string(self.prev_turn.piece_to_place)} to {self.prev_turn.piece_coord} and choose {Piece.to_string(self.piece_to_place)}"
#             return f"Player: {self.player}, \nPiece to place: {Piece.to_string(self.piece_to_place)}, \nPiece coordinate: {self.piece_coord} \n\n"