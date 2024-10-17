# create csv file
import csv

csv_input = [
    ['c', 1, 'TSP Instance 1'],
    ['p', 'u', 4, 6],
    ['v', 1],
    ['v', 2],
    ['v', 3],
    ['v', 4],
    ['e', 1, 2],
    ['e', 1, 3],
    ['e', 2, 3],
    ['e', 2, 4],
    ['e', 3, 4],
    ['e', 1, 4],

    ['c', 2, 'TSP Instance 2'],
    ['p', 'u', 5, 8],
    ['v', 1],
    ['v', 2],
    ['v', 3],
    ['v', 4],
    ['v', 5],
    ['e', 1, 2],
    ['e', 1, 3],
    ['e', 2, 3],
    ['e', 3, 4],
    ['e', 4, 5],
    ['e', 5, 1],
    ['e', 2, 5],
    ['e', 4, 2],

    ['c', 3, 'TSP Instance 3'],
    ['p', 'u', 3, 3],
    ['v', 1],
    ['v', 2],
    ['v', 3],
    ['e', 1, 2],
    ['e', 2, 3],
    ['e', 3, 1],

    ['c', 4, 'TSP Instance 4'],
    ['p', 'u', 6, 9],
    ['v', 1],
    ['v', 2],
    ['v', 3],
    ['v', 4],
    ['v', 5],
    ['v', 6],
    ['e', 1, 2],
    ['e', 1, 3],
    ['e', 2, 4],
    ['e', 3, 5],
    ['e', 4, 6],
    ['e', 5, 1],
    ['e', 2, 3],
    ['e', 3, 4],
    ['e', 5, 2],
    ['e', 6, 1],

    ['c', 5, 'TSP Instance 5'],
    ['p', 'u', 7, 10],
    ['v', 1],
    ['v', 2],
    ['v', 3],
    ['v', 4],
    ['v', 5],
    ['v', 6],
    ['v', 7],
    ['e', 1, 2],
    ['e', 1, 3],
    ['e', 2, 4],
    ['e', 3, 5],
    ['e', 4, 6],
    ['e', 5, 7],
    ['e', 6, 1],
    ['e', 2, 3],
    ['e', 3, 4],
    ['e', 6, 4],
    ['e', 5, 1],

    ['c', 6, 'TSP Instance 6'],
    ['p', 'u', 8, 12],
    ['v', 1],
    ['v', 2],
    ['v', 3],
    ['v', 4],
    ['v', 5],
    ['v', 6],
    ['v', 7],
    ['v', 8],
    ['e', 1, 2],
    ['e', 1, 3],
    ['e', 2, 4],
    ['e', 3, 5],
    ['e', 4, 6],
    ['e', 5, 7],
    ['e', 6, 8],
    ['e', 7, 1],
    ['e', 2, 5],
    ['e', 3, 4],
    ['e', 6, 2],
    ['e', 8, 3],
    ['e', 4, 1],
]

filename = 'graphs2.csv'

# writing to csv file 
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # write each row from the data list
    writer.writerows(csv_input)

