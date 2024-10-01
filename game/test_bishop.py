import unittest
from bishop import Bishop
from piece import Piece
from function import MoveLogic

class TestBishop(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)] 
        self.white_bishop = Bishop("WHITE")
        self.black_bishop = Bishop("BLACK")
        self.board[0][2] = self.white_bishop  
        self.board[7][5] = self.black_bishop  

    def test_bishop_str_white(self):
        self.assertEqual(str(self.white_bishop), "♗")

    def test_bishop_str_black(self):
        self.assertEqual(str(self.black_bishop), "♝")

    def test_bishop_get_moves_white(self):
        moves = self.white_bishop.get_moves_bishop(self.board, 0, 2)
        expected_moves = [(1, 1), (2, 0), (1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]  
        self.assertCountEqual(moves, expected_moves)

    def test_bishop_get_moves_black(self):
        moves = self.black_bishop.get_moves_bishop(self.board, 7, 5)
        expected_moves = [(6, 4), (5, 3), (4, 2), (3, 1), (2, 0), (6, 6), (5, 7)]  
        self.assertCountEqual(moves, expected_moves)

    def test_bishop_move_white_valid(self):
        from_row, from_col = 0, 2
        to_row, to_col = 3, 5
        self.white_bishop.move(self.board, from_row, from_col, to_row, to_col)
        self.assertIsNone(self.board[from_row][from_col])  
        self.assertEqual(self.board[to_row][to_col], self.white_bishop)  

    def test_bishop_move_black_valid(self):
        from_row, from_col = 7, 5
        to_row, to_col = 4, 2
        self.black_bishop.move(self.board, from_row, from_col, to_row, to_col)
        self.assertIsNone(self.board[from_row][from_col])  
        self.assertEqual(self.board[to_row][to_col], self.black_bishop)  

    def test_bishop_invalid_move(self):
        from_row, from_col = 0, 2
        to_row, to_col = 2, 2  
        with self.assertRaises(Exception): 
            self.white_bishop.move(self.board, from_row, from_col, to_row, to_col)

if __name__ == "__main__":
    unittest.main()
