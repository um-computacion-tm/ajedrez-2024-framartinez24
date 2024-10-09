## [0.0.1.0] - 26|08|2024
### Added
- A new file, `piece.py`, has been added, providing the `get_color` function for each piece.
- Previous pieces remain unchanged.
- The game is not yet playable, and some pieces are missing.

## [0.0.2] - 26|08|2024
### Added
- `Bishop`, `Horse`, `King`, `Queen`, and `Rook` pieces have been added.
- Each piece has been assigned a color (white or black) as described in the readme.
- Translated the readme file to English.
### Removed
- Old files `main.py` and settings tests.

## [0.0.2.1] - 26|08|2024 17:00
### Added
- Created empty `test.py` files for each game component.

## [0.0.2.2] - 26|08|2024 18:28
### Modified
- `Board.py` now imports pieces and includes a graphical grid guide for development.
- Initial positions of pieces are set on the board.

## [0.0.2.3] - 26|08|2024 19:30
### Modified
- `Pawn.py` has been enhanced with two new functions:
  - `valid_moves`: Determines pawn movement validity and identifies potential enemy captures.
  - `move`: Calls `valid_moves` to update pawn's coordinates and removes captured pieces.

## [0.0.2.4] - 26|08|2024 21:46
### Modified
- Added validation in `Pawn.py` to check if the piece has moved.
- Established `Rook.py` with logic similar to `Pawn`, including castling logic and exceptions.

## [0.0.2.4] - 26|08|2024 22:26
### Modified
- Completed basic logic for `Bishop.py`, featuring diagonal movements similar to other pieces.

## [0.0.2.5] - 26|08|2024 23:50
### Modified
- `Queen.py`, `King.py`, and `Horse.py` were enhanced with additional logic and functionalities.

## [0.0.3] - 27|08|2024 10:30
### Modified
- Updated `Board.py` and `cli.py` to fix bugs related to terminal printing.
- Printing functionality still needs further development.

## [0.0.3.1] - 27|08|2024 11:10
### Modified
- Fixed issues in `pawn.py` with color settings and diagonal movement.
- Streamlined and reorganized `Chess` code.

## [0.0.3.2] - 27|08|2024 14:35
### Modified
- Fixed `rook.py` color issue where a white rook was printing as black.

## [0.0.3.3] - 27|08|2024 15:25
### Modified
- Refactored `Queen.py` and `King.py` to ensure correct movement, though some issues with unrestricted movement remain.

## [0.0.3.3] - 27|08|2024 20:00
### Added
- Refactored movement logic for all pieces by adding `class MoveLogic` to reduce redundancy and improve reliability.

## [0.0.3.4] - 27|08|2024 20:50
### Added
- Refactored `Horse.py` and `King.py` by adding `class Movement` and `class Direction` to handle movement logic for both pieces.

## [0.0.3.4] - 27|08|2024 21:30
### Modified
- Simplified complexity in `pawn.py` and prepared for integration into class form in future versions.

## [0.0.3.5] - 5|09|2024 
### Added 
- `pawn_test` added. 

## [0.0.3.6] - 6|09|2024 
### Added 
- `rook_test` added. 

## [0.0.3.7] - 7|09|2024 
### Added 
- `horse_test` added. 

## [0.0.3.5] - 8|09|2024 
### Added 
- `bishop_test` added. 

## [0.0.3.5] - 10|09|2024 
### Added 
- `queen_test` added. 
### Modified
- Changelog.md refactoriced and simplified.

## [0.0.4.0] - 9|10|2024 
### Modified
- Many changes were made, in order to synthesize the code and improve robustness. The code was refactored following OOP guidelines. Still in progress. The tests have not been uploaded but are already mostly operational.
### Comments 
- Board.py, chess.py, cli.py must be entirely re-writen, function.py will be removed asap.