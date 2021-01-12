from GraphAlgo import GraphAlgo
import networkx as nx
from network import Network
import time


file_list = ["../tests/G_30000_240000_1.json", "../tests/G_20000_160000_1.json", "../tests/G_10000_80000_1.json",
             "../tests/G_1000_8000_1.json",
             "../tests/G_100_800_1.json", "../tests/G_10_80_1.json"]

a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []

for i in file_list:
    my_g = GraphAlgo()
    my_g.load_from_json(i)
    netx = Network(i)
    my_g.save_to_json(i + "Ex2")

    print("----", i, "----")

    print("--", "connected_component(3)", "--")
    my_time_s = time.time()
    cc3 = my_g.connected_component(3)
    my_time_e = time.time()
    print("Ex3, len of connected component to 3", len(cc3), " time: ", my_time_e - my_time_s)
    a1.append(my_time_e - my_time_s)

    # my_time_s = time.time()
    # cc3nx = [i for i in nx.strongly_connected_components(netx.G) if 3 in i]
    # my_time_e = time.time()
    # print("nx,  len of connected component to 3", len(cc3nx[0]), " time: ", my_time_e - my_time_s)
    # a2.append(my_time_e - my_time_s)

    print("--", "connected_components()", "--")
    my_time_s = time.time()
    ccs = my_g.connected_components()
    my_time_e = time.time()
    print("Ex3, len of connected components", len(ccs), " time: ", my_time_e - my_time_s)
    a3.append(my_time_e - my_time_s)

    my_time_s = time.time()
    ccsnx = nx.strongly_connected_components(netx.G)
    my_time_e = time.time()
    print("nx,  len of connected components", ccsnx, " time: ", my_time_e - my_time_s)
    a4.append(my_time_e - my_time_s)

    print("--", "shortest path()", "--")
    my_time_s = time.time()
    short = my_g.shortest_path(1, 2)
    my_time_e = time.time()
    print("Ex3, shortest path ", short, " time: ", my_time_e - my_time_s)
    a5.append(my_time_e - my_time_s)

    my_time_s = time.time()
    shortnx = nx.dijkstra_path(netx.G, 1, 2)
    my_time_e = time.time()
    print("nx,  shortest path ", shortnx, " time: ", my_time_e - my_time_s)
    a6.append(my_time_e - my_time_s)
    print()


