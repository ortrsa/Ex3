from unittest import TestCase
import json
import networkx as nx
from GraphAlgo import GraphAlgo
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph


class Network:

    def __init__(self, filename: str):
        self.G = nx.DiGraph()
        d = json.load(open(filename))
        #self.G.add_nodes_from([i["id"] for i in d['Nodes']])
        for i in d['Nodes']:
            x = i["pos"].split(",")[0]
            y = i["pos"].split(",")[1]
            self.G.add_node(i["id"],pos= (float(x),float(y)))
        for i in d["Edges"]:
            self.G.add_edge(i["src"], i["dest"], weight=i["w"])

    def g_to_plot(self):
        pos = pos=nx.get_node_attributes(self.G,'pos')
        nx.draw(self.G, with_labels=True,pos= pos )
        plt.show()
