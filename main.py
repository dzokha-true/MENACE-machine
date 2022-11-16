import random, pickle, numpy as np, copy


class Matchbox:
    """ this class takes 2 dimensional array as an representation of game state which it will represent.
        it must be in a form of ( array1, array2, array3 ) where arrays reoresent the game state as individual row  """
    def __init__(self, setup: list, parent_nodes: list, children_nodes: list):
        self.grid = setup
        self.grid = np.array(self.grid, dtype='O')
        self.parent_nodes = []
        self.children_nodes = []

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
                    new_grid[i][j] = 'o'
                    # self.children_nodes.append(Matchbox(new_grid, self, None))
                    #TODO change the line above so that it is not a new layer in the tree but actually appended to the
                    # same layer deleting the one wher ethere is no nodes everywhere
                else:
                    pass

    def spawn_second_layer(self):
        for i in self.grid:
            for j in i:
                if j != 0 and "x" and "o": #i.e there is a bead that can be placed
                    index_available_placement = np.where(self.grid == j)
                    tupled = zip(index_available_placement[0],index_available_placement[1]) # zip changes it to tuples of
                                                            # form (i, j) where i is row and j is index inside the row
        for tuple in list(tupled):
            new_grid = copy.deepcopy(self.grid) # creating a new grid where menace puts an x
            new_grid[tuple[0]][tuple[1]] = "x"  #putting a new x
            i = -1
            for row in new_grid:
                i += 1
                j = -1
                for column in row:
                    # break
                    j += 1
                    if column != 'x':
                        new_grid[i][j] = 4
                    else:
                        pass
            MB.boxtreeroot.children_nodes.append(Matchbox(new_grid, MB.boxtreeroot, []))
        for current_state in MB.boxtreeroot.children_nodes:
            current_state.put_nodes_everywhere()
            #todo make sure that those current state put nodes everywhere don't go into children nodes but actuallt change the current state itself.

    def spawn_third_layer(self):
        i = 0
        for i in range(len(MB.boxtreeroot.children_nodes)):
            for current_state in MB.boxtreeroot.children_nodes[i].children_nodes:
                i = -1
                for row in current_state.grid:
                    i += 1
                    j = -1
                    for column in row:
                        j+=1
                        if column != "o" and column != "x":     #puts x
                            new_grid = copy.deepcopy(current_state.grid)
                            new_grid[i][j] = "x"

                            k = -1
                            for row in new_grid:    # changes 4s to 2s
                                x = -1
                                k +=1
                                for column in row:
                                    x+=1
                                    if column != "x" and column != "o":
                                        new_grid[k][x] = 2
                            current_state.children_nodes.append(Matchbox(new_grid, current_state, None))
        #todo put an o, also make sure that o's are there before you append new grid to children nodes of matchbox



        # for parent_state in MB.boxtreeroot.children_nodes:
        #     for current_state in parent_state:
        #         pass





    def spawn_forth_layer(self):
        pass

    def spawn_fifth_layer(self):
        pass

    def rotate(self):
        self.grid = np.fliplr(np.array(self.grid).T.tolist())
        return self.grid

    def check_if_duplicate(self, grid, array):
        for i in range(4):
            if grid.rotate() in array:
                return True

    def summon_the_machine(self):
        self.spawn_second_layer()
        self.spawn_third_layer()
        self.spawn_forth_layer()
        self.spawn_fifth_layer()


class Matchboxes:
    """ this is a object which is basically an array which can be accessed inside the matchbox class"""
    def __init__(self):
        self.boxtreeroot = Matchbox([[8, 8, 0], [0, 8, 0], [0, 0, 0]], None, []) #a starting game state which is never changed.


MB = Matchboxes()
MB.boxtreeroot.summon_the_machine()
# for i in range(3):
#     for hehe in range(8):
#         print(MB.boxtreeroot.children_nodes[i].children_nodes[hehe])

for i in MB.boxtreeroot.children_nodes:
    for j in i.children_nodes:
        for k in j.children_nodes:
            print(k.grid)