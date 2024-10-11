from game.piece import Piece
# from game.function import MoveLogic

class Pawn(Piece):
    white_str = "♙"
    black_str = "♟"

    def pawn_movements(self, board, from_row, from_col, direction): 
        moves = []
        r, c = from_row + direction, from_col
        if 0 <= r < 8 and board.get_piece(r, c) is None:
            moves.append((r, c))
            start_row = 6 if self.get_color() == "WHITE" else 1
            if from_row == start_row:
                r_double = from_row + 2 * direction
                if board.get_piece(r_double, c) is None:
                    moves.append((r_double, c))
        return moves

    def diagonally_take(self, board, from_row, from_col, direction):
        moves = []
        for dc in [-1, 1]:
            r_diag, c_diag = from_row + direction, from_col + dc
            if 0 <= r_diag < 8 and 0 <= c_diag < 8:
                piece = board.get_piece(r_diag, c_diag)
                if piece is not None and piece.get_color() != self.get_color():
                    moves.append((r_diag, c_diag))
        return moves

    def move_pawn(self, board, from_row, from_col):
        moves = []
        direction = -1 if self.get_color() == "WHITE" else 1
        moves.extend(self.pawn_movements(board, from_row, from_col, direction))
        moves.extend(self.diagonally_take(board, from_row, from_col, direction))
        return moves
    
    def get_valid_moves(self, board, from_row, from_col):
        return self.move_pawn(board, from_row, from_col)

    def pawn_perfom_move(self, board, from_row, from_col, to_row, to_col):
        return self.perform_movement(board, from_row, from_col, to_row, to_col)
