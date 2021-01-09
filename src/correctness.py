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

    my_g = GraphAlgo()
    my_g.load_from_json(file_list[0])
    my_g.save_to_json("G_30000_240000_0Ex2.json")

    my_time_s = time.time()
    cc3 = my_g.connected_component(3)
    my_time_e = time.time()
    print(cc3, my_time_e - my_time_s)

    my_time_s = time.time()
    ccs = my_g.connected_components()
    my_time_e = time.time()
    print(ccs, my_time_e - my_time_s)

    my_time_s = time.time()
    short1 = my_g.shortest_path()
    my_time_e = time.time()
    print(short1,my_time_e - my_time_s)


    print(my_time_e - my_time_s)
    print()
    print()
    print()



    netx = Network(file_list)
    x_time_s = time.time()
    t3 = [i for i in nx.strongly_connected_components(netx.G)]

    x_time_e = time.time()

    print(x_time_e - x_time_s)


