from ast import main
import time
import matplotlib.pyplot as plt

# read csv file
def read_csv(csv_input):
    graphs = []
    graph = None

    with open(csv_input, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)

        for line in csv_reader:
          if line[0] == 'p':  
            if graph is not None:
                graphs.append(graph)  # add the previous graph to the list
            # create new graph
            graph = {'type': line[1], 'vertices': int(line[2]), 'edges': []}  
          elif line[0] == 'v':  
              vertex = line[1]
              if vertex not in graph:
                  graph[vertex] = []
          elif line[0] == 'e': 
              source = line[1]
              target = line[2]
              graph[source].append(target)  # add directed edge
              if graph['type'] == 'u':  # if graph is undirected, add reverse edge
                  graph[target].append(source)
              graph['edges'].append((source, target))
      
    if graph is not None:
        graphs.append(graph)
    
    return graphs

# Find all Hamiltonian cycles of the graph
def find_hamiltonian_cycles(graph, start_vertex, path, cycles):
    # Base case: if the path includes all vertices and can return to the start vertex
    if len(path) == graph['vertices']:
        if start_vertex in graph[path[-1]]:
            cycles.append(path + [start_vertex])  # add cycle including the start vertex
        return

    # Recursive case
    for neighbor in graph[path[-1]]:
        if neighbor not in path:  # proceed if neighbor is not already in the path
            find_hamiltonian_cycles(graph, start_vertex, path + [neighbor], cycles)

# Input data
graphs = read_csv('graphs2.csv')
times = []
num_cycles = []
num_vertices = []

# Loop through all graphs 
for index, graph in enumerate(graphs,1):
    total_execution_time = 0 
    cycles = []
    # search for Hamiltonian cycles from each vertex
    for start_vertex in graph.keys():
        if start_vertex not in ['type', 'vertices', 'edges']: 
            # track the time it takes to find all cycles
            start_time = time.time()
            find_hamiltonian_cycles(graph, start_vertex, [start_vertex], cycles)
            end_time = time.time()
            execution_time = end_time - start_time
            total_execution_time += execution_time

    # print
    print(f"Hamiltonian Cycles for graph {index}:")
    for cycle in cycles:
        print(",".join(map(str, cycle)))
    print(f'Execution Time: {execution_time}')
    print(f'Number of Cycles: {len(cycles)}')
    print()
    num_cycles.append(len(cycles))
    times.append(total_execution_time)
    num_vertices.append(graph['vertices'])

# create time graph
plt.plot(num_vertices, times, 'o')  
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Size vs Time')  
plt.show()


