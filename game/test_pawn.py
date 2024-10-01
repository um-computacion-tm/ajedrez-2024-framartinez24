import unittest
from pawn import Pawn
from piece import Piece
from function import MoveLogic

class TestPawn(unittest.TestCase):

    def setUp(self):
        
        self.board = [[None for _ in range(8)] for _ in range(8)] 
        self.white_pawn = Pawn("WHITE")
        self.black_pawn = Pawn("BLACK")
        self.board[6][0] = self.white_pawn  
        self.board[1][0] = self.black_pawn  

    def test_pawn_str_white(self):  
        self.assertEqual(str(self.white_pawn), "♙")

    def test_pawn_str_black(self):
        self.assertEqual(str(self.black_pawn), "♟")

    def test_pawn_move_white_valid(self):
        from_row, from_col = 6, 0
        to_row, to_col = 5, 0
        self.white_pawn.move(self.board, from_row, from_col, to_row, to_col)
        self.assertIsNone(self.board[from_row][from_col]) 
        self.assertEqual(self.board[to_row][to_col], self.white_pawn)  

    def test_pawn_move_black_valid(self):
        from_row, from_col = 1, 0
        to_row, to_col = 2, 0
        self.black_pawn.move(self.board, from_row, from_col, to_row, to_col)
        self.assertIsNone(self.board[from_row][from_col])  
        self.assertEqual(self.board[to_row][to_col], self.black_pawn)  

    def test_pawn_invalid_move(self):
        from_row, from_col = 6, 0
        to_row, to_col = 4, 1  
        with self.assertRaises(Exception):  
            self.white_pawn.move(self.board, from_row, from_col, to_row, to_col)

if __name__ == "__main__":
    unittest.main()