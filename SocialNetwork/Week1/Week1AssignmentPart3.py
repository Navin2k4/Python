"Exception Handling in NetworkX"

import networkx as nx
import matplotlib.pyplot as plt
import random
import sys
def create_network(city_set, costs, num_edges):

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

def add_random_edge(G,costs):
    c1 = random.choice(list(G.nodes()))
    c2 = random.choice(list(G.nodes()))
    if c1 != c2 and G.has_edge(c1, c2) == 0:
        w = random.choice(costs)
        G.add_edge(c1, c2, weight=w)

city_set = ["Bangalore", "Hyderabad", "Chennai",
            "Kolkata", "Jaipur", "Ahmedabad", "Pune", "Lucknow"]

costs = []
value = 100
while value <= 2000:
    costs.append(value)
    value += 100

G = create_network(city_set, costs, 0)

try:
    l = nx.dijkstra_path_length(G, 'Jaipur', 'Pune')
except:
    l = 10000
print('path length =', l)

x = [0]
y = [l]
for t in range(1,500):
    add_random_edge(G, costs)
    x.append(t)
    try:
        l = nx.dijkstra_path_length(G, 'Jaipur', 'Pune')
        y.append(l)
        print('Path length after', t, 'edges:', l)
        break
    except:
        l = 10000
        y.append(10000)
        print('No path')

plt.figure(num="Costs for Cities")
plt.title("Changes in traveling cost as more roads are added")
plt.xlabel('Time')
plt.ylabel('Traveling Cost')
plt.plot(x, y)
plt.show()