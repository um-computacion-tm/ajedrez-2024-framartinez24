from piece import Piece

class Queen(Piece):
    def __str__(self):
        self.has_moved = False
        if self.__color__ == "WHITE":
            return "♕"
        else:
            return "♛"
        
    #Queen combines bishop and rook movements, so the patterns can be re-utilized
def valid_moves(self, board, current_row, current_col):
    moves = []
    # diagonal movements as bishop
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # up-left, up-right, down-left, down right
    for direction in directions:
        row_direction, col_direction = direction
        for step in range(1, 8):
            new_row = current_row + row_direction * step
            new_col = current_col + col_direction * step
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                piece = board.get_piece(new_row, new_col)
                if piece is None:
                    moves.append((new_row, new_col))
                elif piece.color != self.color:
                    moves.append((new_row, new_col))
                    break  # Enemy spotted, stop the movemvnts
                else:
                    break  # Same color piece, stop.
            else:
                break
    # Straight movements as rook...
    straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    for direction in straight_directions:
        row_direction, col_direction = direction
        for step in range(1, 8):
            new_row = current_row + row_direction * step
            new_col = current_col + col_direction * step
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                piece = board.get_piece(new_row, new_col)
                if piece is None:
                    moves.append((new_row, new_col))  # Enemy spotted, stop the movemvnts
                elif piece.color != self.color:
                    moves.append((new_row, new_col)) # Same color piece, stop.
                    break
                else:
                    break
            else:
                break
    return moves
def move(self, board, current_row, current_col, new_row, new_col):
    # checks valid movements
    if (new_row, new_col) in self.valid_moves(board, current_row, current_col):
        board.set_piece(new_row, new_col, self)
        board.remove_piece(current_row, current_col)
        self.has_moved = True
    else:
        raise ValueError("Wrong or invalid movement")
    
    
    
    
    
    
    
    
    #dono-why this makes me think a lot... 