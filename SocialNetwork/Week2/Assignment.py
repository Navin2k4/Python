import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G.add_edges_from([(1, 4), (2, 4), (3, 4),(5,4),(6,4)])
# G.add_edges_from([(1, 2), (2, 3), (3, 7),(7,4),(4,6),(6,5),(5,4),(2,4)])

print("Degree :", list(dict(nx.degree(G)).values()))

nx.draw(G)
plt.show()
print("Density : ",nx.density(G))
print(nx.clustering(G))