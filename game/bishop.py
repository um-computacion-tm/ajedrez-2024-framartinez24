from piece import Piece
from function import MoveLogic

class Bishop(Piece):
    def __str__(self):
        self.has_moved = False
        if self.__color__ == "WHITE":
            return "♗"
        else:
            return "♝"
    
    def get_moves_bishop(self, board, from_row, from_col):
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] 

        for direction in directions:
            r, c = from_row, from_col
            while True:
                r += direction[0]
                c += direction[1]
                if 0 <= r < 8 and 0 <= c < 8:  #Check board limits
                    piece = board.get_piece(r, c)
                    if piece is None:
                        moves.append((r, c))  
                    elif piece.get_color() != self.get_color():
                        moves.append((r, c))  # != color the piece can be taken
                        break  
                    else:
                        break  # == color stops the movements
                else:
                    break  # Out of the board limits
        return moves

    def move(self, board, from_row, from_col, to_row, to_col):
            MoveLogic.move(board, from_row, from_col, to_row, to_col, self)