from game.piece import Piece

class Rook(Piece):
    white_str = "♖"
    black_str = "♜"
    def __init__(self, color, piece_type):
        super().__init__(color, piece_type)
#reminder super access












# from game.piece import Piece
# from game.function import MoveLogic

# class Rook(Piece):
#     def __str__(self):
#         self.has_moved = False #For castling future feature... maybe...
#         if self.__color__ == "WHITE":
#             return "♖"
#         else:
#             return "♜"
#     def get_moves_rook(self, board, row, col):
#         moves = []
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
#         for direction in directions:
#             r, c = row, col
#             while True:
#                 r += direction[0]
#                 c += direction[1]
#                 if 0 <= r < 8 and 0 <= c < 8:  # Checks limits of the board
#                     piece = board.get_piece(r, c)
#                     if piece is None:
#                         moves.append((r, c))  
#                     elif piece.get_color() != self.get_color():
#                         moves.append((r, c))  # != color, piece can be taken.
#                         break  
#                     else:
#                         break  # == color, stops the movement
#                 else:
#                     break  # Out of board limits.

#         return moves
    
#     def move(self, board, from_row, from_col, to_row, to_col):
#         MoveLogic.move(board, from_row, from_col, to_row, to_col, self)
