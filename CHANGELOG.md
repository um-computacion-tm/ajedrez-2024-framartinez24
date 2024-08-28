## CHANGELOG
# Version 0.0.1.0 (26/8/24) -Choosing color-
A new file, piece.py, has been added to the program. This file provides a function, "get_color," for each piece. The remaining pieces were previously added to the program, but no changes have been made to them yet. The game is not yet playable, and some pieces are missing.

# Version 0.0.2 (26/8/24) -Party friends-
The following pieces have been added to the game: bishop, horse, king, queen, and rook. Each piece has been assigned a color (white or black) using the method described in the readme file.
Modifications: The readme file has been translated into English.
Removals: The old, superfluous files (main.py and tests for settings) have been removed.
The structure of the game is almost complete. The board file will serve as the main file, and all pieces must be imported for use in the game.

# Version 0.0.2.1 (26/8/24) 17:00 -Test Structure-
Added: All test.py files for each component of the game are devoid of content.

# Version 0.0.2.2 (26/8/24) 18:28 -Guides and initial settings-
Modified: Board.py 
In the board.py file, the pieces have been imported, a graphic grid guide has been added for development purposes, and the initial positions of the pieces on the board have been set.

# Version 0.0.2.3 (26/8/24) 19:30 -Pawn functions-
Modified: The pawn.py 
Has been augmented with two new functions. The first is valid_moves. This function determines the feasibility of the proposed pawn movements and identifies potential opportunities for capturing enemy pieces. If both conditions are met, the move can be executed.
2: move: This function calls valid_moves and, if the move is valid, updates the pawn's column and row coordinates and removes any captured enemy pieces.
 
 # Version 0.0.2.4 (26/8/24) 21:46 -Rook functions-
 Modified: Pawn.py 
 A missing line was added to validate whether the piece has been moved or not. The fundamental characteristics and operational logic of Rook.py have been established. It is comparable to Pawn, but with the incorporation of exceptions and states for "castling," a maneuver exclusive to Rook.

 
 # Version 0.0.2.4 (26/8/24) 22:26 -Bishop functions-
Modified: bishop.py
The fundamental characteristics and underlying logic of the Bishop.py program have been completed. Its design is analogous to that of the other components, but with a diagonal orientation. 

# Version 0.0.2.5 (26/8/24) 23:50 -King & queen on horses-
Modified: queen.py, king.py, and horse.py 
Have been enhanced with additional fundamental logic and functionalities. 

# Version 0.0.3 (27/8/24) 10:30 -Board visible on terminal-
Modified: Board.py & cli.py 
The software has been updated to address some of the bugs that were previously affecting the printing functionality on the terminal. However, it is important to note that the printing mode is still in its infancy and has significant limitations.
Further improvements are necessary to ensure that the movements and features of all pieces are fully operational.

# Version 0.0.3.1 (27/8/24) 11:10 -Refactoriced Pawn and chess-
Modified: pawn.py 
There were some issues with the color settings and the ability to move forward and diagonally. These have now been resolved, and the white pawn can move freely.
The Chess code has been streamlined and reorganized.

# Version 0.0.3.2 (27/8/24) 14:35 -Rook on correctly color now-
Modified: rook.py
An error was identified in the color settings. When the WHITE color was selected, the print returned a black rook.
The issue has been resolved, and rook is now functioning correctly for the board and able to take other enemy pieces.

# Version 0.0.3.3 (27/8/24) 15:25 -King & Queen-
Modified: queen.py & king.py 
The queen and king have undergone a refactoring process, enabling them to move in accordance with the desired specifications. However, there are still aspects that require attention. Currently, many pieces are capable of moving to any location without restriction or engaging in illegal movements.

# Version 0.0.3.3 (27/8/24) 20:00 -Move def added as class-
Modified: all pieces. 
Added: class MoveLogic
Each component has undergone a process of refactoring. The block of code responsible for performing all the moves has been modified and refactored to utilize a class. This approach reduces the amount of repeated code and enhances the overall reliability of the program.

# Version 0.0.3.4 (27/8/24) 20:50 -King & Horse logic class-
Modified: horse.py king.py
Add: class Movement & class direction
The block code utilized for both horse and king movements is analogous. This block has undergone a refactoring process and has been imported as a class.

# Version 0.0.3.4 (27/8/24) 21:30 -Pawn complexity reduction-
Modified: pawn.py
The pawn presented some issues with regard to the complexity code, which have now been resolved. It will be incorporated into the class form in subsequent versions.