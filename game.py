# 🎮 Tic-Tac-Toe Game in Python (Jupyter Notebook)

# Display the game board
def display_board(board):
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

# Check if the current player has won
def check_win(board, player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    return any(board[i] == board[j] == board[k] == player for i,j,k in win_conditions)

# Main game logic
def play_game():
    board = [" " for _ in range(9)]
    current_player = "X"

    for turn in range(9):
        display_board(board)
        try:
            move = int(input(f"Player {current_player}, choose your move (0-8): "))
            while move < 0 or move > 8 or board[move] != " ":
                move = int(input("Invalid move! Try again (0-8): "))
        except:
            print("⚠️ Please enter a valid number between 0 and 8.")
            continue

        board[move] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    display_board(board)
    print("It's a draw!")

# Run the game
play_game()
