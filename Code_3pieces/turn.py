from player import Player
from piece import Piece
import copy

class Action:
    pass

# Instead of dealing with messy initializers for Turn, that is more reasonable to create two stages of a turn:
# a stage where we place a piece, if there is one; and a stage where we choose a piece.
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