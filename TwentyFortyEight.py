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
    height = 0
    width = 0
    grid = []
    

    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        width = self.get_grid_width()
        height = self.get_grid_height()
        row_list = []
        
        print width,height
        
        for dummy_col in range(width):
            row_list.append(0)
        
        for dummy_row in range(height):
            self.grid.append(list(row_list))

        for dummy_num in range(0,2):
            row = random.randrange(0, height)
            col = random.randrange(0, width)
            value = self.new_tile()
            self.set_tile(row, col, value)
        print self.grid
        
        return 0
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code

        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        #print ""
        tile_range = random.randrange(0, 10)
        #print tile_range
        if tile_range > 0:
            #print "2"
            return 2
        else:
            #print "4"
            return 4

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self.grid[row][col] = value
        return 0

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self.grid[row][col]

    

poc_2048_gui.run_gui(TwentyFortyEight(5, 4))
