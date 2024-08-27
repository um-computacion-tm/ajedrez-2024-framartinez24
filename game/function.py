class MoveLogic:
    @staticmethod
    def move(board, from_row, from_col, to_row, to_col, piece):
        board.set_piece(to_row, to_col, piece)
        board.remove_piece(from_row, from_col)
