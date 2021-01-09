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
    # digraph = DiGraph()
    # digraph.graph_maker(1000000,2000000)
    # g_algo = GraphAlgo(digraph)
    # print(g_algo.G)
    filen = "../data/A5"

    temp = DiGraph()
    for i in range(5):
        temp.add_node(i)
    temp.add_edge(0,1,1)
    temp.add_edge(1, 2, 1)
    temp.add_edge(1, 3, 1)
    temp.add_edge(2, 1, 1)
    temp.add_edge(2, 0, 1)
    temp.add_edge(3, 4, 1)
    temp.add_edge(4, 1, 1)
    # temp.add_edge(4, 1, 1)
    my_g = GraphAlgo(temp)
    print(my_g.G.e_size())
    print(my_g.G.remove_node(1))


    print(my_g.G.all_out_edges_of_node(2))
    print(my_g.G.e_size())
    # my_g.plot_graph()

    # t1 = my_g.shortest_path(2,3)


    # print(t1)
    print()
    print()
    print()

    # filen = "G_1000_8000_0.json"
    # my_g = GraphAlgo()
    # my_g.load_from_json(filen)
    # my_time_s = time.time()
    # # my_g.save_to_json("G_30000_240000_0Ex2.json")
    # # t1 = my_g.connected_components()
    # t2 = my_g.shortest_path(1, 2)
    # # short1 = my_g.connected_component(378)
    # my_time_e = time.time()
    #
    # # print(short1,my_time_e - my_time_s)
    # # print(t1, my_time_e - my_time_s)
    # print(t2, my_time_e - my_time_s)
    # print()
    # filen = "G_30000_240000_0.json"
    netx = Network(filen)
    x_time_s = time.time()
    t3 = [i for i in nx.strongly_connected_components(netx.G)]
    # t4 = nx.dijkstra_path(netx.G,1,2)
    # short2 = [i for i in nx.strongly_connected_components(netx.G) if 378 in i]
    x_time_e = time.time()
    # print(short2, x_time_e-x_time_s)
    # print(t3, x_time_e-x_time_s)
    print( x_time_e - x_time_s)
# print(nx.dijkstra_path_length(g_algo.G, 1, 6))
# g_algo.G.remove_edge(13, 14)
# g_algo.G.remove_edge(14, 13)

# print([i for i in nx.strongly_connected_components(g_algo.G) if i.__contains__(1)])
# print(Galgo.connected_component(1))
# g_algo.g_to_plot()


# def graph_maker(v_size: int, e_size: int):
#     g = DiGraph()
#     for i in range(v_size):
#         g.add_node(i)
#
#     for i in range(e_size):
#         a = random.randint(e_size)
#         b = random.randint(e_size)
#         c = random.uniform(0, 10)
#         if a != b:
#             g.add_edge(a, b, c)
#     return g
