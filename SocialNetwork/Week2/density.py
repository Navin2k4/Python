import networkx as nx
import matplotlib.pyplot as plt

# Density = Number of Edges present / Total Possible Edges (4C2 - Probablity method)

G = nx.complete_graph(100)
print(nx.density(G))
# Density of complete graph is 1
print("\nDensity of the Graph is : ", nx.density(G))
# print("Clustering Coefficient : ", nx.clustering(G))
print("\nClustering Coefficient : ")
for i in dict(nx.clustering(G)).items():
    print(i)
print("\nAverage clustering Coefficient : ", nx.average_clustering(G))
print("\nDiameter of the Graph is : ", nx.diameter(G))
print("\nNumber of nodes : ",nx.number_of_nodes(G))
print("\nNumber of Edges : ",nx.number_of_edges(G))
# Density of graph without any node is 0

