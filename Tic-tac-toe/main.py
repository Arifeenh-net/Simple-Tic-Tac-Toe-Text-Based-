import random
import time
# Saving the winning combinations
winning_combs = [
    [0,1,2],
    [0,3,6],
    [0,4,8],
    [3,4,5],
    [6,7,8],
    [2,5,8],
    [1,4,7],
    [2,4,6]
]

player_score = 0

corners = [0, 2, 6, 8]

# Creating the board
def create_board():
    return [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
#Printing the game board
def print_game(game_board):
    print("Tic-Tac-Toe")
    print(f"{game_board[0]} | {game_board[1]} | {game_board[2]} ")
    print("---------")
    print(f"{game_board[3]} | {game_board[4]} | {game_board[5]} ")
    print("---------")
    print(f"{game_board[6]} | {game_board[7]} | {game_board[8]} ")



# Move making processor
def make_move(game_board):
    # Ensuring only 0 to 8 inputs are valid
    while True:
        try:
            position = int(input(f"Player's turn. Choose a position (0 to 8): "))
            if 0 <= position <= 8:
                break
            else:
                print("Please enter a number from 0 to 8.")
        except ValueError:
            print("Please enter a whole number!")
    if game_board[position] != " ":
        print("Board is already taken!")
        return False
    game_board[position] = "X"
    return True

def ai_move(game_board):
    empty_positions = []
    # Saving the empty positions
    for position in range(9):
        if game_board[position] == " ":
            empty_positions.append(position)
    # Checking if the next move will win
    for combination in winning_combs:
        if [game_board[position] for position in combination].count("O") == 2 and [game_board[position] for position in combination].count(" ") == 1:
            for position in combination:
                if game_board[position] == " ":
                    game_board[position] = "O"
                    return True
        # # Checking if the player is about to win
        elif [game_board[position] for position in combination].count("X") == 2 and [game_board[position] for position in combination].count(" ") == 1:
            for position in combination:
                if game_board[position] == " ":
                    game_board[position] = "O"
                    return True
    # Take the center position if empty
    if game_board[4] == " ":
       game_board[4] = "O"
       return True
    # Take the corners if empty
    for position in corners:
        if game_board[position] == " ":
            game_board[position] = "O"
            return True
    # Random location if all conditions fail to meet
    position = random.choice(empty_positions)
    game_board[position] = "O"
    return True

def choose_winner(game_board):
    for combination in winning_combs:
       #  Checking if any player's moves match the winning combination
       if all(game_board[position] == "X" for position in combination):
          print("Player Wins!")
          return "player"
       elif all(game_board[position] == "O" for position in combination):
          print("Computer Wins!")
          return "computer"
    return False

while True:
    board = create_board()
    print(f"Player Score: {player_score}")
    for turn in range(9):
        if turn % 2 == 0:
            made_moves = make_move(board)
            while not made_moves:
                made_moves = make_move(board)
        else:
            time.sleep(0.5)
            ai_move(board)
        print_game(board)
        game_over = choose_winner(board)
        if game_over == 'player':
            player_score += 1
            break
        elif game_over == "computer":
            break
    else:
        print("It's a Draw!")
