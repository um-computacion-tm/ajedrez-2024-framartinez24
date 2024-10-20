from game.board import Board
from game.exceptions import InvalidTurn, EmptyPosition
from game.king import King

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.playing = True
        self.winner = None

    def is_playing(self): 
        return self.playing

    def move(self, from_row,
             from_col,
             to_row,
             to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece:
            raise EmptyPosition()
        if not piece.get_color() == self.__turn__:
            raise InvalidTurn()
        piece_took = self.__board__.perform_movement(from_row, from_col, to_row, to_col)
        
        self.view_king()
        if not self.winner:
            self.change_turn()

    def end_game(self):
        self.playing = False  
        print(f"Winner: {self.winner}")

    def view_king(self):
        white_king_found = any(isinstance(self.__board__.get_piece(row, col), King) and self.__board__.get_piece(row, col).get_color() == "WHITE" for row in range(8) for col in range(8))

        black_king_found = any(isinstance(self.__board__.get_piece(row, col), King) and self.__board__.get_piece(row, col).get_color() == "BLACK" for row in range(8) for col in range(8))
        if not white_king_found:
            self.winner = "BLACK"
            self.end_game()
        elif not black_king_found:
            self.winner = "WHITE"
            self.end_game()

    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
            
    def set_turn(self, turn):
       if turn in ["WHITE", "BLACK"]:
           self.__turn__ = turn
       else:
           raise ValueError("Must be white or black!")

