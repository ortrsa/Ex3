from src.GraphInterface import GraphInterface
from Edge import Edge
from NodaData import NodeData
import random


class DiGraph(GraphInterface):
    def __init__(self):
        self.graph = {}
        self.edges = {}
        self.parents = {}
        self.MC = 0
        self.edgeSize = 0

    def v_size(self) -> int:
        return len(self.graph)

    def e_size(self) -> int:
        return self.edgeSize

    def get_all_v(self) -> dict:
        return self.graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        dict1 = {}
        itr = iter(self.parents[id1].keys())
        while True:
            try:

                temp = next(itr)
                dict1[temp] = self.parents[id1][temp].w

            except StopIteration:
                break

        return dict1

    def all_out_edges_of_node(self, id1: int) -> dict:
        dict1 = {}
        itr = iter(self.edges[id1].keys())
        while True:
            try:

                temp = next(itr)
                dict1[temp] = self.edges[id1][temp].w

            except StopIteration:
                break

        return dict1

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:

        if id1 == id2:
            return False
        if id1 not in self.graph.keys() or id2 not in self.graph.keys():
            return False
        if weight < 0:
            raise ValueError
        if id2 not in dict(self.edges[id1]).keys():
            self.edgeSize += 1
        elif weight == self.edges[id1][id2].w:
            return False
        self.MC += 1
        edge = Edge(id1, id2, weight)
        self.edges[id1][id2] = edge
        self.parents[id2][id1] = edge
        return True

    def add_node(self, node_id: int, X: float = None, Y: float = None, Z: float = 0) -> bool:
        if self.graph is not None:
            if node_id in dict(self.graph).keys():
                return False
        if X is None:
            X = random.uniform(0.0, 10.0)
            Y = random.uniform(0.0, 10.0)
        node = NodeData(X, Y, Z, Key=node_id)
        self.graph[node_id] = node
        self.edges[node_id] = {}
        self.parents[node_id] = {}
        self.MC += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.graph.keys():
            return False
        del self.graph[node_id]
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:

        if node_id1 not in self.graph.keys() or node_id2 not in self.graph.keys():
            return False
        if node_id2 not in self.edges[node_id1].keys():
            return False
        del self.edges[node_id1][node_id2]
        del self.parents[node_id2][node_id1]
        self.edgeSize -= 1
        self.MC += 1
        return True

    def __str__(self) -> str:
        return "Graph: |V|=" + str(len(self.graph)) + " , |E|=" + str(self.edgeSize)

    def as_dict(self):
        return self.__dict__
