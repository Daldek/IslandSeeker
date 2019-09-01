input_file = open('E:\OneDrive\Dokumenty\Inne\pyton\IslandSeeker\IslandSeeker\Matrix2.txt', 'r')
analyzed_file = input_file.readlines()[1:]  # creates a new list in which each verse is an element
input_file.close()

elevation_matrix = []

for each_verse in analyzed_file:
    separated_verse = each_verse.split()  # each element (verse) of the analyzed_file list becomes a set of elements
    data_conventer = []
    for each_cell in separated_verse:
        data_conventer.append(float(each_cell))  # converts each element to a floating point and adds to the
        # new list
    elevation_matrix.append(data_conventer)

while True:
    try:
        lower_boundary_condition = float(input("Insert the value of the lower boundary condition "))
        upper_boundary_condition = float(input("Insert the value of the upper boundary condition "))
        break
    except ValueError:
        print("wrong data type")

discoverer = []  # creates an empty list with cells that do not yet have neighbors
number_of_islands = 0  # this variable counts the number of founded islands
number_of_cells = 0

vertical_length = len(elevation_matrix[0])
horizontal_length = len(elevation_matrix)

for horizontal_movement in range(horizontal_length):
    for vertical_movement in range(horizontal_length):
        if elevation_matrix[horizontal_movement][vertical_movement] == 'rejected' \
                or elevation_matrix[horizontal_movement][vertical_movement] == 'approved':
            pass
        else:
            if lower_boundary_condition > elevation_matrix[horizontal_movement][vertical_movement]:
                elevation_matrix[horizontal_movement][vertical_movement] = 'rejected'
            elif upper_boundary_condition < elevation_matrix[horizontal_movement][vertical_movement]:
                elevation_matrix[horizontal_movement][vertical_movement] = 'rejected'
            else:
                elevation_matrix[horizontal_movement][vertical_movement] = 'approved'
                discoverer.append((horizontal_movement, vertical_movement))
                number_of_islands += 1

print(number_of_islands)
