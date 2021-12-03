import copy

class Piece:
    """Definition of a game piece by 4 characteristics:
    - RoundShape [True/False]
    - BigSize [True/False]
    - LightColor [True/False]
    - TopHole [True/False]"""

    def __init__(self,
                 id = 1,
                 round_shape = False,
                 big_size = False,
                 light_color = False,
                 top_hole = False):
        self.round_shape = round_shape
        self.big_size = big_size
        self.light_color = light_color
        self.top_hole = top_hole
        self.id = id
        
    @staticmethod
    def get_piece_by_id(id):
        if id != 0:
            return pieces_dict[id]
    
    def __hash__(self):
        return (4 * (self.round_shape + 1) + 3 * (self.big_size + 1) + 2 * self.light_color + self.top_hole)

    @staticmethod 
    def to_string(piece_id):

        if piece_id == 0:
            return "No piece to place"

        if piece_id == -1 :
            return " . "

        piece_display = str(piece_id)
        piece = Piece.get_piece_by_id(piece_id)
        if piece.round_shape:
            if piece.top_hole:
                piece_display = "○"
            else:
                piece_display = "●"
        else:
            if piece.top_hole:
                piece_display = "□"
            else:
                piece_display = "■"

        if piece.big_size:
            piece_display = "B" + piece_display
        else:
            piece_display = "S" + piece_display

        if piece.light_color:
            piece_display = "W" + piece_display
        else:
            piece_display = "B" + piece_display

        return piece_display
    
    def __repr__(self):
        return Piece.to_string(self.id)
            

pieces_list_definition = [
        Piece(1, False, False, False),
        Piece(2, True, False, False),
        Piece(3, False, True, False),
        Piece(4, True, True, False),
        Piece(5, False, False, True),
        Piece(6, True, False, True),
        Piece(7, False, True, True),
        Piece(8, True, True, True)
    ]

pieces_dict = {
    1 : Piece(1, False, False, False),
    2 : Piece(2, True, False, False),
    3 : Piece(3, False, True, False),
    4 : Piece(4, True, True, False),
    5 : Piece(5, False, False, True),
    6 : Piece(6, True, False, True),
    7 : Piece(7, False, True, True),
    8 : Piece(8, True, True, True)
}

