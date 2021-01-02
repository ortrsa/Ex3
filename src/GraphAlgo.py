from typing import List

import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
from Edge import Edge
from NodaData import NodeData
import matplotlib.pyplot as plt
from src.DiGraph import DiGraph
import json


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
                    new_pos = [float(i) for i in node["pos"].split(",", maxsplit=2)]
                    self.G.add_node(node["id"], new_pos[0], new_pos[1], new_pos[2])
                for edge in x["Edges"]:
                    self.G.add_edge(edge["src"], edge["dest"], edge["w"])

                print(self.G.Edges)

        except IOError as e:
            return e

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:

        x = [i.Pos[0] for i in self.G.get_all_v()]
        y = [i.Pos[1] for i in self.G.get_all_v()]
        plt.plot(x, y, "o")
        plt.show()
