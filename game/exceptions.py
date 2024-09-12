class InvalidMove(Exception):
    message = "Piece invalid move"
    def __str__(self):
        return self.message

class InvalidTurn(InvalidMove):
    message = "Can´t move another player piece"

class EmptyPosition(InvalidMove):
    message = "Empty position"

class OutOfBoard(InvalidMove):
    message = "Out of range"