from ast import main
import time
import matplotlib.pyplot as plt
import csv

''' traveling salesmen problem '''
OUTPUT_FILE = 'output_TSP.txt'

#read csv file --> make the graph directed even if it comes as undirected
def read_csv(csv_input_path):
    graphs = []
    graph = None
    
    #open and read the CSV file
    with open(csv_input_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)

        for line in csv_reader:
            if line[0] == 'p':  
                if graph is not None:
                    graphs.append(graph)  
                graph = {'type': line[1], 'vertices': int(line[2]), 'edges': []}  
            elif line[0] == 'v':  
                vertex = line[1]
                if vertex not in graph:
                    graph[vertex] = []
            elif line[0] == 'e':  
                source = line[1]
                target = line[2]
                weight = float(line[3])
                
                if source not in graph:
                    graph[source] = []
                graph[source].append((target, weight))  
                
                graph['edges'].append((source, target, weight))
    
    if graph is not None:
        graphs.append(graph)
    
    return graphs

#find the hamiltonian cycle of the graph
def find_hamiltonian_cycle(graph, start_vertex, path, sum_path, main_sum, best_path_sum):
    #base case
    if len(path) == graph['vertices']:
        for neighbor, weight in graph[start_vertex]:
            if neighbor == path[0]:  #find the way back to the start
                total_sum = sum_path + weight  #add the way back to the path
                if total_sum < main_sum[0]:
                    main_sum[0] = total_sum
                    best_path_sum[0] = path + [path[0]] #add the 1 at the back again
        return

    #recursive case
    for neighbor, weight in graph[start_vertex]:
        if neighbor not in path:
            path.append(neighbor)
            sum_path += weight
            find_hamiltonian_cycle(graph, neighbor, path, sum_path, main_sum, best_path_sum)
            path.pop()
            sum_path -= weight

    return path, sum_path

def hamiltonian_cycle_output(hamiltonian_cycle,exec_time,graph):
    with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
        f.write(f"Graph: {graph}\n")
        f.write(f"Hamiltonian Cycle Path: {hamiltonian_cycle[0]}\n")
        f.write(f"Length of Cycle: {hamiltonian_cycle[1]}\n")
        f.write(f"Execution Time: {exec_time} seconds\n")
        f.write("\n")

#make the graph --> list of graphs
graphs = read_csv('graphs.csv')

times = []
sizes = []
#loop through all graphs 
for graph in graphs:
    #create path and sum
    path = []
    sum_path = 0
    main_sum = [float('inf')]  #this will keep track of actual path sum
    best_path_sum = [None]     #this will keep track of actual path

    #get the startig vertex (we need this list)
    start_vertex = list(graph.keys())[3]

    #append start vertext in the graph
    path.append(start_vertex)

    # Find the cycle for TSP
    start_time = time.time()
    find_hamiltonian_cycle(graph, start_vertex, path, sum_path, main_sum, best_path_sum)
    end_time = time.time()
    execution_time = end_time - start_time
    # print("Execution Time:", execution_time, "seconds")
    times.append(execution_time)
    sizes.append(graph['vertices'])

    hamiltonian_cycle = (best_path_sum[0], main_sum[0])
    hamiltonian_cycle_output(hamiltonian_cycle,execution_time,graph)


#create a chart that has the time in y axis and size in x axis 
print(times)
print(sizes)
plt.plot(sizes, times, 'o')  
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Size vs Time')  
plt.show()
