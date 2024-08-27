from piece import Piece
from function import MoveLogic
class Horse(Piece):

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♘"
        else:
            return "♞"

    def get_moves_horse(self, board, from_row, from_col):
        moves = []
        #Remember the horse can "jump" on L
        directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

        for direction in directions:
            r, c = from_row + direction[0], from_col + direction[1]
            if 0 <= r < 8 and 0 <= c < 8:  # Checks board limits
                piece = board.get_piece(r, c)
                if piece is None:
                    moves.append((r, c)) 
                elif piece.get_color() != self.get_color():
                    moves.append((r, c))  # != color the piece can be taken

        return moves
#Same as rook, as pawn, as bishop
    # def move(self,board, from_row, from_col, to_row, to_col):
    #     board.set_piece(to_row, to_col, self)
    #     board.remove_piece(from_row, from_col)
    def move(self, board, from_row, from_col, to_row, to_col):
            MoveLogic.move(board, from_row, from_col, to_row, to_col, self)