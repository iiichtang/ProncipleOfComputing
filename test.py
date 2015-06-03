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

array=[0,10,20,40]
for i in reversed(array):
    print i
array.reverse()
print array