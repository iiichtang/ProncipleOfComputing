'''
listoflists = []
a_list = []
for i in range(0,10):
    a_list.append(i)
    if len(a_list)>3:
        a_list.remove(a_list[0])
        listoflists.append(list(a_list))
print listoflists
print listoflists[1]
print listoflists[1][1]



CELL_SIZE = 50
GRID_HEIGHT = 6
GRID_WIDTH = 9

for row in range(GRID_HEIGHT):
    for col in range(GRID_WIDTH):
        polygon = [[col * CELL_SIZE, row * CELL_SIZE],
                    [col * CELL_SIZE, (row + 1) * CELL_SIZE],
                    [(col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE],
                    [(col + 1) * CELL_SIZE, (row) * CELL_SIZE]]
        text_pos = [(col + 0.1) * CELL_SIZE, (row + 0.8) * CELL_SIZE]
        print polygon
        print text_pos




        width = 8
        height = 7
        row_list = []grid = []
        for dummy_row in range(self.height):
            for dummy_col in range(self.width):
                row_list.append(0)
            grid.append(list)
            row_list[:] = []
        print grid


        for dummy_num in range(2):
            row = random.randrange(0, width)
            col = random.randrange(0, height)
            value = self.new_tile()
            self.set_tile(row, col, value)

'''

"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    line2 = []
    line2.append(0)
    ptr = 0
    length_line = len(line)

    for length in range(length_line):

        if line[length] == 0:
            pass
        elif line2[ptr] == 0:
            line2[ptr] += line[length]
        elif line2[ptr] == line[length] :
            line2[ptr] += line[length]
            line2.append(0)
            ptr +=1
        else:
            line2.append(line[length])
            ptr += 1

    ptr +=1

    while ptr < length_line :
        line2.append(0)
        ptr +=1

    return line2

class TwentyFortyEight:
    """
    Class to run the game logic.
    """
    GRID_HEIGHT = 0
    GRID_WIDTH = 0
    grid = []

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.GRID_HEIGHT = grid_height
        self.GRID_WIDTH = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self.grid[:] = []
        local_width = self.get_grid_width()
        local_height = self.get_grid_height()
        row_list = []

        #print local_height, local_width

        for dummy_col in range(local_width):
            row_list.append(0)

        for dummy_row in range(local_height):
            self.grid.append(list(row_list))

        index_number = 0
        while index_number < 2:
            self.new_tile()
            index_number += 1


    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self.grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.GRID_HEIGHT

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.GRID_WIDTH

    def get_direction(self, direction):
        if direction == "UP" or direction == 1:
            direction = 1
        elif direction == "DOWN"  or direction == 2:
            direction = 2
        elif direction == "LEFT"  or direction == 3:
            direction = 3
        elif direction == "RIGHT"  or direction == 4:
            direction = 4
        return direction


    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        tile_move = 0
        local_list = []

        direction = self.get_direction(direction)

        if direction < 3:
            for grid_col in range(0, self.get_grid_width()):
                for grid_row in range(0,self.get_grid_height()):
                    local_list.append(self.get_tile(grid_row,grid_col))
                #print local_list
                if direction == 2:
                    local_list.reverse()
                    new_list = merge(local_list)
                    new_list.reverse()
                else:
                    new_list = merge(local_list)
                for grid_row in range(0,self.get_grid_height()):
                    if new_list[grid_row] != self.get_tile(grid_row,grid_col):
                        tile_move = 1
                    self.set_tile(grid_row,grid_col,new_list[grid_row])
                local_list[:] = []
            if tile_move == 1:
                self.new_tile()
        else:
            for grid_row in range(0,self.get_grid_height()):
                for grid_col in range(0, self.get_grid_width()):
                    local_list.append(self.get_tile(grid_row,grid_col))
                #print local_list
                if direction == 4:
                    local_list.reverse()
                    new_list = merge(local_list)
                    new_list.reverse()
                else:
                    new_list = merge(local_list)
                for grid_col in range(0,self.get_grid_width()):
                    if new_list[grid_col] != self.get_tile(grid_row,grid_col):
                        tile_move = 1
                    self.set_tile(grid_row,grid_col,new_list[grid_col])
                local_list[:] = []
            if tile_move == 1:
                self.new_tile()


    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        local_index = 0
        tile_range = random.randrange(0, 10)
        emp_ptr = 0

        for grid_col in range(0, self.get_grid_width()):
            for grid_row in range(0,self.get_grid_height()):
                if self.grid[grid_row][grid_col] == 0:
                    emp_ptr += 1

        index = random.randrange(1,emp_ptr + 1)

        for grid_col in range(0, self.get_grid_width()):
            for grid_row in range(0,self.get_grid_height()):
                if self.grid[grid_row][grid_col] == 0:
                    local_index += 1
                    if local_index == index:

                        #print emp_ptr,grid_row,grid_col,self.grid[grid_row][grid_col]
                        if tile_range > 0:
                            self.set_tile(grid_row,grid_col,2)
                            return None
                        else:
                            self.set_tile(grid_row,grid_col,4)
                            return None

        #print tile_range


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))