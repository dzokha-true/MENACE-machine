import random
import copy

beads = 8
WHOSE_TURN_IS_IT = 1  # will be passed to object. if it is divisible by 2 then it is players turn
GRIDS = [[8, 8, 8], [8, 8, 8], [8, 8, 8]]
# grid is given as a 2d array. First layer of arrays are rows. 2nd layer is columns

class Matchbox:
    def __init__(self, grid, parentnodes, childnodes, beads, WhoseTurn):
        """
        Initialize the matchbox object with given parameters
        grid: 2d array representing the tic-tac-toe game board
        parentnodes: list of parent nodes of this matchbox object
        childnodes: list of child nodes of this matchbox object
        beads: number of beads in the matchbox
        WhoseTurn: determines whose turn it is to play (1 for player, 0 for Menace)
        """
        self.grid = grid
        self.parentnode = parentnodes
        self.childnodes = childnodes
        self.beads = beads
        self.WhoseTurn = WhoseTurn
        self.next_step()

    def next_step(self):
        """
        Check if the game is won, if not, create child nodes and place beads
        """
        if not self.checking_win()[0]:  # if the game is not finished...
            self.creating_child(self.beads)
            self.placing_beads()

    def checking_win(self):
        """
        Check if there is a winning combination on the game board.

        Returns:
            A list with two elements, the first element is a boolean indicating if the game is won,
            and the second element is either "Menace" or "Player" depending on the winner.
        """
        if (self.grid[0][0] == 'x' or self.grid[0][0] == 'o') and self.grid[0][0] == self.grid[1][0] == self.grid[2][
            0]:  # for all vertical wins
            if self.grid[0][0] == "x":
                return [True, "Menace"]
            else:
                return [True, "Player"]
        elif (self.grid[0][1] == 'x' or self.grid[0][1] == 'o') and self.grid[0][1] == self.grid[1][1] == self.grid[2][
            1]:
            if self.grid[0][1] == "x":
                return [True, "Menace"]
            else:
                return [True, "Player"]
        elif (self.grid[0][2] == 'x' or self.grid[0][2] == 'o') and self.grid[0][2] == self.grid[1][2] == self.grid[2][
            2]:
            if self.grid[0][2] == "x":
                return [True, "Menace"]
            else:
                return [True, "Player"]  # end of vertical wins
        elif (self.grid[0][0] == 'x' or self.grid[0][0] == 'o') and self.grid[0][0] == self.grid[0][1] == self.grid[0][
            2]:  # start of horizontal wins
            if self.grid[0][0] == "x":
                return [True, "Menace"]
            else:
                return [True, "Player"]
        elif (self.grid[1][0] == 'x' or self.grid[1][0] == 'o') and self.grid[1][0] == self.grid[1][1] == self.grid[1][
            2]:
            if self.grid[1][0] == "x":
                return [True, "Menace"]
            else:
                return [True, "Player"]
        elif (self.grid[2][0] == 'x' or self.grid[2][0] == 'o') and self.grid[2][0] == self.grid[2][1] == self.grid[2][
            2]:
            if self.grid[2][0] == "x":
                return [True, "Menace"]
            else:
                return [True, "Player"]  # end of horizontal wins
        elif (self.grid[0][0] == 'x' or self.grid[0][0] == 'o') and self.grid[0][0] == self.grid[1][1] == self.grid[2][
            2]:
            if self.grid[0][0] == "x":
                return [True, "Menace"]
            else:
                return [True, "Player"]  # i am genuinely sorry that it looks so ugly, god will be my judge
        elif (self.grid[0][2] == 'x' or self.grid[0][2] == 'o') and self.grid[0][2] == self.grid[1][1] == self.grid[2][
            0]:
            if self.grid[0][2] == "x":
                return [True, "Menace"]
            else:
                return [True, "Player"]
        else:
            return [False, "draw"]

    def placing_beads(self):
        """
        Places beads on the board
        Changes the game board
        """
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] != self.beads and self.grid[i][j] != 'x' and self.grid[i][j] != 'o':
                    self.grid[i][j] = self.beads
        return self.grid

    def creating_child(self, beads):
        """
        Appends all possible next game states to the current Matchbox. Makes sure that if the game state is finished it
        doesn't continue with the code.
        :param beads: is used to append matchbox with the correct number of beads into unoccupied cell.
        :return: appending child nodes to the current node
        """
        thingy = copy.deepcopy(self.WhoseTurn)    # todo deelte this
        thingy += 1
        if (self.WhoseTurn % 2) != 0:
            for i in range(3):
                for j in range(3):
                    new_grid = copy.deepcopy(self.grid)
                    if new_grid[i][j] != "x" and new_grid[i][j] != "o" and new_grid[i][j] != 0:  # should never be zero unless user specifically defines 0 to be from the start
                        new_grid[i][j] = "x"
                        self.childnodes.append(Matchbox(new_grid, self, [], self.beads, thingy)) #TODO change thingy to WhoseTurn + 1
                    else:
                        self.childnodes.append(None)
        elif (self.WhoseTurn % 2) == 0:
            for i in range(3):
                for j in range(3):
                    new_grid = copy.deepcopy(self.grid)
                    if self.grid[i][j] != "x" and self.grid[i][j] != "o":
                        new_grid[i][j] = "o"
                        # print(f"flag one 1\n\nnew grid is {new_grid}")
                        self.childnodes.append(Matchbox(new_grid, self, [], self.beads, thingy)) #TODO change thingy to WhoseTurn + 1

                    else:
                        # print(f"flag 2\n")
                        self.childnodes.append(None)

    def user_go(self, grid):
        """
        Takes a player input in the (row,column) format. It must be a tuple. Might have security issues because of the
        eval() line, but the project is aimed to not be used on the web-servers. Makes sure that the players go won't
        lead to the illegal game state.
        :param grid: grid that is needed to be output to the player, so it is easy for them to understand what is going on
        :return: the coordinates that player has chosen for their go.
        """
        current_grid = copy.deepcopy(grid)
        user_go = input(f" {grid[0]} \n {grid[1]}\n {grid[2]}\nPut your move in (row,column) format, with no space: ")
        user_go = eval(user_go)
        if type(user_go) != type((0, 0)) or len(user_go) != 2 or type(grid[user_go[0]][user_go[1]]) != type(
                0):  # checking if user_go is the right format
            print(f"you have put the answer in the wrong format, or used occupied cell. Please try again. ")
            self.user_go(grid)
        else:
            return user_go

    def game(self):
        if self.checking_win()[1] == "Menace": #if the menace hast won...
            print("Menace has won")
            return [True, "Menace"]
        elif self.checking_win()[1] == "Player":  #or if the player hast won...
            print("Player has won")
            return [False, "Player"]
        elif self.checking_win()[0] is False:
            if self.WhoseTurn % 2 != 0:   # if the matchbox has a turn for MENACE...
                count = 0
                for row in range(0, 3):
                    for col in range(0, 3):
                        if self.grid[row][col] != 'x' and self.grid[row][col] != 'o':
                            count += self.grid[row][col]      #...count the total number of beads...

                random_x = random.randint(0, count)       #...set the random number...
                break_out_flag = False
                index = 0           #index will be used to locate matchbox inside childnode that is same for current gametstate
                for row2 in range(0, 3): #start process of MENACE choosing where to place an x
                    for col2 in range(0, 3):
                        print(f"random x is {random_x}")
                        if type(self.grid[row2][col2]) == type(0):  # checking whether column in a row is an integer
                            if random_x - self.grid[row2][col2] <= 0:
                                break_out_flag = True  #if this cell is choosen by MENACE, set the loopbreaker to True
                                break
                            else:
                                random_x -= self.grid[row2][col2] #otherwise continue, and increment an x
                                index += 1
                        else:
                            index += 1 # if the cell wasn't integer, skip it and increment the index by one (cause it cant be menace's choice)
                            pass
                    if break_out_flag: #if the MENACE made its choice...
                        self.row2 = row2
                        self.col2 = col2
                        self.placed_x = (self.row2, self.col2) #remember where it has placed its' x
                        break #and break
                result = self.childnodes[index].game() #call the next game with that index.
                print(result)
                if (result[0] == True):
                    self.grid[self.placed_x[0]][self.placed_x[1]] += 3
                    return [True, "Menace"]
                elif (result[0] == False):
                    self.grid[self.placed_x[0]][self.placed_x[1]] -= 2
                    return [False, "Player"]
            elif self.WhoseTurn % 2 == 0:
                user_cords = self.user_go(self.grid)
                index = ((3 * user_cords[0]) + (user_cords[1])) # calculates the index of the matchbox with the same game
                                                                # grid inside the childnode list.
                result = self.childnodes[index].game()
                print(result)
                if result[0] == True:
                    return [True, "Menace"]
                elif result[0] == False:
                    return [False, "Player"]

matchbox = Matchbox(GRIDS, [], [], beads, WhoseTurn=WHOSE_TURN_IS_IT)
user_decided = int(input("please input the number of times you want to play a game please "))
for i in range(user_decided):
    matchbox.game()
print(matchbox.grid)
# print(f"\n\nParent node is {matchbox.childnodes[0].grid}, Whoseturn {matchbox.childnodes[0].WhoseTurn}\n childnode is {matchbox.childnodes[0].childnodes[2].grid}\n\n")