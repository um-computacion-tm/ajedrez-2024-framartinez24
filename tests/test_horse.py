import unittest
from game.board import Board
from game.horse import Horse
from game.queen import Queen

class TestHorse(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__horse__ = Horse("WHITE", "HORSE")

    def test_move_horse(self):
        self.__board__.set_piece(3,5, self.__horse__)
        black_queen = Queen("BLACK", "QUEEN")
        self.__board__.set_piece(1,4, black_queen)
        self.__horse__.perform_movement(self.__board__, 3, 5, 1, 4)
        self.assertEqual(self.__board__.get_piece(1,4), self.__horse__)
        self.assertIsNone(self.__board__.get_piece(3,5))

if __name__ == '__main__':
    unittest.main()

