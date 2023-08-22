import networkx as nx #Shortform for networkx
import matplotlib.pyplot as plt
G=nx.Graph()
# Adding he nodes
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
#Adding the edges
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(2, 6)
G.add_edge(4, 5)
G.add_edge(4, 6)
print("The nodes are : ", G.nodes())  # Display all the nodes
print("The Edges are : ", G.edges())  # Disply all the edges as tuple in list
nx.draw(G,with_labels=1)
plt.show()
