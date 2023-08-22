import networkx as nx 
import matplotlib.pyplot as plt
# G = nx.gnp_random_graph(20,0.5) #0.5 probablity of edges
G = nx.erdos_renyi_graph(20, 1)
nx.draw(G)
plt.show()