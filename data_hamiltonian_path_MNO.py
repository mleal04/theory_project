from ast import main
import time
import matplotlib.pyplot as plt
import csv

# Read CSV file to make the graph directed
def read_csv(csv_input):
    graphs = []
    graph = None

    with open(csv_input, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)

        for line in csv_reader:
            if not line:
                continue
            if line[0] == 'p':
                if graph is not None:
                    graphs.append(graph)  # Add the previous graph to the list
                # Create new graph
                graph = {'type': line[1], 'vertices': int(line[2]), 'edges': []}
            elif line[0] == 'v':
                vertex = line[1]
                if vertex not in graph:
                    graph[vertex] = []
            elif line[0] == 'e':
                source = line[1]
                target = line[2]
                graph[source].append(target)  # Add directed edge
                if graph['type'] == 'u':  # If graph is undirected, add reverse edge
                    graph[target].append(source)
                graph['edges'].append((source, target))

    if graph is not None:
        graphs.append(graph)

    return graphs

# Find the Hamiltonian path of a graph
def find_hamiltonian_path(graph, current_vertex, path):
    # base case, it has gone through all vertices
    if len(path) == graph['vertices']:
        return path  # return the path if all vertices are included

    # recursive case
    for neighbor in graph[current_vertex]:
        if neighbor not in path:  # only visit unvisited vertices
            path.append(neighbor)
            result = find_hamiltonian_path(graph, neighbor, path)
            if result is not None:
                return result
            path.pop()  # backtracking

    return None  # if no path found

# Make the graph --> list of graphs
graphs = read_csv('first_part_graph_data.csv')

times = []
sizes = []

# Loop through all graphs
for index, graph in enumerate(graphs, 0):
    vertices = [v for v in graph.keys() if v not in ['type', 'vertices', 'edges']] 

    # attempting to find hamiltonian path from any start vertex in the graph
    found_path = None
    for start_vertex in vertices:
        path = [start_vertex]  # the start path with the current vertex

        # Find Hamiltonian Path
        start_time = time.time()
        ham_path = find_hamiltonian_path(graph, start_vertex, path)  
        end_time = time.time()
        execution_time = end_time - start_time

        if ham_path:
            found_path = ham_path
            times.append(execution_time)
            sizes.append(graph['vertices'])
            break  # exit search if a path is found

    print(f"TSP Instance {index + 1}:")
    print("Execution Time:", execution_time, "seconds")

    if found_path:
        print("Hamiltonian Path:", found_path)
    else:
        print("No Hamiltonian Path Found")

    print()

# Create the time graph
plt.plot(sizes, times, 'o')
plt.xlabel('Size (number of vertices)')
plt.ylabel('Execution Time')
plt.title('Size vs Time for Hamiltonian Path')
plt.show()
