from game.chess import Chess
from game.exceptions import InvalidMove 

def main():
    print("Welcome to PythonChess")
    chess = Chess()
    while chess.is_playing():
        play(chess)

def play(chess):
    try:
        print(chess.show_board())
        print("turn: ", chess.turn)
        from_row = int(input("From Row →: "))
        from_col = int(input("From Col ↓: "))
        to_row = int(input("To Row →: "))
        to_col = int(input("To Col ↓: "))
        chess.move(
            from_row,
            from_col,
            to_row,
            to_col)
        give_up(chess)
        
    except InvalidMove as e:
        print(e)
    except Exception as e:
        print("Error:", e)

def give_up(chess):
    answer = input("Player " + chess.turn + "Giving up ah? (y/n)").lower()
    if answer == "y":
        print(f"Player Chicken {chess.turn} gave up")
        chess.end_game() 
        return

if __name__ == '__main__':
    main()