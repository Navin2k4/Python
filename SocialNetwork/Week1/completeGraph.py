import networkx as nx 
import matplotlib.pyplot as plt
Z=nx.complete_graph(10)
print(Z.nodes())
print(Z.edges())
print(Z.order()) #No of nodes
print(Z.size()) #No of edges
print(Z.number_of_edges()) #No of Edges
nx.draw(Z,with_labels=1)
plt.show()