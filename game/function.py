class MoveLogic:
    @staticmethod
    def move(board, from_row, from_col, to_row, to_col, piece):
        board.set_piece(to_row, to_col, piece)
        board.remove_piece(from_row, from_col)

class MoveDirection:
       def direction(board, from_row, from_col, directions,moves):
              for direction in directions:
                     r, c = from_row + direction[0], from_col + direction[1]
              if 0 <= r < 8 and 0 <= c < 8:  # Checks board limits
                piece = board.get_piece(r, c)
              if piece is None:
                    moves.append((r, c))  
              elif piece.get_color() != self.get_color(): # != color, piece can be taken.
                    moves.append((r, c))           
              return moves
       
class Movement:
    def __init__(self, directions):
        self.directions = directions

    def get_moves(self, board, from_row, from_col, color):
        moves = []
        for direction in self.directions:
            r, c = from_row + direction[0], from_col + direction[1]
            if 0 <= r < 8 and 0 <= c < 8:  # Checks board limits
                piece = board.get_piece(r, c)
                if piece is None:
                    moves.append((r, c))
                elif piece.get_color() != color:  # Different color, piece can be taken.
                    moves.append((r, c))
        return moves
 
 