from game.piece import Piece
class Queen(Piece):
    white_str = "♕"
    black_str = "♛"
# from game.function import MoveLogic

# class Queen(Piece):
#     def __str__(self):
#         self.has_moved = False
#         if self.__color__ == "WHITE":
#             return "♕"
#         else:
#             return "♛"
        
#       #Queen combines bishop and rook movements, so the patterns can be re-utilized
#     def get_moves_queen(self, board, from_row, from_col):
#         move = []
#         directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] 
#         for direction in directions:
#             r, c = from_row, from_col
#             while True:
#                 r += direction[0]
#                 c += direction[1]
#                 if 0 <= r < 8 and 0 <= c < 8:  #Checks board limits
#                     piece = board.get_piece(r, c)
#                     if piece is None:
#                         move.append((r, c)) 
#                     elif piece.get_color() != self.get_color():
#                         move.append((r, c))  # != color, piece can be taken.
#                         break  
#                     else:
#                         break  
#                 else:
#                     break  
#         return move
#     def move(self, board, from_row, from_col, to_row, to_col):
#             MoveLogic.move(board, from_row, from_col, to_row, to_col, self)