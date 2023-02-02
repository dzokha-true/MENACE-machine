import random

# Define the board and its initial state
board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]

# Define the MENACE machine's memory
memory = []

# Function to check if the game has been won by either player
def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False

# Function to display the current state of the board
def display_board(board):
    for row in board:
        print(row)

# Function to get the user's move
def get_user_move(board):
    move = input("Enter your move in the format 'row,column': ")
    row, col = [int(x) for x in move.split(',')]
    if board[row][col] == ' ':
        board[row][col] = 'X'
    else:
        print("Invalid move, try again.")
        get_user_move(board)

# Function to get the MENACE machine's move
def get_machine_move(board, memory):
    matchboxes = [x[:9] for x in memory if x[9] == 'O']
    beads = [x[9:] for x in memory if x[9] == 'O']
    if not matchboxes:
        matchboxes.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        beads.append(0)
    move = matchboxes[beads.index(max(beads))]
    for i in range(9):
        if board[i//3][i%3] == ' ':
            move[i] += 1
    move_index = move.index(max(move))
    board[move_index//3][move_index%3] = 'O'
    memory.append([x for x in move] + ['O'])

# Main game loop
while not check_win(board):
    display_board(board)
    get_user_move(board)
    if not check_win(board):
        get_machine_move(board, memory)

# Print the final state of the board and the winner
display_board(board)
if check_win(board):
    print("The winner is " + board[move_index//3][move_index%3])
else:
    print("It's a tie!")
