from piece import Piece

class Rook(Piece):
    def __str__(self):
        self.has_moved = False #For castling future feature... maybe...
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"

def valid_moves(self, board, current_row, current_col):
        moves = []

        #Same as pawn, this determines the forward direction
        for direction in [-1, 1]: 
            for step in range(1, 8):
                new_row = current_row + direction * step
                if 0 <= new_row < 8:
                    piece = board.get_piece(new_row, current_col)
                    if piece is None:
                        #Empty, invalid move
                        moves.append((new_row, current_col))  
                        
                        #Check if there is an enemy piece to take.
                    elif piece.color != self.color:
                        moves.append((new_row, current_col))  
                        break  #Movement stops if there is a piece next to
                    else:
                        break  #Movements stops if there is a same color piece
                else:
                    break  # out of board limits, stop the movement. 

        # Horizontal movements (left & right)
        for direction in [-1, 1]:
            for step in range(1, 8):
                new_col = current_col + direction * step
                if 0 <= new_col < 8:
                    piece = board.get_piece(current_row, new_col)
                    if piece is None:
                        moves.append((current_row, new_col))  #Empty, invalid move
                    elif piece.color != self.color:
                        moves.append((current_row, new_col))  #Check if there is an enemy piece to take.
                        break  #Movement stops if there is a piece next to
                    else:
                        break  #Movements stops if there is a same color piece
                else:
                    break  # Again out of board limits

        return moves

def move(self, board, current_row, current_col, new_row, new_col):
        # verifies if the move is correct.
        if (new_row, new_col) in self.valid_moves(board, current_row, current_col):
            board.set_piece(new_row, new_col, self)
            board.remove_piece(current_row, current_col)
            self.has_moved = True
        else:
            raise ValueError("Wrong or invalid movement")
