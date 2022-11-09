import random, pickle, numpy as np, copy


class Matchbox:
    """ this class takes 2 dimensional array as an representation of game state which it will represent.
        it must be in a form of ( array1, array2, array3 ) where arrays reoresent the game state as individual row  """
    def __init__(self, setup: list, parent_nodes: list, children_nodes: list):
        self.grid = setup
        self.grid = np.array(self.grid, dtype='O')
        self.parent_nodes = []
        self.children_nodes = []

    def spawn_from_first_layer(self):
        for i in self.grid:
            for j in i:
                if j != 0 and "x" and "o": #i.e there is a bead that can be placed
                    index_available_placement = np.where(self.grid == j)
                    tupled = zip(index_available_placement[0],index_available_placement[1]) # zip changes it to tuples of
                                                            # form (i, j) where i is row and j is index inside the row
        for tuple in list(tupled):
            new_grid = copy.deepcopy(self.grid) # creating a new grid where menace puts an x
            new_grid[tuple[0]][tuple[1]] = "x"  #putting a new x
            MB.boxtreeroot.children_nodes.append(Matchbox(new_grid, MB.boxtreeroot, []))

    def spawn_from_second_layer(self):
        for current_state in MB.boxtreeroot:
            if "x" in current_state.grid:
                pass

    def place_a_bead(self):
        available_places = []
        for i in self.grid:
            for j in i:
                if j != 0 or "x" or "o":
                    available_places.append([i, j])
        print(available_places)

    def Player_placing_a_bead(self):
        Failed = True
        while Failed == True:
            print(f"\n\nHere is the current grid! \n{self.grid}")
            position = input("please enter coordinates for your choice\n"
                             "Make sure you put them in a 'x,y' (without quotation marks and no larger than 2, start from 0)"
                             " format wherex is a row and y is a column ") #TODO put try, except ValueError catch
            position = tuple(int(x) for x in position.split(","))
            print(position)
            if self.grid[position[0]][position[1]] != "x":
                self.grid[position[0]][position[1]] = "o"
                print(self.grid)
                Failed = False

    def put_nodes_everywhere(self):
        i = -1
        for row in self.grid:
            i += 1
            j = -1
            for column in row:
                j += 1
                if column != 'x' and 'o':
                    new_grid = copy.deepcopy(self.grid)
                    new_grid[i][j]
                    self.children_nodes.append(new_grid)
                else:
                    pass


    def spawn_from_second_layer(self):
            pass
        #for current_state in MB.boxtreeroot.children_nodes:
        #    for row in range(len(current_state.grid))
        #        for column in row:
        #            if column != 'x' or 'o'


    def spawn_from_third_layer(self):
        pass

    def spawn_from_forth_layer(self):
        pass

    def rotate(self):
        self.grid = np.fliplr(np.array(self.grid).T.tolist())
        return self.grid

    def check_if_duplicate(self, grid, array):
        for i in range(4):
            if grid.rotate() in array:
                return True


class Matchboxes:
    """ this is a object which is basically an array which can be accessed inside the matchbox class"""
    def __init__(self):
        self.boxtreeroot = Matchbox([[8, 8, 0], [0, 8, 0], [0, 0, 0]], None, []) #a starting game state which is never changed.


MB = Matchboxes()
MB.boxtreeroot.spawn_from_first_layer()
print(MB.boxtreeroot.grid)
print(MB.boxtreeroot.children_nodes[0].grid)
print(MB.boxtreeroot.children_nodes[1].grid)
print(MB.boxtreeroot.children_nodes[2].grid)
MB.boxtreeroot.children_nodes[0].put_nodes_everywhere()
print(len(MB.boxtreeroot.children_nodes[0].children_nodes))
