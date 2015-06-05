"""
Clone of 2048 game.
code for project 2
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
    merged_line = [0]
    line_ptr = 0

    for length in range(len(line)):
        if line[length] == 0:
            pass
        elif merged_line[line_ptr] == 0:
            merged_line[line_ptr] += line[length]
        elif merged_line[line_ptr] == line[length]:
            merged_line[line_ptr] += line[length]
            merged_line.append(0)
            line_ptr += 1
        else:
            merged_line.append(line[length])
            line_ptr += 1

    line_ptr += 1

    while line_ptr < len(line):
        merged_line.append(0)
        line_ptr += 1

    return merged_line


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # set height, width, grid
        self._tfe_grid_height = grid_height
        self._tfe_grid_width = grid_width
        self._tfe_grid = []
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._tfe_grid = [[0 for dummy_col in range(self.get_grid_width())]
                          for dummy_row in range(self.get_grid_height())]
        # create a grid_height by grid_width grid with value 0

        for dummy_index in range(0, 2):
            self.new_tile()
        # add 2 tiles with non-zero value

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._tfe_grid)
        # print the entire grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._tfe_grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._tfe_grid_width

    def get_direction(self, direction):
        """
        Transform the direction into number
        """
        if direction == "UP" or direction == 1:
            direction = UP
        elif direction == "DOWN" or direction == 2:
            direction = DOWN
        elif direction == "LEFT" or direction == 3:
            direction = LEFT
        elif direction == "RIGHT" or direction == 4:
            direction = RIGHT
        return direction

    def traverse_grid(self, start_cell, direction, num_steps):
        """
        Function that iterates through the cells in a grid
        in a linear direction

        Both start_cell is a tuple(row, col) denoting the
        starting cell

        direction is a tuple that contains difference between
        consecutive cells in the traversal
        """
        local_list = []
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]

            local_list.append(self._tfe_grid[row][col])

        new_list = merge(local_list)
        tile_move = 0

        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]

            if self._tfe_grid[row][col] != new_list[step]:
                tile_move = 1
            self._tfe_grid[row][col] = new_list[step]

        return tile_move
        # return 1 if ant tile moved

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        local_width = self.get_grid_width()
        local_height = self.get_grid_height()
        tile_move = 0
        # verify if any tile move

        direction = self.get_direction(direction)

        if direction == UP:
            for grid_col in range(0, local_width):
                tile_move += self.traverse_grid((0, grid_col),
                                                OFFSETS[direction], local_height)
        elif direction == DOWN:
            for grid_col in range(0, local_width):
                tile_move += self.traverse_grid((local_height - 1, grid_col),
                                                OFFSETS[direction], local_height)
        elif direction == LEFT:
            for grid_row in range(0, local_height):
                tile_move += self.traverse_grid((grid_row, 0),
                                                OFFSETS[direction], local_width)
        elif direction == RIGHT:
            for grid_row in range(0, local_height):
                tile_move += self.traverse_grid((grid_row, local_width - 1),
                                                OFFSETS[direction], local_width)

        if tile_move > 0:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        emp_ptr = 0
        emp_list = []

        for grid_row in range(0, self.get_grid_height()):
            for grid_col in range(0, self.get_grid_width()):
                if self._tfe_grid[grid_row][grid_col] == 0:
                    emp_list.append([grid_row, grid_col])
                    emp_ptr += 1
        # count the total number of 0
        # put all (row,col) pairs with value 0 into the emp_list

        index = random.randrange(0, emp_ptr)
        tile_range = random.randrange(0, 10)

        if tile_range > 0:
            self.set_tile(emp_list[index][0], emp_list[index][1], 2)
            return None
        else:
            self.set_tile(emp_list[index][0], emp_list[index][1], 4)
            return None
        # if tile_range = 1-9, set value to 2 (90%)
        # if tile_range = 0, set value to 4 (10%)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._tfe_grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._tfe_grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
