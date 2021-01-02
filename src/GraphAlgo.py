from typing import List

import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from Edge import Edge
from NodaData import NodeData
import matplotlib.pyplot as plt
from src.DiGraph import DiGraph
import json
import queue


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None):
        self.G = graph

    def get_graph(self) -> GraphInterface:
        return self.G

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as file:
                x = json.load(file)
                for node in x["Nodes"]:
                    if node.__contains__("pos"):
                        new_pos = [float(i) for i in node["pos"].split(",", maxsplit=2)]
                        self.G.add_node(node["id"], new_pos[0], new_pos[1], new_pos[2])
                    else:
                        self.G.add_node(node["id"])
                if x.__contains__("Edges"):
                    for edge in x["Edges"]:
                        self.G.add_edge(edge["src"], edge["dest"], edge["w"])

                print(self.G.Edges)

        except IOError as e:
            return e

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        used = []
        unused = queue.PriorityQueue()
        nodeDis = {}
        nodePar = {}
        path = []

        self.G.Graph.get(id1).Weight = 0.0
        nodeDis[id1] = 0.0
        unused.put(self.G.Graph.get(id1))

        while not unused.empty():

            t = unused.get()
            used.append(t)

            for Nei in self.G.all_out_edges_of_node(t.Key):
                if not nodeDis.__contains__(Nei):
                    nodeDis[Nei] = -1
                tempNeiDis = nodeDis.get(Nei)
                tDis = nodeDis.get(t.Key)
                EdgeDis = self.G.Edges.get(t.Key).get(Nei).weight

                if (tempNeiDis == -1 or tempNeiDis > (tDis + EdgeDis)) and not used.__contains__(self.G.Graph.get(Nei)):
                    nodeDis[Nei] = tDis + EdgeDis
                    self.G.Graph.get(Nei).Weight = tDis + EdgeDis
                    unused.put(self.G.Graph.get(Nei))
                    nodePar[Nei] = t
        if self.G.Graph.get(id2).Weight == -1:
            return None, -1

        pointernode = self.G.Graph.get(id2)
        path.append(pointernode)
        while pointernode is not self.G.Graph.get(id1):
            pointernode = nodePar.get(pointernode.Key)
            path.append(pointernode)
        path.reverse()

        return self.G.Graph.get(id2).Weight, path

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:

        x = [i.Pos[0] for i in self.G.get_all_v()]
        y = [i.Pos[1] for i in self.G.get_all_v()]

        for i in self.G.get_all_v():
            for j in self.G.all_out_edges_of_node(i.Key):
                x1 = i.Pos[0]
                y1 = i.Pos[1]
                x2 = self.G.Graph[j].Pos[0]
                y2 = self.G.Graph[j].Pos[1]
                plt.plot([x1, x2], [y1, y2], "r-")
        plt.plot(x, y, "o")
        plt.show()
