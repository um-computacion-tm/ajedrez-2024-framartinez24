from game.rook import Rook   
from game.horse import Horse
from game.bishop import Bishop
from game.queen import Queen
from game.king import King
from game.pawn import Pawn

#           Chess grid guide 
#
#      0  1  2 3  4  5 6 7
# 0    ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
# 1    ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
# 2    0  0  0  0 0  0  0 0
# 3    0  0  0  0 0  0  0 0
# 4    0  0  0  0 0  0  0 0
# 5    0  0  0  0 0  0  0 0
# 6    ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
# 7    ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖

class Board:
    def __init__(self, test=False):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        if not test:
            self.__positions__[0][0] = Rook("BLACK")
            self.__positions__[7][7] = Rook("WHITE")
            self.__positions__[0][7] = Rook("BLACK") 
            self.__positions__[7][0] = Rook("WHITE")
            self.__positions__[0][1] = Horse("BLACK")
            self.__positions__[0][6] = Horse("BLACK")
            self.__positions__[7][1] = Horse("WHITE")
            self.__positions__[7][6] = Horse("WHITE")
            self.__positions__[0][2] = Bishop("BLACK")
            self.__positions__[0][5] = Bishop("BLACK")
            self.__positions__[7][2] = Bishop("WHITE")
            self.__positions__[7][5] = Bishop("WHITE")
            self.__positions__[0][3] = Queen("BLACK")
            self.__positions__[7][3] = Queen("WHITE")
            self.__positions__[0][4] = King("BLACK")
            self.__positions__[7][4] = King("WHITE")
            for i in range(8):
                self.__positions__[1][i] = Pawn("BLACK")
                self.__positions__[6][i] = Pawn("WHITE")

    def __str__(self):
        board_str = "  0 1 2 3 4 5 6 7\n"  
        for i, row in enumerate(self.__positions__):
            board_str += str(i) + " "  
            for cell in row:
                if cell is not None:
                    board_str += str(cell) + " " # If a piece exists, it converts the piece object to a string
                else:
                    board_str += " "  
            board_str += str(i) + "\n" 
        board_str += "  0 1 2 3 4 5 6 7\n"
        return board_str
    
    def get_size(self): # get_size(): Returns the size of the chessboard (8x8).
        return len(self.__positions__)

    def get_piece(self, row, col): # get_piece(row, col): Returns the piece at the specified row and column.
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece): # set_piece(row, col, piece): Sets the piece at the specified row and column.
        self.__positions__[row][col] = piece

    def remove_piece(self, row, col): # remove_piece(row, col): Removes the piece at the specified row and column.
        self.__positions__[row][col] = None
    
    def perfom_move(self, from_row, from_col, to_row, to_col):
        piece = self.get_piece(from_row, from_col)
        if piece is None:
            raise ValueError("Missing piece")
        piece_kind = piece.__class__.__name__.upper() 
        if isinstance(piece, Pawn):  
            moved_piece = piece.pawn_move(self, from_row, from_col, to_row, to_col)
        else:
            moved_piece = piece.move_piece(self, from_row, from_col, to_row, to_col)
        if moved_piece is None:
            raise ValueError(f"Invalid movement for: {piece_kind }")
        return moved_piece