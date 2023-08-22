#Getting intro on creating generating nodes and modifying
import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.Graph()  # Undirected graph
# G = nx.DiGraph() #Directed graph
city_set = ["Bangalore", "Hyderabad", "Chennai",
            "Kolkata", "Jaipur", "Ahmedabad", "Pune", "Lucknow"]

for each in city_set:
    G.add_node(each)
print(G.nodes())

costs = []
value = 100
while value <= 2000:
    costs.append(value)
    value += 100
print(costs)    
# we are going to add 16 edges in the network
while G.number_of_edges() < 5:
    c1 = random.choice(list(G.nodes()))
    c2 = random.choice(list(G.nodes()))
    if c1 != c2 and G.has_edge(c1, c2)==0:
        w = random.choice(costs)
        G.add_edge(c1, c2, weight=w)
print(nx.is_connected(G))
for u in G.nodes():
    for v in G.nodes():
        print(u, v, nx.has_path(G, u, v))

# pos = nx.spectral_layout(G)
pos = nx.circular_layout(G)
#pos = nx.spring_layout(G)
nx.draw(G, pos,with_labels=True)
nx.draw_networkx_edge_labels(G,pos)
plt.show()


