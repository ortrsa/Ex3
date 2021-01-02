from DiGraph import DiGraph
from Edge import Edge
from NodaData import NodeData
import matplotlib.pyplot as plt
import numpy as np
from GraphAlgo import GraphAlgo
import random
import queue

if __name__ == '__main__':
    graph = DiGraph()
    graph.add_node(0)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    graph.add_node(6)

    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 2, 1)
    graph.add_edge(2, 1, 1)
    graph.add_edge(2, 4, 9)
    graph.add_edge(1, 3, 3)
    graph.add_edge(3, 4, 4)

    Ga = GraphAlgo(graph)
    # Ga.load_from_json("data/A3")
    Ga.plot_graph()
    print(Ga.shortest_path(0, 0))
