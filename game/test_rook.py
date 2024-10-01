import unittest
from piece import Piece
from rook import Rook
from function import MoveLogic

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)] 
        self.white_rook = Rook("WHITE")
        self.black_rook = Rook("BLACK")
        self.board[0][0] = self.white_rook 
        self.board[7][7] = self.black_rook  

    def test_rook_str_white(self):
        self.assertEqual(str(self.white_rook), "♖")

    def test_rook_str_black(self):
        self.assertEqual(str(self.black_rook), "♜")

    def test_rook_get_moves_white(self):
        moves = self.white_rook.get_moves_rook(self.board, 0, 0)
        expected_moves = [(i, 0) for i in range(1, 8)] + [(0, i) for i in range(1, 8)] 
        self.assertCountEqual(moves, expected_moves)

    def test_rook_get_moves_black(self):
        moves = self.black_rook.get_moves_rook(self.board, 7, 7)
        expected_moves = [(i, 7) for i in range(0, 7)] + [(7, i) for i in range(0, 7)]  
        self.assertCountEqual(moves, expected_moves)

    def test_rook_move_white_valid(self):
        from_row, from_col = 0, 0
        to_row, to_col = 0, 4
        self.white_rook.move(self.board, from_row, from_col, to_row, to_col)
        self.assertIsNone(self.board[from_row][from_col])  
        self.assertEqual(self.board[to_row][to_col], self.white_rook)  

    def test_rook_move_black_valid(self):
        from_row, from_col = 7, 7
        to_row, to_col = 7, 3
        self.black_rook.move(self.board, from_row, from_col, to_row, to_col)
        self.assertIsNone(self.board[from_row][from_col]) 
        self.assertEqual(self.board[to_row][to_col], self.black_rook)  

    def test_rook_invalid_move(self):
        from_row, from_col = 0, 0
        to_row, to_col = 3, 3  
        with self.assertRaises(Exception):  
            self.white_rook.move(self.board, from_row, from_col, to_row, to_col)

if __name__ == "__main__":
    unittest.main()