from piece import Piece

class Pawn(Piece):
    def __str__(self):
        self.has_moved = False
        if self.__color__ == "WHITE":
            return "♙"
        else:
            return "♟️" #There isn´t an official black pawn.

    def valid_moves(self, board, current_row, current_col):
        direction = -1 if self.color == "WHITE" else 1 #determines forward movement depending on color
        moves = []

       #Foward movement and direction (if goes down or up depending on color)
        forward_row = current_row + direction  # Foward move 1 step (current_row)
        
        # Checking if the move is inside of the board limits & checking the col-row is empty or if there is a piece.
        if 0 <= forward_row < 8 and board.get_piece(forward_row, current_col) is None:
            moves.append((forward_row, current_col))
            #If is None = move happend 
        
        
        if not self.has_moved: #This is for initial step, if the pawn hasn´t move, he can move 2 step foward.
            two_step_row = current_row + (2 * direction) #this part is as the code of foward_row but *2
            if 0 <= two_step_row < 8 and board.get_piece(forward_row, current_col) is None and board.get_piece(two_step_row, current_col) is None:
                moves.append((two_step_row, current_col))
        
        
        ## diagonal kill or "take"
        for col_offset in [-1, 1]:  # -1 left move, 1 right move
            diag_col = current_col + col_offset #This "calculates" where can the pawn move diagonally 
            if 0 <= diag_col < 8: #checking board limits again
                
                #getting the piece if there is one, diagonally to pawn.
                diag_piece = board.get_piece(forward_row, diag_col)
                
                if diag_piece is not None and diag_piece.color != self.color: #check if is not None & the color of the piece is not as the self pawn, if this 2 condition are true, he can kill the other piece.
                    moves.append((forward_row, diag_col))
        return moves
    
    
       ## Move pawn and update state and position...     
       #new row and new col is where the pawn is going to move if all the conditions of valid movements are true.   
    def move(self, board, current_row, current_col, new_row, new_col):
        
        if (new_row, new_col) in self.valid_moves(board, current_row, current_col):
            #Update where the pawn currently is.
            board.set_piece(new_row, new_col, self)
            #Removes the piece murdered by the pawn 
            board.remove_piece(current_row, current_col)
            #Changes the state of has_moved, so I'll never move 2 step in once again... saddly :( 
            self.has_moved = True
            
        else:
            raise ValueError("Wrong or invalid movement")
