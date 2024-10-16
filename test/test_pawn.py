import unittest
from game.pawn import Pawn
from game.board import Board

class TestPawn(unittest.TestCase):
    def setUp(self):
        self.__board__ = Board()
        self.__pawn__ = Pawn("WHITE", "PAWN")

    def test_get_moves_pawn(self):
        self.__board__.set_piece(6,3, self.__pawn__)
        pawn = self.__board__.get_piece(6,3)
        self.assertEqual(pawn.get_moves_pawn(self.__board__, 6, 3), [(5,3),(4,3)])
    
    def test_get_moves_pawn_2(self):
        self.__board__.set_piece(2,4, self.__pawn__)
        pawn = self.__board__.get_piece(2,4)
        self.assertEqual(pawn.get_moves_pawn(self.__board__, 2, 4), [(1,3),(1,5)]) 

    def test_face_to_face(self):
        self.__board__.set_piece(3,3, self.__pawn__)
        self.__board__.set_piece(2,3, Pawn("BLACK", "PAWN"))
        pawn = self.__board__.get_piece(3,3)
        self.assertEqual(pawn.get_moves_pawn(self.__board__, 3, 3), [])

    def test_pawn_move(self):
        self.__board__.set_piece(6, 4, self.__pawn__)
        pawn = self.__board__.get_piece(6, 4)
        self.__pawn__.perform_movement(self.__board__, 6, 4, 4, 4)      
        self.assertEqual(self.__board__.get_piece(4, 4), pawn)      
        self.assertIsNone(self.__board__.get_piece(6, 4)) 

    def test_pawn_move_invalid(self):
        self.__board__.set_piece(6, 4, self.__pawn__)
        move = self.__pawn__.perform_movement(self.__board__, 6, 4, 7, 4)
        self.assertIsNone (move)

if __name__ == '__main__':
    unittest.main()