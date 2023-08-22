import networkx as nx
import itertools

def communities_brute(G):
    nodes = G.nodes()
    n = G.number_of_nodes()

    first_community = []
    for i in range(1, n//2 + 1):
        comb = [list(x) for x in itertools.combinations(nodes, i)]
        first_community.extend(comb)

    # Which division is the best
    num_inter_edges = G.number_of_edges()
    ratio = []  # Ratio of number of intra and number of inter-community edges

    for i in range(len(first_community)):
        second_community = list(set(nodes) - set(first_community[i]))
        num_intra_edge1 = G.subgraph(first_community[i]).number_of_edges()
        num_intra_edge2 = G.subgraph(second_community).number_of_edges()
        num_inter_edges = G.number_of_edges() - num_intra_edge1 - num_intra_edge2
        ratio.append((num_intra_edge1 + num_intra_edge2) / num_inter_edges)

    max_value = max(ratio)
    max_index = ratio.index(max_value)

    print(first_community[max_index], list(
        set(nodes) - set(first_community[max_index])))


G = nx.barbell_graph(4, 2)
communities_brute(G)
