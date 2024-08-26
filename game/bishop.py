from piece import Piece

class Bishop(Piece):
    def __str__(self):
        if self.__color__ == "WHITE":
            return "♗"
        else:
            return "♝"