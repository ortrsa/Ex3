from DiGraph import DiGraph
from Edge import Edge
from NodaData import NodeData
import matplotlib.pyplot as plt
import numpy as np
from GraphAlgo import GraphAlgo
import random
import queue
import networkx as nx
import json
from network import Network

if __name__ == '__main__':
    filename = 'data/A5'
    Galgo = GraphAlgo()
    Galgo.load_from_json(filename)
    print(Galgo.shortest_path(1,6)[0])
    Galgo.G.remove_edge(13, 14)
    Galgo.G.remove_edge(14, 13)

    g_algo = Network(filename)
    print(nx.dijkstra_path_length(g_algo.G,1,6))
    g_algo.G.remove_edge(13,14)
    g_algo.G.remove_edge(14, 13)

    print([i for i in nx.strongly_connected_components(g_algo.G) if i.__contains__(1)])
    print(Galgo.connected_component(1))
    g_algo.g_to_plot()
