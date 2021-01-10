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
    filename = 'data/A5'
    Galgo = GraphAlgo()
    netx = Network(filename)
    Galgo.load_from_json(filename)
    Galgo.G.remove_node(5)
    Galgo.G.remove_node(13)
    Galgo.G.remove_node(14)
    netx.G.remove_node(14)
    print(netx.G.out_edges(14))
    # print(Galgo.G.all_in_edges_of_node(14))
    Galgo.plot_graph()


