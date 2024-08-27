from piece import Piece

class Bishop(Piece):
    def __str__(self):
        self.has_moved = False
        if self.__color__ == "WHITE":
            return "♗"
        else:
            return "♝"
    
    def get_moves_bishop(self, board, from_row, from_col):
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] 

        for direction in directions:
            r, c = from_row, from_col
            while True:
                r += direction[0]
                c += direction[1]
                if 0 <= r < 8 and 0 <= c < 8:  #Check board limits
                    piece = board.get_piece(r, c)
                    if piece is None:
                        moves.append((r, c))  
                    elif piece.get_color() != self.get_color():
                        moves.append((r, c))  # != color the piece can be taken
                        break  
                    else:
                        break  # == color stops the movements
                else:
                    break  # Out of the board limits
        return moves


#Same as pawn as rook... 
    def move(self, board, from_row, from_col, to_row, to_col):
        board.set_piece(to_row, to_col, self)
        board.remove_piece(from_row, from_col)
    
    
    
    
    
    
    
    # def valid_moves(self, board, current_row, current_col):
    #     moves = []

    #     # Diagonal movements
    #     directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Up-left, up-right, down-left, down-right

    #     for direction in directions:
    #         row_direction, col_direction = direction
    #         for step in range(1, 8):
    #             new_row = current_row + row_direction * step
    #             new_col = current_col + col_direction * step
    #             if 0 <= new_row < 8 and 0 <= new_col < 8:
    #                 piece = board.get_piece(new_row, new_col)
    #                 if piece is None:
    #                     #Empty, invalid move
    #                     moves.append((new_row, new_col))   
    #                 elif piece.color != self.color:
    #                     moves.append((new_row, new_col))  #Check if there is an enemy piece to take.
    #                     break  #Movement stops if there is a piece next to
    #                 else:
    #                     break  #Movements stops if there is a same color piece
    #             else:
    #                 break  # out of board limits, stop the movement. 

    #     return moves

    # def move(self, board, current_row, current_col, new_row, new_col):
    #     # verifies if the move is correct.
    #     if (new_row, new_col) in self.valid_moves(board, current_row, current_col):
    #         board.set_piece(new_row, new_col, self)
    #         board.remove_piece(current_row, current_col)
    #         self.has_moved = True
    #     else:
    #         raise ValueError("Wrong or invalid movement")