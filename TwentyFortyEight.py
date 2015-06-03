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
    grid_height = 0
    grid_width = 0
    grid = []

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()
        pass

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self.grid[:] = []
        self.empty_ptr = 0
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

        #print self.grid

        pass

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
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        tile_move = 0

        if direction == "UP":
            direction = 1
        elif direction == "DOWN":
            direction = 2
        elif direction == "LEFT":
            direction = 3
        elif direction == "RIGHT":
            direction = 4

        local_list = []
        if direction == UP:
            for i in range(0, self.get_grid_width()):
                for j in range(0,self.get_grid_height()):
                    local_list.append(self.get_tile(j,i))
                #print local_list
                new_list = merge(local_list)
                for j in range(0,self.get_grid_height()):
                    if new_list[j] != self.get_tile(j,i):
                        tile_move = 1
                    self.set_tile(j,i,new_list[j])
                local_list[:] = []
            if tile_move == 1:
                self.new_tile()
            pass
        elif direction == DOWN:
            for i in range(0, self.get_grid_width()):
                for j in range(0,self.get_grid_height()):
                    local_list.append(self.get_tile(j,i))
                #print local_list
                local_list.reverse()
                new_list = merge(local_list)
                new_list.reverse()
                for j in range(0,self.get_grid_height()):
                    if new_list[j] != self.get_tile(j,i):
                        tile_move = 1
                    self.set_tile(j,i,new_list[j])
                local_list[:] = []
            if tile_move == 1:
                self.new_tile()
            pass
        elif direction == 3:
            for j in range(0,self.get_grid_height()):
                for i in range(0, self.get_grid_width()):
                    local_list.append(self.get_tile(j,i))
                #print local_list
                new_list = merge(local_list)
                for i in range(0,self.get_grid_width()):
                    if new_list[i] != self.get_tile(j,i):
                        tile_move = 1
                    self.set_tile(j,i,new_list[i])
                local_list[:] = []
            if tile_move == 1:
                self.new_tile()
            pass
        elif direction == 4:
            for j in range(0,self.get_grid_height()):
                for i in range(0, self.get_grid_width()):
                    local_list.append(self.get_tile(j,i))
                #print local_list
                local_list.reverse()
                new_list = merge(local_list)
                new_list.reverse()
                for i in range(0,self.get_grid_width()):
                    if new_list[i] != self.get_tile(j,i):
                        print j,i,new_list[i],self.get_tile(j,i)
                        tile_move = 1
                    self.set_tile(j,i,new_list[i])
                local_list[:] = []
            if tile_move == 1:
                self.new_tile()
            pass
        else:
            pass

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

        for i in range(0, self.get_grid_width()):
            for j in range(0,self.get_grid_height()):
                if self.grid[j][i] == 0:
                    emp_ptr += 1

        index = random.randrange(1,emp_ptr + 1)

        for i in range(0, self.get_grid_width()):
            for j in range(0,self.get_grid_height()):
                if self.grid[j][i] == 0:
                    local_index += 1
                    if local_index == index:

                        print emp_ptr,j,i,self.grid[j][i]
                        if tile_range > 0:
                            self.set_tile(j,i,2)
                            pass
                        else:
                            self.set_tile(j,i,4)
                            pass

        #print tile_range


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self.grid[row][col] = value
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))