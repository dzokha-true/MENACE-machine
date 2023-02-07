import random
import copy

beads = 8
WHOSE_TURN_IS_IT = 1  # will be passed to object. if it is divisble by 2 then it is players turn
GRIDS = [[8, 8, 8], [8, 8, 8], [8, 8, 8]]

#grid is given as a 2d array. First layer of arrays are rows. 2nd layer is columns

class Matchbox:
    def __init__(self, grid, parentnodes, childnodes, beads, WhoseTurn):
        self.grid = grid
        self.parentnode = parentnodes
        self.childnodes = childnodes
        self.beads = beads
        self.WhoseTurn = WhoseTurn
        self.next_step()

    def place_beads(self):
        for i in range(1, 3):
            for j in range(1, 3):
                if self.grid[i][j] != "x" and self.grid[i][j] != "o":
                    self.grid[i][j] = beads

    def next_step(self):
        # print(self.grid)
        if self.checking_win() == False:
            self.creating_child(self.beads)
            self.placing_beads()
        else:
            if self.grid[0][0] == 'x': #i.e. the game was won by menace machine
                pass
        # checking winning

    def checking_win(self):
        if (self.grid[0][0] == 'x' or self.grid[0][0] == 'o') and self.grid[0][0] == self.grid[1][0] == self.grid[2][
            0]:  # for all vertical wins
            return True
        elif (self.grid[0][1] == 'x' or self.grid[0][1] == 'o') and self.grid[0][1] == self.grid[1][1] == self.grid[2][1]:
            return True
        elif (self.grid[0][2] == 'x' or self.grid[0][2] == 'o') and self.grid[0][2] == self.grid[1][2] == self.grid[2][2]:
            return True  # end of vertical wins
        elif (self.grid[0][0] == 'x' or self.grid[0][0] == 'o') and self.grid[0][0] == self.grid[0][1] == self.grid[0][
            2]:  # start of horizontal wins
            return True
        elif (self.grid[1][0] == 'x' or self.grid[1][0] == 'o') and self.grid[1][0] == self.grid[1][1] == self.grid[1][2]:
            return True
        elif (self.grid[2][0] == 'x' or self.grid[2][0] == 'o') and self.grid[2][0] == self.grid[2][1] == self.grid[2][2]:
            return True  # end of horziontal wins
        elif (self.grid[0][0] == 'x' or self.grid[0][0] == 'o') and self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            return True  # i am genuinely sorry that it looks so ugly, god will be my judge
        elif (self.grid[0][2] == 'x' or self.grid[0][2] == 'o') and self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
            return True
        else:
            return False

    def placing_beads(self):
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] != self.beads and self.grid[i][j] != 'x' and self.grid[i][j] != 'x':
                    self.grid[i][j] = self.beads

    def creating_child(self, beads):
        if self.WhoseTurn % 2 != 0:
            self.WhoseTurn += 1
            for i in range(3):
                for j in range(3):
                    new_grid = copy.deepcopy(self.grid)
                    if new_grid[i][j] != "x" and new_grid[i][j] != "o" and new_grid[i][j] != 0:
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

    def user_go(self, grid):
        current_grid = grid
        user_go = input(f" {grid[0]} \n {grid[1]}\n {grid[2]}\nPut your move in (row,column) format, with no space: ")
        user_go = eval(user_go)
        if type(user_go) != type((0,0)) or len(user_go) != 2 or type(grid[user_go[0]][user_go[1]]) != type(0): #checking if user_go is the right format
                print(f"you have putted the answer in the wrong format, or used occupied cell. Please try again. ")
                new_grid = self.user_go(grid)
        else:
            current_grid[user_go[0]][user_go[1]] = "o"
            new_grid = current_grid
        return new_grid

    def game(self):
        current_game_grid = copy.deepcopy(self.grid)
        self.count = 0
        for row in range(0,3):
            for col in range(0,3):
                if self.grid[row][col] != 'x' and self.grid[row][col] != 'o':
                    self.count += self.grid[row][col]

        self.random_x = random.randint(0, self.count)
        print(f"count is {self.count}")
        print(f"random is {self.random_x}")
        break_out_flag = False
        for row2 in range(0,3):
            for col2 in range(0,3):
                if type(col2) == type(0):   #checking whether column in a row is an integer
                    if self.random_x - self.grid[row2][col2] <= 0:
                        print(f"triggered <=self.random_x {self.random_x}")
                        print(f"row and col are {row2} {col2}")
                        break_out_flag = True
                        break
                    else:
                        self.random_x -= self.grid[row2][col2]
                        print(f"self count is {self.random_x}")
            if break_out_flag == True:
                break
        print(row2, col2)
        current_game_grid[row2][col2] = 'x'
        new_grid = self.user_go(current_game_grid)
        print(new_grid)
        # except What_ever_mistake:
        #       print (hey whatcha tryna do brwoski)
        #       user_go()
        # user_go_tuple = tuple(int(item) for item in user_go_tuple.split())
        # current_game_grid[user_go_tuple[0]][user_go_tuple[1]] = "o"
        # print(current_game_grid)

matchbox = Matchbox(GRIDS, [], [], beads, WhoseTurn=WHOSE_TURN_IS_IT)

matchbox.game()