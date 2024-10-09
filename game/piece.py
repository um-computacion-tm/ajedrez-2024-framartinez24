class Piece:
    def __init__(self, color, piece_type):
        self.__color__ = color
        self.__piece__type = piece_type

    def get_color(self):
        return self.__color__
    
    def get_directions(self):
        directions = {
            "QUEEN": [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)],
            "HORSE": [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)],
            "KING": [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)],
            "BISHOP": [(-1, -1), (-1, 1), (1, -1), (1, 1)],
            "ROOK": [(-1, 0), (1, 0), (0, -1), (0, 1)],
        }
        return directions.get(self.__piece_type__.upper(), [])
    
    def get_valid_moves(self, board, from_row, from_col):
        directions = self.get_directions()
        if self.__piece_type__.upper() in ["ROOK", "BISHOP", "QUEEN"]:
            return self.get_pieces_moves_rqb(board, from_row, from_col, directions)
        else:
            return self.get_moves_kh(board, from_row, from_col, directions)

    def move_piece(self, board, from_row, from_col, to_row, to_col):
        return self.perform_movement(board, from_row, from_col, to_row, to_col)
    
    def get_pieces_moves_rqb(self, board, from_row, from_col, directions):
        moves = []
        for direction in directions:
            r, c = from_row, from_col
            while True:
                r += direction[0]
                c += direction[1]
                if 0 <= r < 8 and 0 <= c < 8:
                    piece = board.get_piece(r, c)
                    if piece is None:
                        moves.append((r, c))
                    elif piece.get_color() != self.get_color():
                        moves.append((r, c))
                        break
                    else:
                        break
                else:
                    break
        return moves

    def get_moves_kh(self, board, from_row, from_col, directions):
        moves = []
        for direction in directions:
            r, c = from_row + direction[0], from_col + direction[1]
            if 0 <= r < 8 and 0 <= c < 8:
                piece = board.get_piece(r, c)
                if piece is None:
                    moves.append((r, c))
                elif piece.get_color() != self.get_color():
                    moves.append((r, c))
        return moves
    
    def perform_movement(self, board, from_row, from_col, to_row, to_col, ):
        valid_moves = self.get_valid_moves(board, from_row, from_col)
        if (to_row, to_col) in valid_moves:
            board.set_piece(to_row, to_col, self)
            board.remove_piece(from_row, from_col)
            return self
        else:
            return None