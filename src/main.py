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

# for i in range(0, 100):
#     graph.add_node(i)
#
# for i in range(50):
#     graph.add_edge(random.randint(0,50),random.randint(50,99),1)

# for i in range(6):
#     graph.add_edge(random.randint(0,99), random.randint(0,99), 5)


Ga = GraphAlgo(graph)
Ga.load_from_json("try.txt")
Ga.plot_graph()
# for i in Ga.G.get_all_v().values():
#     print(i.as_dict())
# Ga.save_to_json("try.txt")
