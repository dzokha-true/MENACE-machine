import random

class MenaceMachine:
    def __init__(self):
        self.matchboxes = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(2)]
        self.matchbox_counts = [[0 for _ in range(3)] for _ in range(3)]

    def play_move(self, board):
        available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

        if not available_moves:
            return None

        move = None
        max_count = -1
        for i, j in available_moves:
            matchbox = self.matchboxes[board[i][j]][i][j]
            if matchbox > max_count:
                move = (i, j)
                max_count = matchbox

        if max_count == 0:
            move = random.choice(available_moves)

        self.matchbox_counts[move[0]][move[1]] += 1
        return move

    def update_matchboxes(self, board, move, player):
        matchbox = self.matchboxes[player][move[0]][move[1]]
        matchbox[self.matchbox_counts[move[0]][move[1]] - 1] = 1

    def play(self, board, player):
        move = self.play_move(board)
        if move is None:
            return None
        board[move[0]][move[1]] = player
        self.update_matchboxes(board, move, player)
        return move

    def train(self, opponent_move_function):
        board = [[0 for _ in range(3)] for _ in range(3)]
        player = 1
        while True:
            move = self.play(board, player)
            if move is None or self.is_win(board, player):
                self.reset_matchboxes()
                return

            opponent_move = opponent_move_function(board)
            if opponent_move is None or self.is_win(board, player % 2 + 1):
                self.reset_matchboxes()
                return

            player = player % 2 + 1

    def is_win(self, board, player):
        for i in range(3):
            if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                return True
            if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                return True

        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
        return False

    def reset_matchboxes(self):
        self.matchbox_counts = [[0 for _ in range(3)] for _ in range(3)]

