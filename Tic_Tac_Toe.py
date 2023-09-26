def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                raise ValueError("Invalid input. Please enter a number between 1 and 9.")
            return move
        except ValueError as e:
            print(e)

def update_board(board, move, player):
    row = (move - 1) // 3
    col = (move - 1) % 3

    if board[row][col] == " ":
        board[row][col] = player
        return True
    else:
        print("Invalid move. That spot is already taken.")
        return False

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        move = get_move()
        if update_board(board, move, current_player):
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
