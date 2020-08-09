#By SANTOSH KHATRI
#TIC TAC TOE Game

#This will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#whether to play again or not.
def replay():
    while game_still_going == False:
        play_again=input("Do you want to play again?(y/n):")

        if play_again=='y':
            play_game()
        elif play_again=='n':
            print("Thank You For Playing Tic Tac Toe.")
            break
        else:
            print("Sorry.You Choosed wrong option.Please Choose again.")
def resetboard():
        board[0] = "-"
        board[1] = "-"
        board[2] = "-"
        board[3] = "-"
        board[4] = "-"
        board[5] = "-"
        board[6] = "-"
        board[7] = "-"
        board[8] = "-" 
        display_board()
        global game_still_going
        game_still_going = True
# to know if the game is over yet
game_still_going = True

# Tells us who is the winner
winner = None

# Tells us who the current player is (X goes first)
current_player = "X"
# ------------- Functions ---------------
# Play a game of tic tac toe
def play_game():    
    resetboard()
    # Show the initial game board
    #display_board()

    # Loop until the game stops (winner or tie)
    while game_still_going:
        # to Handle a turn
        handle_turn(current_player)

        # to check if the game is over
        check_if_game_over()

        # to flip  the other players
        flip_player()

    # Since the game is over, print the winner or tie
    if winner == "X" or winner == "Y":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

# Display the game board to the screen
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


# Handle a turn for an arbitrary player
def handle_turn(player):
    # to get position from player
    print(player + "'s turn.")
    position = input("Choose a number from 1-9: ")

    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a number from 1-9: ")

        # to get correct index in board list
        position = int(position) - 1

        # to make sure the spot is available on the board
        if board[position] == "-":
            valid = True
        else:
            print("This position is not available. Choose again.")

    # to put the game piece on the board
    board[position] = player

    # to show the game board
    display_board()


# to check if the game is over
def check_if_game_over():
    check_for_winner()
    check_for_tie()


# Check to see if somebody has won
def check_for_winner():
    global winner
    # to check if there was a winner anywhere
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    # to get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


# to check the rows for win
def check_rows():
    global game_still_going
    # to check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
        # Or return None if there was no winner
    else:
        return None


# Check the columns for a win
def check_columns():
    global game_still_going
    # Check if any of the columns have all the same value and is not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
        # Or return None if there was no winner
    else:
        return None


# Check the diagonals for a win
def check_diagonals():
    # Set global variables
    global game_still_going
    # Check if any of the columns have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    # Or return None if there was no winner
    else:
        return None


# Check if there is a tie
def check_for_tie():
    # Set global variables
    global game_still_going
    # If board is full
    if "-" not in board:
        game_still_going = False
        return True
    # Else there is no tie
    else:
        return False


# to change  the current player from X to Y, or Y to X
def flip_player():
    # Global variables we need
    global current_player
    # If the current player was X, make it Y
    if current_player == "X":
        current_player = "Y"
    # Or if the current player was Y, make it X
    elif current_player == "Y":
        current_player = "X"
play_game()
replay()