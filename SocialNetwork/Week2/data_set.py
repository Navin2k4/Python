import networkx as nx
import matplotlib.pyplot as plt

def plot_deg_dist(G):
    all_degrees = list(dict(nx.degree(G)).values()) 
    print(all_degrees) # All the Degrees
    unique_degree = list(set(all_degrees))  # All the unique degrees
    print(unique_degree)
    count_of_degrees = []

    for i in unique_degree:
        x = all_degrees.count(i)
        count_of_degrees.append(x)
    
    print(count_of_degrees)

    plt.plot(unique_degree,count_of_degrees,'ro-')
    # plt.loglog(unique_degree,count_of_degrees,'yo-')
    plt.xlabel("Degrees")
    plt.ylabel("No of nodes")
    plt.title("Degree Distribution of Karate network")
    plt.show()

G = nx.read_gml('E:\Social Network\Week2\Datasets\karate.gml',label=None)

# plot_deg_dist(G)

print("\nDensity of the Graph is : ",nx.density(G))

# print("Clustering Coefficient : ", nx.clustering(G))

print("\nClustering Coefficient : ")
for i in dict(nx.clustering(G)).items():
    print(i)

print("\nAverage clustering Coefficient : ",nx.average_clustering(G))

print("\nDiameter of the Graph is : ",nx.diameter(G))

print("\nNumber of nodes : ", nx.number_of_nodes(G))

print("\nNumber of Edges : ", nx.number_of_edges(G))

# Density = Number of Edges present / Total Possible Edges (4C2 - Probablity method)
# Clustering Coefficient = Actual number of friendship / Total possible friendship
# Diameter is the maximum shortest path that we have to travel to go to one node form other node