import random
import copy

beads = 8
WHOSE_TURN_IS_IT = 1  # will be passed to object. if it is divisible by 2 then it is players turn
GRIDS = [[' ' for _ in range(3)] for _ in range(3)]
memory = {}


class Matchbox:
    def __init__(self, grid, parentnodes, childnodes, beads, WhoseTurn):
        self.grid = grid
        self.parentnode = parentnodes
        self.childnodes = childnodes
        self.beads = beads
        self.WhoseTurn = WhoseTurn
        self.place_beads()
        self.next_step()

    def place_beads(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == ' ':
                    self.grid[i][j] = beads

    def next_step(self):
        self.beads = self.beads / 2
        winner = self.checking_win()
        if winner == None:
            self.creating_child()
        else:
            self.update_memory(winner)

    def checking_win(self):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != ' ':
                return self.grid[i][0]
        for i in range(3):
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != ' ':
                return self.grid[0][i]
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != ' ':
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != ' ':
            return self.grid[0][2]
        if ' ' not in [cell for row in self.grid for cell in row]:
            return 'Draw'
        return None

    def creating_child(self):
        if self.WhoseTurn % 2 != 0:
            self.WhoseTurn += 1
            for i in range(3):
                for j in range(3):
                    new_grid = copy.deepcopy(self.grid)
                    if new_grid[i][j] == ' ':
                        new_grid[i][j] = 'X' if self.WhoseTurn % 2 != 0 else 'O'
                        child_node = Matchbox(new_grid, self, [], beads, self.WhoseTurn)
                        self.childnodes.append(child_node)

    def print_board(self):
        for row in self.grid:
            print(" ".join(row))

    def update_memory(self, winner):
        if winner == 'X':
            reward = 1
        elif winner == 'O':
            reward = -1
        else:
            return
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] != ' ':
                    move = (i, j)
                    memory[str(move)] = memory.get(str(move), 0) + reward

    def play_game():
        game = Matchbox(GRIDS, None, [], beads, WHOSE_TURN_IS_IT)
        while not game.checking_win():
            game.print_board()
            move = get_move(game)
            if move is None:
                print("Invalid move, please try again.")
                continue
            game.grid[move[0]][move[1]] = 'X' if WHOSE_TURN_IS_IT % 2 != 0 else 'O'
            game.next_step()
            WHOSE_TURN_IS_IT += 1
        game.print_board()
        winner = game.checking_win()
        if winner == 'X':
            print("You win!")
        elif winner == 'O':
            print("MENACE wins!")
        else:
            print("It's a draw!")

    def get_move(game):
        x, y = input("Enter your move (row column): ").split()
        x, y = int(x), int(y)
        if x < 0 or x > 2 or y < 0 or y > 2:
            return None
        if game.grid[x][y] != ' ':
            return None
        return x, y

    play_game()