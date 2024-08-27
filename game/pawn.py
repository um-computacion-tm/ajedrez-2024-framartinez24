from piece import Piece


class Pawn(Piece):

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♙"
        else:
            return "♟" #There isn´t an official black pawn.

    def get_moves_pawn(self, board, from_row, from_col):
        moves = []

        direction = -1 if self.__color__ == "WHITE" else 1 #determines forward movement depending on color
        r, c = from_row + direction, from_col  # Foward move 1 step (current_row)
        if 0 <= r < 8:  # Checking if the move is inside of the board limits & checking the col-row is empty or if there is a piece.
            if board.get_piece(r, c) is None: #If is None = move happend 
                moves.append((r, c))  

                #refactoriced has_moved
                start_row = 6 if self.__color__ == "WHITE" else 1 #This is for initial step, if the pawn hasn´t move, he can move 2 step foward.
                if from_row == start_row:
                    r_double = from_row + 2 * direction 
                    if board.get_piece(r_double, c) is None: #If is None = move happend 
                        moves.append((r_double, c))

        # # diagonal kill or "take"
        for dc in [-1, 1]:  # -1 left move, 1 right move
            r_diag, c_diag = from_row + direction, from_col + dc 
            if 0 <= r_diag < 8 and 0 <= c_diag < 8: #checking board limits again
                piece = board.get_piece(r_diag, c_diag)
                if piece is not None and piece.get_color() != self.get_color():
                    moves.append((r_diag, c_diag))  #getting the piece if there is one, diagonally to pawn.

        return moves

    ## Move pawn and update state and position...     
       #new row and new col is where the pawn is going to move if all the conditions of valid movements are true.
    def move(self, board, from_row, from_col, to_row, to_col):
       #Update where the pawn currently is.
        board.set_piece(to_row, to_col, self)
       #Removes the piece murdered by the pawn 
        board.remove_piece(from_row, from_col)

#exception gone