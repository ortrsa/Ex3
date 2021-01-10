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
import time

if __name__ == '__main__':
    file_list = ["G_30000_240000_0.json", "G_20000_160000_0.json", "G_10000_80000_0.json", "G_1000_8000_0.json",
             "G_100_800_0.json", "G_10_80_0.json"]

    for i in file_list:
        my_g = GraphAlgo()
        my_g.load_from_json(i)
        netx = Network(i)

        print("----",i,"----")
        print("--","connected_component(3)","--" )
        my_time_s = time.time()
        cc3 = my_g.connected_component(3)
        my_time_e = time.time()
        print("Ex3, len of connected component to 3",len(cc3), " time: ", my_time_e - my_time_s)

        my_time_s = time.time()
        cc3nx = [i for i in nx.strongly_connected_components(netx.G) if 3 in i]
        my_time_e = time.time()
        print("nx,  len of connected component to 3",len(cc3nx[0])," time: ", my_time_e - my_time_s)
        print("--", "connected_components()","--")
        my_time_s = time.time()
        ccs = my_g.connected_components()
        my_time_e = time.time()
        print("Ex3, len of connected components",len(ccs)," time: " ,my_time_e - my_time_s)

        my_time_s = time.time()
        ccsnx = [i for i in nx.strongly_connected_components(netx.G)]
        my_time_e = time.time()
        print("nx,  len of connected components", len(ccsnx)," time: ", my_time_e - my_time_s)
        print("--", "shortest path()","--")
        my_time_s = time.time()
        short = my_g.shortest_path(1,2)
        my_time_e = time.time()
        print("Ex3, shortest path ",short," time: " ,my_time_e - my_time_s)

        my_time_s = time.time()
        shortnx = nx.dijkstra_path(netx.G,1,2)
        my_time_e = time.time()
        print("nx,  shortest path ",short," time: " ,my_time_e - my_time_s)

        print()









