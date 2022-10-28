import random, pickle, numpy as np, copy


class Matchbox:
    """ this class takes 2 dimensional array as an representation of game state which it will represent.
        it must be in a form of ( array1, array2, array3 ) where arrays reoresent the game state as individual row  """
    def __init__(self, setup: list):
        self.grid = setup
        self.grid = np.array(self.grid, dtype='O')

    def spawn_from_first_layer(self):
        for i in self.grid:
            for j in i:
                if j != 0 and "x" and "o": #i.e there is a bead that can be placed
                    index_available_placement = np.where(self.grid == j)
                    tupled = zip(index_available_placement[0],index_available_placement[1]) # zip changes it to tuples of
                                                            # form (i, j) where i is row and j is index inside the row
                    for tuple in tupled:
                        print(f"this is current tuple: {tuple}\nfrom this list: {list(tupled)}")
                        new_grid = copy.deepcopy(self.grid) # creating a new grid where menace puts an x
                        new_grid[tuple[0]][tuple[1]] = "x"  #putting a new x
                        MB.boxtreeroot.append(Matchbox(new_grid))



                    # add some zeroes
                    # mb.boxtreeroot[-1].spawn() todo need to create a method that would spawn a grid with suitable amount of beads.

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
print(len(MB.boxtreeroot))
print(MB.boxtreeroot[0].grid)


