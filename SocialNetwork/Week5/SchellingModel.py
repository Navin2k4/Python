import matplotlib.pyplot as plt
import networkx as nx
import random

# Parameters
N = 20  # Grid size
empty_ratio = 0.1  # Ratio of empty cells
homophily_threshold = 0.3  # Homophily threshold

# Create a grid graph
G = nx.grid_2d_graph(N, N)

# Add attribute "type" to nodes (1 for agent, 0 for empty cell)
for node in G.nodes():
    if random.random() < empty_ratio:
        G.nodes[node]["type"] = 0
    else:
        G.nodes[node]["type"] = 1


def compute_homophily(node):
    neighbors = list(G.neighbors(node))  # Convert to list to compute len
    similar_neighbors = [n for n in neighbors if G.nodes[n]
                         ["type"] == G.nodes[node]["type"]]
    # Avoid division by zero
    return len(similar_neighbors) / max(1, len(neighbors))


def update_graph():
    global G
    nodes_to_move = []

    for node in G.nodes():
        if G.nodes[node]["type"] == 0:
            continue

        homophily = compute_homophily(node)
        if homophily < homophily_threshold:
            nodes_to_move.append(node)

    random.shuffle(nodes_to_move)

    for node in nodes_to_move:
        empty_neighbors = [n for n in G.neighbors(
            node) if G.nodes[n]["type"] == 0]
        if empty_neighbors:
            target_node = random.choice(empty_neighbors)
            G.nodes[target_node]["type"] = G.nodes[node]["type"]
            G.nodes[node]["type"] = 0


# Visualization
pos = dict((n, n) for n in G.nodes())


def draw():
    nx.draw(G, pos, node_size=50, node_color=[
            G.nodes[n]["type"] for n in G.nodes()])
    plt.show()


# Initial state
draw()

# Run the model
num_iterations = 50
for _ in range(num_iterations):
    update_graph()
    draw()
