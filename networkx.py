import networkx as nx
import matplotlib.pyplot as plt

'''
networkx code i found from repo
'''
def create_graph(csv_input):
    #extract header and problem parameters
    header = csv_input[0]
    problem = csv_input[1]
    
    #parse problem parameters
    _, graph_type, num_vertices, num_edges = problem
    
    #start the appropriate NetworkX graph
    if graph_type == 'u':
        G = nx.Graph()
    elif graph_type == 'd':
        G = nx.DiGraph()
    else:
        raise ValueError("Unknown graph type: should be 'u' (undirected) or 'd' (directed)")
    
    #add the nodes
    for item in csv_input[2:2 + num_vertices]:
        _, node = item
        G.add_node(node)
    
    #add the edges 
    for item in csv_input[2 + num_vertices:]:
        _, u, v, w = item
        G.add_edge(u, v, weight=w)
    
    #extract the name 
    instance_name = header[2]
    
    return G, instance_name

def visualize_graph(G, instance_name):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)  #positions

    #draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')

    #draw edges 
    if G.is_directed():
        nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')
    else:
        nx.draw_networkx_edges(G, pos, edge_color='gray')

    #draw labales
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.title(instance_name)
    plt.axis('off')
    plt.show()


input = [
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

G9, name9 = create_graph(input)
visualize_graph(G9, name9)
print(f"graph Name: {name9}")
print(f"number of Nodes: {G9.number_of_nodes()}")
print(f"number of Edges: {G9.number_of_edges()}")
