import unittest
from horse import Horse
from piece import Piece
from function import MoveLogic, Movement

class TestHorse(unittest.TestCase):

    def setUp(self):
        self.board = [[None for _ in range(8)] for _ in range(8)] 
        self.white_horse = Horse("WHITE")
        self.black_horse = Horse("BLACK")
        self.board[0][1] = self.white_horse  
        self.board[7][6] = self.black_horse  

    def test_horse_str_white(self):
        self.assertEqual(str(self.white_horse), "♘")

    def test_horse_str_black(self):
        self.assertEqual(str(self.black_horse), "♞")

    def test_horse_get_moves_white(self):
        moves = self.white_horse.get_moves(self.board, 0, 1)
        expected_moves = [(2, 0), (2, 2)]  
        self.assertCountEqual(moves, expected_moves)

    def test_horse_get_moves_black(self):
        moves = self.black_horse.get_moves(self.board, 7, 6)
        expected_moves = [(5, 5), (5, 7)] 
        self.assertCountEqual(moves, expected_moves)

    def test_horse_move_white_valid(self):
        from_row, from_col = 0, 1
        to_row, to_col = 2, 0
        self.white_horse.move(self.board, from_row, from_col, to_row, to_col)
        self.assertIsNone(self.board[from_row][from_col])  
        self.assertEqual(self.board[to_row][to_col], self.white_horse)  

    def test_horse_move_black_valid(self):
        from_row, from_col = 7, 6
        to_row, to_col = 5, 5
        self.black_horse.move(self.board, from_row, from_col, to_row, to_col)
        self.assertIsNone(self.board[from_row][from_col])  
        self.assertEqual(self.board[to_row][to_col], self.black_horse)  

    def test_horse_invalid_move(self):
        from_row, from_col = 0, 1
        to_row, to_col = 1, 1  
        with self.assertRaises(Exception):  
            self.white_horse.move(self.board, from_row, from_col, to_row, to_col)

if __name__ == "__main__":
    unittest.main()
