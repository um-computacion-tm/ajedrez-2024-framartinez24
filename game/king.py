from game.piece import Piece
from game.function import MoveLogic, Movement

class King(Piece):
    def __str__(self):
        #self.has_moved = False
        self.movement = Movement([(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)])
        if self.__color__ == "WHITE":
            return "♔"
        else:
            return "♚"
        
    def get_moves(self, board, from_row, from_col):
        return self.movement.get_moves(board, from_row, from_col, self.get_color())
    
    def move(self, board, from_row, from_col, to_row, to_col):
            MoveLogic.move(board, from_row, from_col, to_row, to_col, self)









#I'm not explaining this again, king can step wherever he wants to, he is the king.

    # def get_moves_king(self, board, from_row, from_col):
    #     moves = []
    #     directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    #     for direction in directions:
    #         r, c = from_row + direction[0], from_col + direction[1]
    #         if 0 <= r < 8 and 0 <= c < 8:  # Checks board limits
    #             piece = board.get_piece(r, c)
    #             if piece is None:
    #                 moves.append((r, c))  
    #             elif piece.get_color() != self.get_color(): # != color, piece can be taken.
    #                 moves.append((r, c))           
    #         return moves
        
        
    #bla bla same as always
    # def move(self,board, from_row, from_col, to_row, to_col):
    #     board.set_piece(to_row, to_col, self)
    #     board.remove_piece(from_row, from_col)
