from piece import Piece

class Horse(Piece):

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♘"
        else:
            return "♞"

def valid_moves(self, board, current_row, current_col):
        moves = []
        # Horse move as "L"
        potential_moves = [
            (current_row - 2, current_col - 1), (current_row - 2, current_col + 1),
            (current_row + 2, current_col - 1), (current_row + 2, current_col + 1),
            (current_row - 1, current_col - 2), (current_row - 1, current_col + 2),
            (current_row + 1, current_col - 2), (current_row + 1, current_col + 2)
        ] #This patter forms an L movement for the horse piece.

        for new_row, new_col in potential_moves:
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                piece = board.get_piece(new_row, new_col)
                if piece is None or piece.color != self.color:
                    moves.append((new_row, new_col))  # Empty slot or enemy eateable 
        return moves

def move(self, board, current_row, current_col, new_row, new_col):
    # Checks valid movement 
    if (new_row, new_col) in self.valid_moves(board, current_row, current_col):
        board.set_piece(new_row, new_col, self)
        board.remove_piece(current_row, current_col)
    else:
        raise ValueError("Wrong or invalid movement")