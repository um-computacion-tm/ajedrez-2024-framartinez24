from piece import Piece
from function import MoveLogic

class Pawn(Piece):

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♙"
        else:
            return "♟" #There isn´t an official black pawn.

    ## Move pawn and update state and position...     
       #new row and new col is where the pawn is going to move if all the conditions of valid movements are true.
    def move(self, board, from_row, from_col, to_row, to_col):
        MoveLogic.move(board, from_row, from_col, to_row, to_col, self)
    #Testing def as class.