from DiGraph import DiGraph

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
    filename = 'tests/G_100_800_1.json'
    Galgo = GraphAlgo()
    netx = Network(filename)
    Galgo.load_from_json(filename)

    print(Galgo.shortest_path(0,4))
    # print(Galgo.G.all_in_edges_of_node(14))
    Galgo.plot_graph()


