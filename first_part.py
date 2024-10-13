from ast import main
import time
import matplotlib.pyplot as plt
import csv
''' traveling salesmen problem '''

#read csv file --> make the graph directed even if it comes as undirected
def read_csv(csv_input):
    graphs = []
    graph = None

    with open(csv_input, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)

        for line in csv_reader:
          if line[0] == 'p':  
            if graph is not None:
                graphs.append(graph)  #add the previous graph to the list
            #create new graph
            graph = {'type': line[1], 'vertices': int(line[2]), 'edges': []}  
          elif line[0] == 'v':  
            vertex = line[1]
            if vertex not in graph:
                graph[vertex] = []
          elif line[0] == 'e': 
            source = line[1]
            target = line[2]
            #weight = float(line[3])
            graph[source].append(target)  #add directed edge
            if graph['type'] == 'u':  #if graph is undirected, add reverse edge
                graph[target].append(source)
            graph['edges'].append((source, target))
    
    if graph is not None:
        graphs.append(graph)
    
    return graphs

#find the hamiltonian path of a graph ending at a specific vertex 
def find_hamiltonian_path(graph, start_vertex, end_vertex, path):
    #base case, it has gone through all vertices
    if len(path) == graph['vertices']:
      # check if it ends at the correct vertex
      if path[-1] == end_vertex:
        return path
      return None
    #recursive case
    for neighbor in graph[start_vertex]:
        if neighbor not in path:
            path.append(neighbor)
            result = find_hamiltonian_path(graph, neighbor, end_vertex, path)
            if result is not None: 
                return result
            path.pop() # backtracking 

    return None # for no path found 




#make the graph --> list of graphs
graphs = read_csv('ham_path_graph_data.csv')

times = []
sizes = []

#loop through all graphs 
for index, graph in enumerate(graphs, 0):
    #create path and sum
    path = []

    #get the startig vertex (we need this list)
    start_vertex = list(graph.keys())[3]
    #get the end vertex (we need this list)
    end_vertex = list(graph.keys())[4]
    #append start vertext in the graph
    path.append(start_vertex)

    # Find Hamiltonian Path 
    start_time = time.time()
    ham_path = find_hamiltonian_path(graph, start_vertex, end_vertex, path)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution Time:", execution_time, "seconds")
    print()
    print(f"TSP Instance {index + 1}:")

    times.append(execution_time)
    sizes.append(graph['vertices'])

    if ham_path: 
        print("Hamiltonian Path:", ham_path)
    else:
        print("No Hamiltonian Path Found")
      
    print()
print(times)
print(sizes)

#create the time graph
plt.plot(sizes, times, 'o')  
plt.xlabel('Size') 
plt.ylabel('Time')
plt.title('Size vs Time for Hamiltonian Path')  
plt.show()