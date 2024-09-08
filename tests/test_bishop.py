import unittest
from game.bishop import Bishop
from game.piece import Piece
from game.function import MoveLogic

class TestBishop(unittest.TestCase):

    def setUp(self):
        """Configuración para los tests"""
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
        expected_moves = [(6, 
