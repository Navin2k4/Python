# About dijkstra
import networkx as nx
import matplotlib.pyplot as plt
import random

def create_network(city_set,costs,num_edges):
    G = nx.Graph()  # Undirected graph
    for each in city_set:
        G.add_node(each)
    while G.number_of_edges() < num_edges:
        c1 = random.choice(list(G.nodes()))
        c2 = random.choice(list(G.nodes()))
        if c1 != c2 and G.has_edge(c1, c2) == 0:
            w = random.choice(costs)
            G.add_edge(c1, c2, weight=w)
    return G

city_set = ["Bangalore", "Hyderabad", "Chennai",
            "Kolkata", "Jaipur", "Ahmedabad", "Pune", "Lucknow"]
costs = []
value = 100
while value <= 2000:
    costs.append(value)
    value += 100
print(costs)

G=create_network(city_set,costs,10)

pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()

"""
u='Chennai'
v='Kolkata'
print("Shortest paths of the nodes : ",nx.dijkstra_path(G,u,v)) # Shows the shortest path of the nodes
print("Shortest path cost of node  : ", nx.dijkstra_path_length(G, u, v))  # Shows the path length of the nodes
print(nx.single_source_dijkstra_path(G, u))  # Shows the single shortest path of the nodes
print(nx.single_source_dijkstra_path_length(G, u))  # Shows the single path length of the nodes
nx.draw(G, pos, with_labels=True)
plt.show()
"""


"""
for u in G.nodes():
    for v in G.nodes():
        print(u, v, nx.has_path(G, u, v))

pos = nx.spectral_layout(G)
pos = nx.circular_layout(G)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G,pos)
plt.show()
"""