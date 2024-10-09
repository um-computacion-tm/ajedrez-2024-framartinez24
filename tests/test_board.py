# import unittest
# from game.board import Board
# from game.rook import Rook
# from game.horse import Horse
# from game.bishop import Bishop
# from game.queen import Queen
# from game.king import King
# from game.pawn import Pawn

# class TestBoard(unittest.TestCase):
#     def setUp(self):
#         self.board = Board()

#     def test_initial_setup(self):
#         self.assertIsInstance(self.board.get_piece(0, 0), Rook)
#         self.assertIsInstance(self.board.get_piece(0, 7), Rook)
#         self.assertIsInstance(self.board.get_piece(7, 0), Rook)
#         self.assertIsInstance(self.board.get_piece(7, 7), Rook)


#         self.assertIsInstance(self.board.get_piece(0, 1), Horse)
#         self.assertIsInstance(self.board.get_piece(0, 6), Horse)
#         self.assertIsInstance(self.board.get_piece(7, 1), Horse)
#         self.assertIsInstance(self.board.get_piece(7, 6), Horse)


#         self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
#         self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
#         self.assertIsInstance(self.board.get_piece(7, 2), Bishop)
#         self.assertIsInstance(self.board.get_piece(7, 5), Bishop)


#         self.assertIsInstance(self.board.get_piece(0, 3), Queen)
#         self.assertIsInstance(self.board.get_piece(7, 3), Queen)

#         self.assertIsInstance(self.board.get_piece(0, 4), King)
#         self.assertIsInstance(self.board.get_piece(7, 4), King)

#         for i in range(8):
#             self.assertIsInstance(self.board.get_piece(1, i), Pawn)
#             self.assertIsInstance(self.board.get_piece(6, i), Pawn)

#     def test_empty_squares(self):
#         for i in range(2, 6):
#             for j in range(8):
#                 self.assertIsNone(self.board.get_piece(i, j))

#     def test_initial_positions(self):
#         expected_positions = [
#             ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],  
#             ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],  
#             [None, None, None, None, None, None, None, None],
#             [None, None, None, None, None, None, None, None],
#             [None, None, None, None, None, None, None, None],
#             [None, None, None, None, None, None, None, None],
#             ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],  
#             ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"]   
#         ]

#         actual_positions = []
#         for row in range(8):
#             actual_row = []
#             for col in range(8):
#                 piece = self.board.get_piece(row, col)
#                 actual_row.append(str(piece) if piece else None)
#             actual_positions.append(actual_row)
       
#         self.assertEqual(actual_positions, expected_positions)
        
#     def test_str_representation(self):
#         expected_str = (
#             "♜♞♝♛♚♝♞♜\n"
#             "♟♟♟♟♟♟♟♟\n"
#             "        \n"
#             "        \n"
#             "        \n"
#             "        \n"
#             "♙♙♙♙♙♙♙♙\n"
#             "♖♘♗♕♔♗♘♖\n"
#         )
#         self.assertEqual(str(self.board), expected_str)

#     def test_size(self):
#         cantidadcasillas = 8
#         self.assertEqual(self.board.get_size(), cantidadcasillas)

#     def test_move_knight(self):
#         moved_piece = self.board.ejecutar_move(7, 1, 5, 2)
#         self.assertIsInstance(moved_piece, Horse)
#         self.assertEqual(self.board.get_piece(5, 2), moved_piece)
#         self.assertIsNone(self.board.get_piece(7, 1))

#     def test_move_pawn(self):
#         self.pawn = Pawn("WHITE")
#         self.board.set_piece(6, 0, self.pawn)
#         moved_piece = self.board.ejecutar_move(6, 0, 4, 0)
#         self.assertIsInstance(moved_piece, Pawn)
#         self.assertEqual(self.board.get_piece(4, 0), moved_piece)
#         self.assertIsNone(self.board.get_piece(6, 0))


#     def test_invalid_move(self):
#         self.horse = Horse("WHITE")
#         self.board.set_piece(7, 1, self.horse) 
#         with self.assertRaises(ValueError):
#             self.board.ejecutar_move(7, 1, 7, 3)


#     def test_queen_capture_horse(self):
#         queen = Queen("WHITE")
#         self.board.set_piece(4, 4, queen)
#         horse = Horse("BLACK")
#         self.board.set_piece(2, 4, horse)
#         moved_piece = self.board.ejecutar_move(4, 4, 2, 4)     
#         self.assertIsInstance(moved_piece, Queen) 
#         self.assertEqual(self.board.get_piece(2, 4), queen) 
#         self.assertIsNone(self.board.get_piece(4, 4)) 
#         self.assertNotEqual(self.board.get_piece(2, 4), horse) 

#     def test_king_capture_queen(self):
#         king = King("WHITE")
#         self.board.set_piece(4, 4, king)
#         queen = Queen("BLACK")
#         self.board.set_piece(3, 4, queen)  
#         moved_piece = self.board.ejecutar_move(4, 4, 3, 4)
#         self.assertIsInstance(moved_piece, King) 
#         self.assertEqual(self.board.get_piece(3, 4), king) 
#         self.assertIsNone(self.board.get_piece(4, 4)) 
#         self.assertNotEqual(self.board.get_piece(3, 4), queen) 

#     def test_bishop_capture_rook(self):
#         bishop = Bishop("BLACK")
#         self.board.set_piece(3, 3, bishop)
#         rook = Rook("WHITE")
#         self.board.set_piece(4, 4, rook)
#         moved_piece = self.board.ejecutar_move(3, 3, 4, 4)
#         self.assertIsInstance(moved_piece, Bishop)
#         self.assertEqual(self.board.get_piece(4, 4), bishop) 
#         self.assertIsNone(self.board.get_piece(3, 3)) 
#         self.assertNotEqual(self.board.get_piece(4, 4), rook)

#     def test_rook_capture_bishop(self):
#         rook = Rook("BLACK")
#         self.board.set_piece(3, 3, rook)
#         bishop = Bishop("WHITE")
#         self.board.set_piece(4, 3, bishop)
#         moved_piece = self.board.ejecutar_move(3, 3, 4, 3)
#         self.assertIsInstance(moved_piece, Rook) 
#         self.assertEqual(self.board.get_piece(4, 3), rook) 
#         self.assertIsNone(self.board.get_piece(3, 3)) 
#         self.assertNotEqual(self.board.get_piece(4, 3), bishop)

#     def test_no_piece(self):
#         with self.assertRaises(ValueError):
#             self.board.ejecutar_move(3, 2, 3, 3)

# if __name__ == '__main__':
#     unittest.main()

