from piece import Piece

class King(Piece):
    def __str__(self):
        #self.has_moved = False
        if self.__color__ == "WHITE":
            return "♔"
        else:
            return "♚"

#I'm not explaining this again, king can step wherever he wants to, he is the king.
def valid_moves(self, board, current_row, current_col):
        moves = []
        # Every direction for the KING
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for direction in directions:
            new_row = current_row + direction[0]
            new_col = current_col + direction[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                piece = board.get_piece(new_row, new_col)
                if piece is None:
                    moves.append((new_row, new_col))  
                elif piece.color != self.color:
                    moves.append((new_row, new_col))  
        return moves

def move(self, board, current_row, current_col, new_row, new_col):
    # Checks valid movement 
    if (new_row, new_col) in self.valid_moves(board, current_row, current_col):
        board.set_piece(new_row, new_col, self)
        board.remove_piece(current_row, current_col)
        self.has_moved = True
    else:
        raise ValueError("Wrong or invalid movement")