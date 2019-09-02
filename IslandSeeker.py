import time

input_file = open('Matrix.txt', 'r')
analyzed_file = input_file.readlines() # [6:]  creates a new list in which each verse is an element.
# Skips 6 header lines (In Esri grid data, the first six lines indicate the reference of the grid)
input_file.close()

elevation_array = []  # a new list that will contain converted (float) values from the input_file
data_converter = []

'''
The code retrieves each line from the input_file, splits the content into elements and converts to float points
'''

for each_row in analyzed_file:
    separated_verse = each_row.split()  # each element (row) of the analyzed_file list becomes a set of elements
    for each_cell in separated_verse:
        data_converter.append(float(each_cell))  # converts each element to a floating point and adds to the
        # new list
    elevation_array.append(data_converter)

del analyzed_file
del data_converter

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

base_cell = []  # creates an empty list with a cell that is checked for adjacent valid cells
# number_of_islands = 0 counts the number of continuous areas with valid cells
number_of_cells = 0  # counts the total number of valid cells

vertical_length = len(elevation_array[0])  # checks how many items are in a row
horizontal_length = len(elevation_array)  # checks total number of rows

for horizontal_position in range(horizontal_length):
    for vertical_position in range(vertical_length):
        if elevation_array[horizontal_position][vertical_position] == 'rejected' \
                or elevation_array[horizontal_position][vertical_position] == 'approved':
            pass
        else:
            if lower_boundary_condition > elevation_array[horizontal_position][vertical_position]:
                elevation_array[horizontal_position][vertical_position] = 'rejected'
            elif upper_boundary_condition < elevation_array[horizontal_position][vertical_position]:
                elevation_array[horizontal_position][vertical_position] = 'rejected'
            else:
                elevation_array[horizontal_position][vertical_position] = 'approved'
                base_cell.append((horizontal_position, vertical_position))
                number_of_cells += 1

print(number_of_cells)

time.sleep(3)
