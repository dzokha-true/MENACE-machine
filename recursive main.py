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
            return [False, 0]

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
                        self.childnodes.append(Matchbox(new_grid, [self], [], self.beads, thingy)) #TODO change thingy to WhoseTurn + 1
                    else:
                        self.childnodes.append(None)
        elif (self.WhoseTurn % 2) == 0:
            for i in range(3):
                for j in range(3):
                    new_grid = copy.deepcopy(self.grid)
                    if self.grid[i][j] != "x" and self.grid[i][j] != "o":
                        new_grid[i][j] = "o"
                        # print(f"flag one 1\n\nnew grid is {new_grid}")
                        self.childnodes.append(Matchbox(new_grid, [self], [], self.beads, thingy)) #TODO change thingy to WhoseTurn + 1

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
        if self.WhoseTurn % 1 == 0:
            count = 0
            for row in range(0, 3):
                for col in range(0, 3):
                    if self.grid[row][col] != 'x' and self.grid[row][col] != 'o':
                        count += self.grid[row][col]      #count the total number of beads

            random_x = random.randint(0, count)       #set the random number
            break_out_flag = False
            index = 0           #set the index of the game.
            for row2 in range(0, 3):
                for col2 in range(0, 3):
                    print(f"random x is {random_x}")
                    if type(self.grid[row2][col2]) == type(0):  # checking whether column in a row is an integer
                        if random_x - self.grid[row2][col2] <= 0: #todo check indexing problem
                            break_out_flag = True
                            break
                        else:
                            index += 1
                            random_x -= self.grid[row2][col2]
                if break_out_flag:
                    break
                    # else:
                    #     index += 1
                    #     random_x -= self.grid[row2][col2]
            placed_x = (row2, col2)
            print(f"here we go...\nINDEX is {index},\nCURRENT game board is {self.grid}, \nCHILDNODES are {self.childnodes}")
            self.result = self.childnodes[index].game()
        else:
            user_cords = self.user_go(self.grid)
            index = ((3 * user_cords[0]) + (user_cords[1])) # calculates the index of the matchbox with the same game
            # grid inside the childnode list.
            self.result = self.childnodes[index].game()
        if self.checking_win()[1] == "Menace":
            return True
        elif self.checking_win()[1] == "Player":
            return False
        elif self.checking_win()[0] is False:
            pass
            # if self.game(matchbox) == True:
            #     self.parentnode.grid[placed_x[0]][placed_x[1]] += 3
            # else:
            #     pass


# matchbox = Matchbox(GRIDS, [], [], beads, WhoseTurn=WHOSE_TURN_IS_IT)

matchbox = Matchbox(GRIDS, [], [], beads, WhoseTurn=WHOSE_TURN_IS_IT)
matchbox.game()
# print(f"\n\nParent node is {matchbox.childnodes[0].grid}, Whoseturn {matchbox.childnodes[0].WhoseTurn}\n childnode is {matchbox.childnodes[0].childnodes[2].grid}\n\n")