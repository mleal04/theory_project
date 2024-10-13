# graphs
import csv
import networkx as nx
import matplotlib.pyplot as plt

# read graph data from CSV file
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

# create a NetworkX graph
def create_graph(graph):
    G = nx.Graph() if graph['type'] == 'u' else nx.DiGraph()
    
    # add vertices
    for vertex in graph.keys():
        if vertex not in ['type', 'vertices', 'edges']:
            G.add_node(vertex)

    # add edges
    for (u, v) in graph['edges']:
        G.add_edge(u, v)
    
    return G

def visualize(G, instance_name):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)  # Positions for all nodes

    # draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')

    # draw edges
    if G.is_directed():
        nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')
    else:
        nx.draw_networkx_edges(G, pos, edge_color='gray')

    # draw labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    plt.title(instance_name)
    plt.axis('off')
    plt.show()

def process(csv_input):
    graphs = read_csv(csv_input)
    times = []
    num_vertices = []

    for index, graph in enumerate(graphs, 1):
        G = create_graph(graph)  # Create the graph
        visualize(G, f"Graph Instance {index}")

        print(f"Number of Nodes: {G.number_of_nodes()}")
        print(f"Number of Edges: {G.number_of_edges()}")


# Run the process and visualize function
process('ham_path_graph_data.csv')
