import networkx as nx
import matplotlib.pyplot as plt
import random


def create_graph():
    G = nx.Graph()
    for i in range(1, 101):
        G.add_node(i)
    return G


def visualize(G,labeldict,nodesize):
    nx.draw(G,labels = labeldict,node_size=nodesize)
    plt.show()


def assign_bmi(G):
    for each in G.nodes():
        G.nodes[each]['name'] = random.randint(15, 40)
        G.nodes[each]['type'] = 'person'

def get_labels(G):
    dict1={}
    for each in G.nodes:
        dict1[each]=G.nodes[each]['name']
    return dict1

def get_size(G):
    array1=[]
    for each in G.nodes:
        array1.append(G.nodes[each]['name']*20)
    return array1

G = create_graph()
assign_bmi(G)

labeldict = get_labels(G)
nodesize= get_size(G)

visualize(G,labeldict,nodesize)
