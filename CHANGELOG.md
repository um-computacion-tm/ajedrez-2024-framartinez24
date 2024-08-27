## CHANGELOG
# Version 0.0.1.0 (26/8/24) -Choosing color-
Added: piece.py this files provides "get_color" for everypiece
The others pieces was added before and there isn't changes yet. 
Game is not playable and some pieces are missing.

# Version 0.0.2 (26/8/24) -Party friends-
Added: pieces bishop, horse, king, queen and rook; Has been added with the method to get their own color (white or black) to each piece.
Modified: Readme has been translated to english. 
Removed: old garbage files. (main.py and tests for settings only).
The structure of the game is almost done, the board file will work as main, there must be all the pieces imported to be used into the game. 
"This version is just the beginning, and it will grow over time."

# Version 0.0.2.1 (26/8/24) 17:00 -Test Structure-
Added: All test.py for each piece of the game, there are only files without content.

# Version 0.0.2.2 (26/8/24) 18:28 -Guides and initial settings-
Modified: Board.py: Pieces import added, graphic grid guide for development purposes included, and initial piece positions on the board set.

# Version 0.0.2.3 (26/8/24) 19:30 -Pawn functions-
Modified: pawn.py:  2 functions added
1: valid_moves: This function check if the movements to be done for the pawn are possible or not & check if there's an enemy piece to be taken. If the 2 conditions are valid (True) -> function move can be done.
2: move: This function calls valid_moves and if the move is True, update the state of the col & row of the pawn and remove the enemy piece taken(if there is one).
 
 # Version 0.0.2.4 (26/8/24) 21:46 -Rook functions-
 Modified: Pawn.py added missing line to validate if the piece has been moved or not. 
 Rook.py basic features and logics are done, it's similar to pawn but adding some exceptions and some states to do "castling", which is a move only can be made for rook.

 
 # Version 0.0.2.4 (26/8/24) 21:46 -Bishop functions-
Modified: bishop.py basic features and logics are done. Similar to the other pieces but in diagonal. 




