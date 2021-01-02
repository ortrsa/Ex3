from src.GraphInterface import GraphInterface
from Edge import Edge
from NodaData import NodeData
import random

graph: dict = {}
edges: dict = {}
parents: dict = {}
edgeSize: int = 0
MC: int = 0


class DiGraph(GraphInterface):
    def __init__(self):
        self.Graph = graph
        self.Edges = edges
        self.Parents = parents

    def v_size(self) -> int:
        return len(self.Graph)

    def e_size(self) -> int:
        return edgeSize

    def get_all_v(self) -> dict:
        return self.Graph.values()

    def all_in_edges_of_node(self, id1: int) -> dict:
        dict1 = {}
        itr = iter(parents[id1].keys())
        while True:
            try:

                temp = next(itr)
                dict1[temp] = parents[id1][temp].weight

            except StopIteration:
                break

        return dict1

    def all_out_edges_of_node(self, id1: int) -> dict:
        dict1 = {}
        itr = iter(edges[id1].keys())
        while True:
            try:

                temp = next(itr)
                dict1[temp] = edges[id1][temp].weight

            except StopIteration:
                break

        return dict1

    def get_mc(self) -> int:
        return MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        global MC
        global edgeSize
        global edges
        if id1 == id2:
            return False
        if id1 not in graph.keys() or id2 not in graph.keys():
            return False
        if weight < 0:
            raise ValueError
        if id2 not in dict(edges[id1]).keys():
            edgeSize += 1
        elif weight == edges[id1][id2].weight:
            return False
        MC += 1
        edge = Edge(id1, id2, weight)
        edges[id1][id2] = edge
        parents[id2][id1] = edge
        return True

    def add_node(self, node_id: int, X: float = None, Y: float = None, Z: float = 0) -> bool:
        global MC
        if graph is not None:
            if node_id in dict(graph).keys():
                return False
        if X is None:
            X = random.uniform(0.0, 10.0)
            Y = random.uniform(0.0, 10.0)
        node = NodeData(X, Y, Z, Key=node_id)
        graph[node_id] = node
        edges[node_id] = {}
        parents[node_id] = {}
        MC += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in graph.keys():
            return False
        del graph[node_id]
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        global edgeSize
        global MC
        if node_id1 not in graph.keys() or node_id2 not in graph.keys():
            return False
        if node_id2 not in edges[node_id1].keys():
            return False
        del edges[node_id1][node_id2]
        del parents[node_id2][node_id1]
        edgeSize -= 1
        MC += 1
        return True

    def __str__(self) -> str:

        return str(graph.values())
