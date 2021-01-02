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

for i in range(6):
    graph.add_node(i)

graph.add_edge(0, 2, 1)
graph.add_edge(2, 0, 1)
graph.add_edge(1, 2, 1)
graph.add_edge(2, 1, 1)
graph.add_edge(2, 3, 1)
graph.add_edge(3, 4, 1)
graph.add_edge(4, 5, 1)



# for i in range(6):
#     graph.add_edge(random.randint(0,99), random.randint(0,99), 5)


Ga = GraphAlgo(graph)
# Ga.load_from_json("data/A3")
# Ga.plot_graph()
print(Ga.connected_components())
