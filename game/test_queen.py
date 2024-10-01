import unittest
from queen import Queen
from piece import Piece
from function import MoveLogic

class TestQueen(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]  
        self.white_queen = Queen("WHITE")
        self.black_queen = Queen("BLACK")
        self.board[0][3] = self.white_queen  
        self.board[7][3] = self.black_queen  

    def test_queen_str_white(self):
        self.assertEqual(str(self.white_queen), "♕")

    def test_queen_str_black(self):
        self.assertEqual(str(self.black_queen), "♛")

    def test_queen_get_moves_white(self):
        moves = self.white_queen.get_moves_queen(self.board, 0, 3)
        expected_moves = [
            (1, 2), (2, 1), (3, 0), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), 
            (1, 4), (2, 5), (3, 6), (4, 7), (0, 2), (0, 1), (0, 0), (0, 4), (0, 5), (0, 6), (0, 7)
        ] 
        self.assertCountEqual(moves, expected_moves)

    def test_queen_get_moves_black(self):
        moves = self.black_queen.get_moves_queen(self.board, 7, 3)
        expected_moves = [
            (6, 2), (5, 1), (4, 0), (6, 3), (5, 3), (4, 3), (3, 3), (2, 3), (1, 3), (0, 3), 
            (6, 4), (5, 5), (4, 6), (3, 7), (7, 2), (7, 1), (7, 0), (7, 4), (7, 5), (7, 6), (7, 7)
        ] 
        self.assertCountEqual(moves, expected_moves)

    def test_queen_move_white_valid(self):
        from_row, from_col = 0, 3
        to_row, to_col = 3, 3  
        self.white_queen.move(self.board, from_row, from_col, to_row, to_col)
        self.assertIsNone(self.board[from_row][from_col])  
        self.assertEqual(self.board[to_row][to_col], self.white_queen)  

    def test_queen_move_black_valid(self):
        from_row, from_col = 7, 3
        to_row, to_col = 4, 6  
        self.black_queen.move(self.board, from_row, from_col, to_row, to_col)
        self.assertIsNone(self.board[from_row][from_col])  
        self.assertEqual(self.board[to_row][to_col], self.black_queen)  
    def test_queen_invalid_move(self):
        from_row, from_col = 0, 3
        to_row, to_col = 2, 4  
        with self.assertRaises(Exception): 
            self.white_queen.move(self.board, from_row, from_col, to_row, to_col)

if __name__ == "__main__":
    unittest.main()
