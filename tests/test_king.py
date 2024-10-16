import unittest
from game.board import Board
from game.king import King
from game.pawn import Pawn

class TestKing(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__king__ = King("WHITE", "KING")

    def test_str_king(self):
        self.assertEqual(str(self.__king__), "♔")  
        
if __name__ == '__main__':
    unittest.main()
