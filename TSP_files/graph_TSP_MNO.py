import networkx as nx
import matplotlib.pyplot as plt
import time
import csv

def read_csv(csv_input):
    graphs = []
    current_graph = []

    for line in csv_input:
        if line[0] == 'c':
            if current_graph:
                graphs.append(current_graph)
                current_graph = []
        current_graph.append(line)

    if current_graph:
        graphs.append(current_graph)

    return graphs

def create_graph(graph_data):
    # Extract header and problem parameters
    header = graph_data[0]  # 'c' line
    problem = graph_data[1]  # 'p' line

    # Parse problem parameters
    _, graph_type, num_vertices, num_edges = problem
    num_vertices = int(num_vertices)
    num_edges = int(num_edges)

    # Initialize the appropriate NetworkX graph
    if graph_type == 'u':
        G = nx.Graph()
    elif graph_type == 'd':
        G = nx.DiGraph()
    else:
        raise ValueError("Unknown graph type: should be 'u' (undirected) or 'd' (directed)")

    # Add nodes
    for item in graph_data[2:2 + num_vertices]:
        _, node = item
        G.add_node(int(node))  # Ensure node is integer

    # Add edges
    for item in graph_data[2 + num_vertices:]:
        _, u, v, w = item
        G.add_edge(int(u), int(v), weight=float(w))

    # Extract instance name
    instance_name = header[2]

    return G, instance_name

def visualize_graph(G, instance_name):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)  # Positions for all nodes

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')

    # Draw edges with weights
    if G.is_directed():
        nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')
    else:
        nx.draw_networkx_edges(G, pos, edge_color='gray')

    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.title(instance_name)
    plt.axis('off')
    plt.show()

#read csv file --> make the graph directed even if it comes as undirected
def read_csv(csv_input_path):
    graphs = []
    graph = None
    
    #open and read the CSV file
    with open(csv_input_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for line in csv_reader:
            graphs.append(line)
    
    return graphs
    
# Read and parse the CSV input
graphs = read_csv('graphs.csv')
# Display graphs with NetworkX
for graph in graphs:
    try:
        G, name = create_graph(graph)
        visualize_graph(G, name)
        print(f"Graph Name: {name}")
        print(f"Number of Nodes: {G.number_of_nodes()}")
        print(f"Number of Edges: {G.number_of_edges()}\n")
    except Exception as e:
        print(f"An error occurred while processing {graph}: {e}\n")

