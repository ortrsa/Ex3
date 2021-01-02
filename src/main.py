from DiGraph import DiGraph
from Edge import Edge
from NodaData import NodeData
import matplotlib.pyplot as plt
import numpy as np
from GraphAlgo import GraphAlgo
import random

if __name__ == '__main__':
    graph = DiGraph()
    Ga = GraphAlgo(graph)
    Ga.load_from_json("data/A0")
    Ga.plot_graph()