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

import random

emp_ptr = 0
emp_list = []

tfe_grid = [[0 for dummy_col in range(4)]
                           for dummy_row in range(5)]

for grid_col in range(0, 4):
    for grid_row in range(0,5):
        if tfe_grid[grid_row][grid_col] == 0:
            emp_list.append([grid_row, grid_col])
            emp_ptr += 1

index = random.randrange(0,emp_ptr)

tile_range = random.randrange(0, 10)

tfe_grid[emp_list[index][0]][emp_list[index][1]] = tile_range

print tile_range,index
print emp_list[index][0],emp_list[index][1]
print
print tfe_grid