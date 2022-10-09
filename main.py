import random, pickle, numpy as np


class Matchbox:
    """ this class takes 2 dimensional array as an representation of game state which it will represent.
        it must be in a form of ( array1, array2, array3 ) where arrays reoresent the game state as individual row  """
    def __init__(self, setup: list):
        self.grid = setup
        self.grid = np.array(self.grid)

    def spawn_from_first_layer(self):
        for i in self.grid:
            # print(i)
            for j in i:
                if j != 0 or "x" or "o": #i.e there is a bead that can be placed
                    new_grid = self.grid
                    index_of_placing = np.where(new_grid == j)
                    print(index_of_placing)
                    #new_grid[altered_row][altered_element_index] = "x"
                    # MB.boxtreeroot.append(Matchbox(new_grid))


                    # add some zeroes
                    # mb.boxtreeroot[-1].spawn() need to create a method that would spawn a grid with suitable amount of beads.

    def place_a_bead(self):
        available_places = []
        for i in self.grid:
            for j in i:
                if j != 0 or "x" or "o":
                    available_places.append([i, j])
        print(available_places)

    def spawn_from_second_layer(self):
        pass

    def spawn_from_third_layer(self):
        pass

    def spawn_from_forth_layer(self):
        pass

    def rotate(self):
        self.grid = np.fliplr(np.array(self.grid).T.tolist())

    def check_if_duplicate(self):
        pass


class Matchboxes:
    """ this is a object which is basically a array which can be accessed inside the matchbox class"""
    def __init__(self):
        self.boxtreeroot = []


MB = Matchboxes()
MB.boxtreeroot.append(Matchbox([[8, 8, 0], [0, 8, 0], [0, 0, 0]]))
MB.boxtreeroot[0].spawn_from_first_layer()
