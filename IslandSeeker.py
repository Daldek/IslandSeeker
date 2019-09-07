import time

input_file = open('Matrix.txt', 'r')
analyzed_file = input_file.readlines() # [6:]  creates a new list in which each verse is an element.
# Skips 6 header lines (In Esri grid data, the first six lines indicate the reference of the grid)
input_file.close()

elevation_array = []  # a new list that will contain converted (float) values from the input_file

'''
The code retrieves each line from the input_file, splits the content into elements and converts to float points
'''

for each_row in analyzed_file:
    separated_verse = each_row.split()  # each element (row) of the analyzed_file list becomes a set of elements
    data_converter = []
    for each_cell in separated_verse:
        data_converter.append(float(each_cell))  # converts each element to a floating point and adds to the
        # new list
    elevation_array.append(data_converter)

del analyzed_file

'''
The code retrieves the upper and lower boundary condition values and checks whether the data type is valid
'''

while True:
    try:
        lower_boundary_condition = float(input("Insert the value of the lower boundary condition "))
        upper_boundary_condition = float(input("Insert the value of the upper boundary condition "))
        break
    except ValueError:
        print("Wrong data type")

'''
Main part of the script. Values are checked cell by call until the correct value is found. Subsequently the surrounding
cells are checked.
'''

base_cells = []  # creates an empty list with cells that is checked for adjacent valid cells
number_of_islands = 0  # counts the number of continuous areas with valid cells
number_of_cells = 0  # counts the total number of valid cells

horizontal_length = len(elevation_array[0])  # checks how many items are in a row
vertical_length = len(elevation_array)  # checks total number of rows

for vertical_position in range(vertical_length):
    for horizontal_position in range(horizontal_length):
        if elevation_array[vertical_position][horizontal_position] == 'rejected' or\
                elevation_array[vertical_position][horizontal_position] == 'approved':
            pass  # this cell has already been checked
        else:
            if lower_boundary_condition > elevation_array[vertical_position][horizontal_position] or\
                    upper_boundary_condition < elevation_array[vertical_position][horizontal_position]:
                elevation_array[vertical_position][horizontal_position] = 'rejected'
            else:
                elevation_array[vertical_position][horizontal_position] = 'approved'
                base_cells.append((vertical_position, horizontal_position))
                number_of_islands += 1
                number_of_cells += 1
                while base_cells != []:
                    base_cell = base_cells[0]
                    base_cells.remove(base_cell)
                    adjacent_cells = [(base_cell[0]-1, base_cell[1]), (base_cell[0]+1, base_cell[1]),\
                                      (base_cell[0], base_cell[1]-1), (base_cell[0], base_cell[1]+1)]
                    for cell in adjacent_cells:
                        y = cell[0]
                        x = cell[1]
                        if y < 0 or y >= vertical_length or x < 0 or x >= horizontal_length:
                            pass
                        elif elevation_array[y][x] == 'rejected' or elevation_array[y][x] == 'approved':
                            pass
                        else:
                            if lower_boundary_condition > elevation_array[y][x] or\
                                    upper_boundary_condition < elevation_array[y][x]:
                                elevation_array[y][x] = 'rejected'
                            else:
                                elevation_array[y][x] = 'approved'
                                base_cells.append((y, x))
                                number_of_cells += 1

print("Number of appropriate cells: " + str(number_of_cells))
print("Number of islands: " + str(number_of_islands))

time.sleep(3)
