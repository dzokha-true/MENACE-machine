import random
import copy

beads = 8
WHOSE_TURN_IS_IT = 1  # will be passed to object. if it is divisble by 2 then it is players turn
GRIDS = [[8, 8, 0], [0, 8, 0], [0, 0, 0]]


class Matchbox:
    def __init__(self, grid, parentnodes, childnodes, beads, WhoseTurn):
        self.grid = grid
        self.parentnode = parentnodes
        self.childnodes = childnodes
        self.beads = beads
        self.WhoseTurn = WhoseTurn
        self.creating_child()

    def place_beads(self):
        for i in range(1, 3):
            for j in range(1, 3):
                if self.grid[i][j] != "x" and self.grid[i][j] != "o":
                    self.grid[i][j] = beads

    def next_step(self):
        self.beads = self.beads / 2
        if self.checking_win() == False:
            pass
        # checking winning

    def checking_win(self):
        if self.grid[0][0] == self.grid[1][0] == self.grid[2][0]:  # for all vertical wins
            return True
        if self.grid[0][1] == self.grid[1][1] == self.grid[2][1]:
            return True
        if self.grid[0][2] == self.grid[1][2] == self.grid[2][2]:
            return True  # end of vertical wins
        if self.grid[0][0] == self.grid[0][1] == self.grid[0][2]:  # start of horizontal wins
            return True
        if self.grid[1][0] == self.grid[1][1] == self.grid[1][2]:
            return True
        if self.grid[2][0] == self.grid[2][1] == self.grid[2][2]:
            return True  # end of horziontal wins
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            return True  # i am genuinely sorry that it looks so ugly, god will
            # be my judge
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
            return True

    def creating_child(self):
        if self.WhoseTurn % 2 != 0:
            self.WhoseTurn += 1
            for i in range(3):
                for j in range(3):
                    new_grid = copy.deepcopy(self.grid)
                    if new_grid[i][j] != "x" and new_grid[i][j] != "o":
                        new_grid[i][j] = "x"
                        self.childnodes.append(Matchbox(new_grid, [self], [], self.beads, self.WhoseTurn))
        elif self.WhoseTurn % 2 == 0:
            self.WhoseTurn += 1
            for i in range(3):
                for j in range(3):
                    new_grid = copy.deepcopy(self.grid)
                    if self.grid[i][j] != "x" and self.grid[i][j] != "o":
                        new_grid[i][j] = "o"
                        self.childnodes.append(Matchbox(new_grid, [self], [], self.beads, self.WhoseTurn))


matchbox = Matchbox(GRIDS, [], [], beads, WhoseTurn=WHOSE_TURN_IS_IT)

print(matchbox.childnodes[0].grid)
