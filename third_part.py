from ast import main
import time
import matplotlib.pyplot as plt
''' traveling salesmen problem '''

#read csv file --> make the graph directed even if it comes as undirected
def read_csv(csv_input):
    graphs = []
    graph = None

    for line in csv_input:
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
            weight = float(line[3])
            graph[source].append((target, weight))  #add directed edge
            if graph['type'] == 'u':  #if graph is undirected, add reverse edge
                graph[target].append((source, weight))
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


#input

csv_input = [
['c', 1, 'TSP Instance 1'],
['p', 'u', 4, 6],
['v', 1],
['v', 2],
['v', 3],
['v', 4],
['e', 1, 2, 10],
['e', 1, 3, 15],
['e', 2, 3, 20],
['e', 2, 4, 25],
['e', 3, 4, 30],
['e', 1, 4, 35],
['c', 1, 'TSP Instance 2'],
['p', 'd', 4, 12],
['v', 1],
['v', 2],
['v', 3],
['v', 4],
['e', 1, 2,20],
['e', 2, 1, 15],
['e', 1, 3, 7],
['e', 3, 1, 10],
['e', 1, 4, 9],
['e', 4, 1, 13],
['e', 2, 4, 8],
['e', 4, 2, 10],
['e', 2, 3, 30],
['e', 3, 2, 25],
['e', 3, 4, 20],
['e', 4, 3, 15],
['c', 1, 'TSP Instance 3'],
['p', 'u', 5, 10],
['v', 1],
['v', 2],
['v', 3],
['v', 4],
['v', 5],
['e', 1, 2, 12],
['e', 1, 3, 8],
['e', 1, 4, 15],
['e', 1, 5, 10],
['e', 2, 3, 7],
['e', 2, 4, 9],
['e', 2, 5, 14],
['e', 3, 4, 6],
['e', 3, 5, 11],
['e', 4, 5, 5],
['c', 1, 'TSP Instance 4'],
['p', 'd', 6, 18],
['v', 1],
['v', 2],
['v', 3],
['v', 4],
['v', 5],
['v', 6],
['e', 1, 2, 20],
['e', 2, 1, 18],
['e', 1, 3, 25],
['e', 3, 1, 22],
['e', 1, 4, 30],
['e', 4, 1, 28],
['e', 1, 5, 24],
['e', 5, 1, 26],
['e', 1, 6, 35],
['e', 6, 1, 33],
['e', 2, 3, 15],
['e', 3, 2, 17],
['e', 2, 4, 10],
['e', 4, 2, 12],
['e', 2, 5, 20],
['e', 5, 2, 19],
['e', 2, 6, 25],
['e', 6, 2, 23],
['e', 3, 4, 8],
['e', 4, 3, 9],
['e', 3, 5, 14],
['e', 5, 3, 16],
['e', 3, 6, 22],
['e', 6, 3, 20],
['e', 4, 5, 7],
['e', 5, 4, 6],
['e', 4, 6, 18],
['e', 6, 4, 19],
['e', 5, 6, 12],
['e', 6, 5, 11],
['c', 1, 'TSP Instance 6'],
['p', 'u', 3, 3],
['v', 1],
['v', 2],
['v', 3],
['e', 1, 2, 10],
['e', 1, 3, 20],
['e', 2, 3, 15],
['c', 1, 'TSP Instance 7'],
['p', 'd', 5, 10],
['v', 1],
['v', 2],
['v', 3],
['v', 4],
['v', 5],
['e', 1, 2, 5],
['e', 2, 1, 5],
['e', 1, 3, 9],
['e', 3, 1, 9],
['e', 1, 4, 14],
['e', 4, 1, 14],
['e', 1, 5, 20],
['e', 5, 1, 20],
['e', 2, 3, 7],
['e', 3, 2, 7],
['e', 2, 4, 12],
['e', 4, 2, 12],
['e', 2, 5, 18],
['e', 5, 2, 18],
['e', 3, 4, 10],
['e', 4, 3, 10],
['e', 3, 5, 16],
['e', 5, 3, 16],
['e', 4, 5, 8],
['e', 5, 4, 8],
['c', 1, 'TSP Instance 8'],
['p', 'u', 7, 14],
['v', 1],
['v', 2],
['v', 3],
['v', 4],
['v', 5],
['v', 6],
['v', 7],
['e', 1, 2, 11],
['e', 1, 3, 14],
['e', 1, 4, 9],
['e', 1, 5, 16],
['e', 1, 6, 20],
['e', 1, 7, 25],
['e', 2, 3, 10],
['e', 2, 4, 13],
['e', 2, 5, 19],
['e', 2, 6, 22],
['e', 2, 7, 27],
['e', 3, 4, 12],
['e', 3, 5, 17],
['e', 3, 6, 21],
['e', 3, 7, 26],
['e', 4, 5, 8],
['e', 4, 6, 14],
['e', 4, 7, 19],
['e', 5, 6, 6],
['e', 5, 7, 11],
['e', 6, 7, 5],
['c', 1, 'TSP Instance 9'],
['p', 'd', 8, 16],
['v', 1],
['v', 2],
['v', 3],
['v', 4],
['v', 5],
['v', 6],
['v', 7],
['v', 8],
['e', 1, 2, 18],
['e', 2, 1, 17],
['e', 1, 3, 25],
['e', 3, 1, 23],
['e', 1, 4, 30],
['e', 4, 1, 28],
['e', 1, 5, 22],
['e', 5, 1, 24],
['e', 1, 6, 35],
['e', 6, 1, 33],
['e', 1, 7, 40],
['e', 7, 1, 38],
['e', 1, 8, 45],
['e', 8, 1, 43],
['e', 2, 3, 15],
['e', 3, 2, 16],
['e', 2, 4, 20],
['e', 4, 2, 19],
['e', 2, 5, 25],
['e', 5, 2, 23],
['e', 2, 6, 28],
['e', 6, 2, 26],
['e', 2, 7, 32],
['e', 7, 2, 30],
['e', 2, 8, 35],
['e', 8, 2, 33],
['e', 3, 4, 10],
['e', 4, 3, 11],
['e', 3, 5, 18],
['e', 5, 3, 20],
['e', 3, 6, 22],
['e', 6, 3, 21],
['e', 3, 7, 27],
['e', 7, 3, 25],
['e', 3, 8, 30],
['e', 8, 3, 28],
['e', 4, 5, 12],
['e', 5, 4, 13],
['e', 4, 6, 17],
['e', 6, 4, 16],
['e', 4, 7, 22],
['e', 7, 4, 20],
['e', 4, 8, 25],
['e', 8, 4, 23],
['e', 5, 6, 8],
['e', 6, 5, 9],
['e', 5, 7, 14],
['e', 7, 5, 13],
['e', 5, 8, 18],
['e', 8, 5, 17],
['e', 6, 7, 10],
['e', 7, 6, 11],
['e', 6, 8, 15],
['e', 8, 6, 14],
['e', 7, 8, 5],
['e', 8, 7, 6],
['c', 1, 'TSP Instance 10'],
['p', 'u', 4, 6],
['v', 1],
['v', 2],
['v', 3],
['v', 4],
['e', 1, 2, 14],
['e', 1, 3, 9],
['e', 1, 4, 16],
['e', 2, 3, 12],
['e', 2, 4, 7],
['e', 3, 4, 10],
['c', 1, 'TSP Instance 11'],
['p', 'd', 6, 12],
['v', 1],
['v', 2],
['v', 3],
['v', 4],
['v', 5],
['v', 6],
['e', 1, 2, 14],
['e', 2, 1, 13],
['e', 1, 3, 20],
['e', 3, 1, 18],
['e', 1, 4, 25],
['e', 4, 1, 23],
['e', 1, 5, 19],
['e', 5, 1, 21],
['e', 1, 6, 30],
['e', 6, 1, 28],
['e', 2, 3, 17],
['e', 3, 2, 16],
['e', 2, 4, 22],
['e', 4, 2, 20],
['e', 2, 5, 26],
['e', 5, 2, 24],
['e', 2, 6, 31],
['e', 6, 2, 29],
['e', 3, 4, 19],
['e', 4, 3, 18],
['e', 3, 5, 23],
['e', 5, 3, 21],
['e', 3, 6, 28],
['e', 6, 3, 26],
['e', 4, 5, 15],
['e', 5, 4, 14],
['e', 4, 6, 20],
['e', 6, 4, 18],
['e', 5, 6, 12],
['e', 6, 5, 11],
['c', 1, 'TSP Instance 12'],
['p', 'd', 7, 14],
['v', 1],
['v', 2],
['v', 3],
['v', 4],
['v', 5],
['v', 6],
['v', 7],
['e', 1, 2, 19],
['e', 2, 1, 17],
['e', 1, 3, 24],
['e', 3, 1, 22],
['e', 1, 4, 29],
['e', 4, 1, 27],
['e', 1, 5, 21],
['e', 5, 1, 23],
['e', 1, 6, 34],
['e', 6, 1, 32],
['e', 1, 7, 39],
['e', 7, 1, 37],
['e', 2, 3, 14],
['e', 3, 2, 13],
['e', 2, 4, 19],
['e', 4, 2, 17],
['e', 2, 5, 23],
['e', 5, 2, 21],
['e', 2, 6, 28],
['e', 6, 2, 26],
['e', 2, 7, 33],
['e', 7, 2, 31],
['e', 3, 4, 16],
['e', 4, 3, 15],
['e', 3, 5, 20],
['e', 5, 3, 18],
['e', 3, 6, 25],
['e', 6, 3, 23],
['e', 3, 7, 30],
['e', 7, 3, 28],
['e', 4, 5, 12],
['e', 5, 4, 11],
['e', 4, 6, 17],
['e', 6, 4, 15],
['e', 4, 7, 22],
['e', 7, 4, 20],
['e', 5, 6, 10],
['e', 6, 5, 9],
['e', 5, 7, 14],
['e', 7, 5, 13],
['e', 6, 7, 8],
['e', 7, 6, 7]
]

#make the graph --> list of graphs
graphs = read_csv(csv_input)

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
    print("Hamiltonian Cycle Path:", hamiltonian_cycle[0])
    print("Length of Cycle:", hamiltonian_cycle[1])

print(times)
print(sizes)

#create a chart that has the time in y axis and size in x axis 
plt.plot(sizes, times, 'o')  
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Size vs Time')  
plt.show()