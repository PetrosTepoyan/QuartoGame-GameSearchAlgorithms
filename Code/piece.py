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
        Piece(1, False, False, False, False),
        Piece(2, True, False, False, False),
        Piece(3, False, True, False, False),
        Piece(4, True, True, False, False),
        Piece(5, False, False, True, False),
        Piece(6, True, False, True, False),
        Piece(7, False, True, True, False),
        Piece(8, True, True, True, False),
        Piece(9, False, False, False, True),
        Piece(10, True, False, False, True),
        Piece(11, False, True, False, True),
        Piece(12, True, True, False, True),
        Piece(13, False, False, True, True),
        Piece(14, True, False, True, True),
        Piece(15, False, True, True, True),
        Piece(16, True, True, True, True)
    ]

pieces_dict = {
    1 : Piece(1, False, False, False, False),
    2 : Piece(2, True, False, False, False),
    3 : Piece(3, False, True, False, False),
    4 : Piece(4, True, True, False, False),
    5 : Piece(5, False, False, True, False),
    6 : Piece(6, True, False, True, False),
    7 : Piece(7, False, True, True, False),
    8 : Piece(8, True, True, True, False),
    9 : Piece(9, False, False, False, True),
    10: Piece(10, True, False, False, True),
    11: Piece(11, False, True, False, True),
    12: Piece(12, True, True, False, True),
    13: Piece(13, False, False, True, True),
    14: Piece(14, True, False, True, True),
    15: Piece(15, False, True, True, True),
    16: Piece(16, True, True, True, True)
}

str_to_pieceid = {
 'BS■': 1,
 'BS●': 2,
 'BB■': 3,
 'BB●': 4,
 'WS■': 5,
 'WS●': 6,
 'WB■': 7,
 'WB●': 8,
 'BS□': 9,
 'BS○': 10,
 'BB□': 11,
 'BB○': 12,
 'WS□': 13,
 'WS○': 14,
 'WB□': 15,
 'WB○': 16
 }

