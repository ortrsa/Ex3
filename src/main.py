from DiGraph import DiGraph
from Edge import Edge
from NodaData import NodeData
import matplotlib.pyplot as plt
import numpy as np
from GraphAlgo import GraphAlgo
import random
import queue

if __name__ == '__main__':

    g_algo = GraphAlgo()
    file = 'data/A5'
    g_algo.load_from_json(file)
    g_algo.get_graph().remove_edge(13, 14)
    g_algo.save_to_json(file + "_edited")
    dist, path = g_algo.shortest_path(1, 7)
    print(dist, path)
    dist, path = g_algo.shortest_path(47, 19)
    print(dist, path)
    dist, path = g_algo.shortest_path(20, 2)
    print(dist, path)
    dist, path = g_algo.shortest_path(2, 20)
    # print(dist, path)
    print(g_algo.connected_component(0))
    print(g_algo.connected_components())
    g_algo.plot_graph()
# Ga.save_to_json("try.txt")
