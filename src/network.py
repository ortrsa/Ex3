from unittest import TestCase
import json
import networkx as nx
import matplotlib.pyplot as plt


class Network:
    """ this class is to read graph from json to Networkx and to draw this graph.  """
    def __init__(self, filename: str):
        self.G = nx.DiGraph()
        try:
            with open(filename, "r") as file:
                d = json.load(file)
                for i in d['Nodes']:
                    if "pos" not in i:
                        x = None
                        y = None
                    else:
                        xstr = i["pos"].split(",")[0]
                        ystr = i["pos"].split(",")[1]
                        x = float(xstr)
                        y = float(ystr)
                    self.G.add_node(i["id"], pos=(x, y))
                for i in d["Edges"]:
                    self.G.add_edge(i["src"], i["dest"], weight=i["w"])
        except IOError as e:
            print(e)

    def g_to_plot(self):
        pos = pos = nx.get_node_attributes(self.G, 'pos')
        nx.draw(self.G, with_labels=True, pos=pos)
        plt.show()
