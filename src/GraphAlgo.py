import math
from typing import List

import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from NodaData import NodeData
import matplotlib.pyplot as plt
from src.DiGraph import DiGraph
import json
import queue


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None):
        if graph is None:
            graph = DiGraph()
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
                        self.G.add_node(node["id"], (new_pos[0], new_pos[1], new_pos[2]))
                    else:
                        self.G.add_node(node["id"])
                if x.__contains__("Edges"):
                    for edge in x["Edges"]:
                        self.G.add_edge(edge["src"], edge["dest"], edge["w"])

        except IOError as e:
            return e

    def save_to_json(self, file_name: str) -> bool:
        graph_dict = {}
        edge_list = []

        for i in self.G.oute.keys():
            for j in self.G.oute[i].keys():
                edge_map = {'src': i, 'w': self.G.oute[i][j], 'dest': j}
                edge_list.append(edge_map)

        try:
            with open(file_name, "w") as file:
                graph_dict["Edges"] = edge_list
                graph_dict["Nodes"] = [i for i in self.G.graph.values()]
                json.dump(graph_dict, default=lambda m: m.as_dict(), fp=file)
        except IOError as e:
            return e

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 not in self.G.get_all_v() or id2 not in self.G.get_all_v():
            raise ValueError("node not in the graph")
        used = []
        unused = queue.PriorityQueue()
        nodePar = {}
        path = []
        self.G.graph.get(id1).Weight = 0.0
        unused.put(self.G.graph.get(id1))

        while not unused.empty():

            t = unused.get()
            if t.id == id2:
                break
            if t.id in used:
                continue
            used.append(t.id)
            for Nei in self.G.all_out_edges_of_node(t.id):

                tempNeiDis = self.G.graph.get(Nei).Weight  # nodeDis.get(Nei)
                tDis = self.G.graph.get(t.id).Weight
                EdgeDis = self.G.oute.get(t.id).get(Nei)

                if tempNeiDis > (tDis + EdgeDis):
                    self.G.graph.get(Nei).Weight = tDis + EdgeDis
                    unused.put(self.G.graph.get(Nei))
                    nodePar[Nei] = t

        if self.G.graph.get(id2).Weight == math.inf:
            self.reset_w()
            return math.inf, path

        pointernode = self.G.graph.get(id2)
        path.append(pointernode)
        while pointernode.id is not id1:
            pointernode = nodePar.get(pointernode.id)
            path.append(pointernode)
        path.reverse()
        res = self.G.graph.get(id2).Weight
        self.reset_w()
        return res, path

    def connected_component(self, id1: int) -> list:
        connected1 = set()
        connected_to = []
        connected_from = []

        connected1.add(id1)

        while len(connected1) > 0:
            for node in self.G.all_out_edges_of_node(connected1.pop()):

                if self.G.graph.get(node).Weight == math.inf:
                    self.G.graph.get(node).Weight = 0
                    connected1.add(node)
                    connected_to.append(node)

        connected1.add(id1)

        while len(connected1) > 0:
            for node in self.G.all_in_edges_of_node(connected1.pop()):
                if self.G.graph.get(node).Tag == -1:
                    self.G.graph.get(node).Tag = 0
                    connected1.add(node)
                    connected_from.append(node)

        res = list(set(connected_from).intersection(connected_to))
        for node in self.G.get_all_v().values():
            node.Weight = math.inf
            node.Tag = -1
        if len(res) == 0:
            res.append(id1)
        return res

    def connected_components(self) -> List[list]:
        all_nodes = set(self.G.get_all_v().keys())
        res = []

        while len(all_nodes) > 0:
            list1 = self.connected_component(all_nodes.pop())
            res.append(list1)

            all_nodes = all_nodes - (set(list1))
        return res

    def plot_graph(self) -> None:

        x = [i.pos[0] for i in self.G.get_all_v().values()]
        y = [i.pos[1] for i in self.G.get_all_v().values()]

        for i in self.G.get_all_v().values():
            for j in self.G.all_out_edges_of_node(i.id):
                x1 = i.pos[0]
                y1 = i.pos[1]
                x2 = self.G.graph[j].pos[0]
                y2 = self.G.graph[j].pos[1]
                plt.plot([x1, x2], [y1, y2], "r-")
        plt.plot(x, y, "o")
        plt.show()

    def reset_w(self):
        for node in self.G.get_all_v().values():
            node.Weight = math.inf
