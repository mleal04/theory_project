from ast import main
import time
import matplotlib.pyplot as plt
import csv

# Read CSV file
def read_csv(csv_input):
    graphs = []
    graph = None

    with open(csv_input, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)

        for line in csv_reader:
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

# Find all Hamiltonian cycles of the graph
def find_hamiltonian_cycle(graph, start_vertex, path):
    if len(path) == graph['vertices']:
        if start_vertex in graph[path[-1]]:
            return path + [start_vertex]  # Return the cycle including the start vertex
    
    # Recursive case
    for neighbor in graph[path[-1]]:
        if neighbor not in path: 
            cycle = find_hamiltonian_cycle(graph, start_vertex, path + [neighbor])
            if cycle:  # If a cycle is found, return it
                return cycle
    
    return False  # no cycle found

# Input data
graphs = read_csv('check_ham_cycle_MNO.csv')
times = []
results = []
num_vertices = []

# Loop through all graphs
for index, graph in enumerate(graphs, 1):
    total_execution_time = 0
    found_cycle = False
    cycle_path = None  
    # Search for Hamiltonian cycles from each vertex
    for start_vertex in graph.keys():
        if start_vertex not in ['type', 'vertices', 'edges']:
            # Track the time it takes to find a cycle
            start_time = time.perf_counter()
            
            cycle_path = find_hamiltonian_cycle(graph, start_vertex, [start_vertex])
            if cycle_path:
                found_cycle = True
                
                end_time = time.perf_counter()
                execution_time = end_time - start_time
                total_execution_time += execution_time
                break  # Stop searching after finding the first cycle
            end_time = time.perf_counter()
            total_execution_time += (end_time - start_time)

    # Print
    if found_cycle:
        print(f"Graph {index}: Hamiltonian cycle found")
        print(f"Hamiltonian Cycle: {cycle_path}")
        results.append(True)
    else:
        print(f"Graph {index}: No Hamiltonian cycle")
        results.append(False)

    print(f'Execution Time: {total_execution_time:.4f} seconds')
    print()

    times.append(total_execution_time)
    num_vertices.append(graph['vertices'])

# Create time graph
colors = ['green' if result else 'red' for result in results] # color code

plt.scatter(num_vertices, times, c=colors)
plt.xlabel('Size (Number of Vertices)')
plt.ylabel('Time (Seconds)')
plt.title('Hamiltonian Cycle Detection: Size vs Time')
plt.show()
