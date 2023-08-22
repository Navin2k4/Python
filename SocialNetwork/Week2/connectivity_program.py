import networkx as nx
import random
import matplotlib.pyplot as plt
import numpy

def add_nodes(n):
    G = nx.Graph()  # Corrected typo
    G.add_nodes_from(range(n))
    return G

def add_random_edge(G):
    v1 = random.choice(list(G.nodes()))
    v2 = random.choice(list(G.nodes()))
    if v1 != v2 and not G.has_edge(v1, v2):
        G.add_edge(v1, v2)
    return G

def add_till_connectivity(G):
    while not nx.is_connected(G):
        G = add_random_edge(G)
    return G

def create_instance(n):
    G = add_nodes(n)
    G = add_till_connectivity(G)
    return G.number_of_edges()

def create_avg_instance(n):
    list1=[]
    for i in range(0,100):
            list1.append(create_instance(n))
    return numpy.average(list1)

def plot_connectivity():
    x = []
    y = []
    i = 10
    while i <= 200:
        x.append(i)
        y.append(create_avg_instance(i))
        i += 10 
    
    plt.xlabel('number of nodes')
    plt.ylabel('Number of edges required to connect the graph')  # Corrected typo
    plt.title('Emergence of connectivity')
    plt.plot(x, y)
    plt.show()

    x1=[]
    y1=[]
    i=10
    while i <= 200:
        x1.append(i)
        y1.append(i+numpy.log(i))
        i=i+10
    plt.plot(x1,y1)
    
plot_connectivity()
