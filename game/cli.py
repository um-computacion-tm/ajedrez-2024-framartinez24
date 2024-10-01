from chess import Chess
def main():
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
            to_col,
        )
    except Exception as e:
        print("error", e)

def give_up(chess):
    answer = input("Player " + chess.turn + "Giving up ah? (y/n)").lower()
    if answer == "y":
        print(f"Player Chicken {chess.turn} gave up")
        chess.end_game() 
        return

if __name__ == '__main__':
    main()