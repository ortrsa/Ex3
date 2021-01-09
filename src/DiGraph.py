from src.GraphInterface import GraphInterface
from NodaData import NodeData
import random


class DiGraph(GraphInterface):
    def __init__(self):
        self.graph = {}
        self.oute = {}
        self.ine = {}
        self.MC = 0
        self.edgeSize = 0

    def v_size(self) -> int:
        return len(self.graph)

    def e_size(self) -> int:
        return self.edgeSize

    def get_all_v(self) -> dict:
        return self.graph

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.ine[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:

        return self.oute[id1]

    def get_mc(self) -> int:
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:

        if id1 == id2:
            return False
        if id1 not in self.graph.keys() or id2 not in self.graph.keys():
            return False
        if weight < 0:
            return False
        if id2 not in self.oute[id1].keys():
            self.edgeSize += 1
        elif weight == self.oute[id1][id2]:
            return False
        self.MC += 1
        self.oute[id1][id2] = weight
        self.ine[id2][id1] = weight
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.graph is not None:
            if node_id in self.graph.keys():
                return False
        if pos is None:
            X = random.uniform(0.0, 10.0)
            Y = random.uniform(0.0, 10.0)
        else:
            X = pos[0]
            Y = pos[1]

        node = NodeData(X, Y, 0, Key=node_id)
        self.graph[node_id] = node
        self.oute[node_id] = {}
        self.ine[node_id] = {}
        self.MC += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.graph.keys():
            return False
        del self.graph[node_id]
        for i in self.all_in_edges_of_node(node_id).keys():
            self.remove_edge(node_id,i)
        for i in self.all_out_edges_of_node(node_id).keys():
            self.remove_edge(node_id,i)
        del self.oute[node_id]
        del self.ine[node_id]
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:

        if node_id1 not in self.graph.keys() or node_id2 not in self.graph.keys():
            return False
        if node_id2 not in self.oute[node_id1].keys():
            return False
        del self.oute[node_id1][node_id2]
        del self.ine[node_id2][node_id1]
        self.edgeSize -= 1
        self.MC += 1
        return True

    def __str__(self) -> str:
        return "Graph: |V|=" + str(len(self.graph)) + " , |E|=" + str(self.edgeSize)

    def as_dict(self):
        return self.__dict__

    def graph_maker(self, v_size: int, e_size: int):
        if e_size > v_size*(v_size-1):
            raise ValueError("to many edges")
        g = self
        for i in range(v_size):
            g.add_node(i)

        while g.edgeSize < e_size:
            a = random.randint(0, v_size)
            b = random.randint(0, v_size)
            c = random.uniform(1, 10)
            g.add_edge(a, b, c)

        return g
