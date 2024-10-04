from game.piece import Piece
from game.function import MoveLogic

class Pawn(Piece):

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♙"
        else:
            return "♟" #There isn´t an official black pawn.
    def move(self, board, from_row, from_col, to_row, to_col):
        MoveLogic.move(board, from_row, from_col, to_row, to_col, self)
