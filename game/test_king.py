import unittest
from king import King
from piece import Piece
from function import MoveLogic, Movement

class TestKing(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)] 
        self.white_king = King("WHITE")
        self.black_king = King("BLACK")
        self.board[0][4] = self.white_king  
        self.board[7][4] = self.black_king  

    def test_king_str_white(self):
        self.assertEqual(str(self.white_king), "♔")

    def test_king_str_black(self):
        self.assertEqual(str(self.black_king), "♚")

    def test_king_get_moves_white(self):
        moves = self.white_king.get_moves(self.board, 0, 4)
        expected_moves = [(0, 3), (0, 5), (1, 3), (1, 4), (1, 5)]  
        self.assertCountEqual(moves, expected_moves)

    def test_king_get_moves_black(self):
        moves = self.black_king.get_moves(self.board, 7, 4)
        expected_moves = [(6, 3), (6, 4), (6, 5), (7, 3), (7, 5)] 
        self.assertCountEqual(moves, expected_moves)

    def test_king_move_white_valid(self):
        from_row, from_col = 0, 4
        to_row, to_col = 1, 4
        self.white_king.move(self.board, from_row, from_col, to_row, to_col)
        self.assertIsNone(self.board[from_row][from_col]) 
        self.assertEqual(self.board[to_row][to_col], self.white_king) 

    def test_king_move_black_valid(self):
        from_row, from_col = 7, 4
        to_row, to_col = 6, 4
        self.black_king.move(self.board, from_row, from_col, to_row, to_col)
        self.assertIsNone(self.board[from_row][from_col])  
        self.assertEqual(self.board[to_row][to_col], self.black_king) 

    def test_king_invalid_move(self):
        from_row, from_col = 0, 4
        to_row, to_col = 2, 4  
        with self.assertRaises(Exception):  
            self.white_king.move(self.board, from_row, from_col, to_row, to_col)

if __name__ == "__main__":
    unittest.main()
